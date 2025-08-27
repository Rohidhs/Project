# 🤖 Smartypants – Your Personal AI Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

Smartypants is a **voice-controlled AI assistant** built with Python. It can search Wikipedia, fetch weather updates, tell jokes, set reminders, play music on YouTube, deliver news headlines, and more – all through your voice commands.

---

## ✨ Features

- **Voice Recognition** – Listens to your commands using Google Speech Recognition.  
- **Text-to-Speech (TTS)** – Responds using `pyttsx3`.  
- **Google Search** – Opens search results directly in your browser.  
- **Wikipedia Search** – Fetches concise summaries for any topic.  
- **Weather Reports** – Real-time weather data using OpenWeather API.  
- **Reminders** – Alerts you at a specified time.  
- **YouTube Music** – Plays songs directly on YouTube using `pytube`.  
- **Jokes** – Lightens your mood with random jokes.  
- **News Headlines** – Delivers the latest headlines using NewsAPI.  

---

## 📂 Project Structure

```

.
├── NMAI  .py       # Main script for Smartypants
├── README.md          # Project documentation
└── from siri to smartypants phase 3.pdf  # Abstract

````

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Rohidhs/From-Siri-to-SmartyPants
````

### 2. Install dependencies

```bash
pip install pyttsx3 speechrecognition wikipedia requests pyjokes newsapi-python pytube python-dateutil
```

## ▶️ How to Run

```bash
NMAI.py
```

Once running, you can say commands like:

* **“Wikipedia Albert Einstein”**
* **“Google search Python programming”**
* **“Weather in New York”**
* **“Play music Shape of You”**
* **“Set reminder buy milk at 2025-08-28 10:00:00”**
* **“Tell me a joke”**
* **“News about technology”**
* **“Stop”** (to exit)

---

## 📌 Known Issues

* **Reminders block the assistant** – current implementation uses `time.sleep()`.
* **API failures** – no graceful fallback if APIs return empty results.
* **Speech recognition errors** – unrecognized voice commands still trigger fallback messages.
* **YouTube search** – no check for empty results.

---

## 🚀 Future Enhancements

* Run reminders on separate threads (non-blocking).
* Add GUI using Tkinter or PyQt.
* Integrate Spotify, Google Calendar, or Email APIs.
* Offline speech recognition models for privacy.
* Improved NLP for more natural commands.

---

## 🙌 Acknowledgements

* [Google Speech Recognition](https://pypi.org/project/SpeechRecognition/)
* [pyttsx3](https://pypi.org/project/pyttsx3/) for TTS
* [Wikipedia API](https://pypi.org/project/wikipedia/)
* [OpenWeather API](https://openweathermap.org/)
* [NewsAPI](https://newsapi.org/)
* [pytube](https://pytube.io/en/latest/) for YouTube playback
* [pyjokes](https://pypi.org/project/pyjokes/) for humor

---

## 👤 Author

**Rohidh Sakthivel**
*Full Stack Developer & AI Enthusiast*
