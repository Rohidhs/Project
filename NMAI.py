import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import pyjokes
from newsapi import NewsApiClient
from pytube import Search
from dateutil import parser

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def perform_google_search(query):
    """Function to perform a Google search."""
    speak("Performing Google search...")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def get_weather(api_key, city):
    """Function to get weather information from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    except requests.RequestException:
        return None

def recognize_speech():
    """Function to recognize speech using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        return "Sorry, the service is unavailable."

def set_reminder(reminder_time, reminder_message):
    """Function to set a reminder."""
    now = datetime.datetime.now()
    try:
        reminder_time = parser.parse(reminder_time)
        delay = (reminder_time - now).total_seconds()
        if delay > 0:
            speak(f"Reminder set for {reminder_time}.")
            time.sleep(delay)
            speak(f"Reminder: {reminder_message}")
        else:
            speak("The time you entered has already passed.")
    except ValueError:
        speak("The time format is incorrect. Please use a recognizable date and time format.")

def handle_reminder_query(query):
    """Function to handle reminder queries."""
    query = query.replace("set reminder", "").strip()
    parts = query.split(" at ")
    if len(parts) == 2:
        reminder_message = parts[0].strip()
        reminder_time = parts[1].strip()
        set_reminder(reminder_time, reminder_message)
        return f"Reminder set for {reminder_time} to {reminder_message}."
    else:
        speak("Please provide the reminder in the format 'set reminder [your reminder message] at [YYYY-MM-DD HH:MM:SS]' or a recognizable date and time format.")
        return "Sorry, I couldn't understand the reminder time."

def play_music_on_youtube(song_name):
    """Function to play a requested song on YouTube."""
    speak(f"Searching for {song_name} on YouTube.")
    search = Search(song_name)
    result = search.results[0]
    webbrowser.open(result.watch_url)
    speak(f"Playing {song_name} on YouTube.")

def handle_music_query(query):
    """Function to handle music play queries."""
    if 'play music' in query:
        song_name = query.replace('play music', '').strip()
        if song_name:
            play_music_on_youtube(song_name)
            return f"Playing {song_name} on YouTube."
        else:
            return "Sorry, I couldn't understand the song name."
    return "No music command detected."

def tell_joke():
    """Function to tell a joke."""
    joke = pyjokes.get_joke()
    speak(joke)
    return joke

def handle_joke_query(query):
    """Function to handle joke queries."""
    if 'joke' in query:
        return tell_joke()

def get_news(api_key, query):
    """Function to get news updates."""
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(q=query, language='en', country='us')
    articles = top_headlines['articles']
    if articles:
        news = [article['title'] for article in articles[:5]]
        news_str = ". ".join(news)
        speak(news_str)
        return news_str
    else:
        return "Sorry, no news found for that topic."

def handle_news_query(query, api_key):
    """Function to handle news queries."""
    query = query.replace("news about", "").strip()
    return get_news(api_key, query)

def handle_query(query, api_keys):
    """Function to handle various queries."""
    if 'wikipedia' in query:
        return handle_wikipedia_query(query)
    elif 'google search' in query:
        query = query.replace("google search", "").strip()
        perform_google_search(query)
        return "I have performed the Google search."
    elif 'weather' in query:
        query = query.replace("weather", "").strip()
        return handle_weather_query(query, api_keys['weather'])
    elif 'time' in query:
        return datetime.datetime.now().strftime("The current time is %H:%M")
    elif 'date' in query:
        return datetime.datetime.now().strftime("Today's date is %B %d, %Y")
    elif 'how are you' in query:
        response = "I'm fine, thank you"
        speak(response)
        return response
    elif 'what is your name' in query:
        response = "My name is Smartypants, your personal AI assistant."
        speak(response)
        return response
    elif 'who am i' in query:
        response = "You are my boss"
        speak(response)
        return response
    elif 'set reminder' in query:
        return handle_reminder_query(query)
    elif 'play music' in query:
        return handle_music_query(query)
    elif 'joke' in query:
        return handle_joke_query(query)
    elif 'news about' in query:
        return handle_news_query(query, api_keys['news'])
    else:
        response = "I'm sorry, I can't help with that right now."
        speak(response)
        return response

def handle_wikipedia_query(query):
    """Function to handle Wikipedia queries."""
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "").strip()
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results for {query}, please be more specific."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

def handle_weather_query(query, api_key):
    """Function to handle weather queries."""
    speak("Getting weather information...")
    weather_data = get_weather(api_key, query)
    if weather_data:
        result = (f"Weather in {weather_data['city']}: "
                  f"Temperature: {weather_data['temperature']}°C, "
                  f"Description: {weather_data['description']}, "
                  f"Humidity: {weather_data['humidity']}%, "
                  f"Wind Speed: {weather_data['wind_speed']} m/s.")
        speak(result)
        return result
    else:
        result = "Sorry, I couldn't find the weather information for that location."
        speak(result)
        return result

def main():
    weather_api_key = "6e6f9659fef62e5c5d1103979100d281"
    news_api_key = "dbe57b028aeb41e285a226a94865f7a7"
    api_keys = {'weather': weather_api_key, 'news': news_api_key}
    while True:
        query = recognize_speech()
        if "stop" in query:
            speak("Goodbye! Have a nice day!")
            break
        response = handle_query(query, api_keys)
        print(response)
        speak(response)

if __name__ == '__main__':
    main()