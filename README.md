# 🎙️ VoiceQuest

**VoiceQuest** is a Python-based voice assistant that listens to spoken queries, converts speech into text, searches for answers using **WolframAlpha**, and falls back to **Wikipedia** when a direct computational answer is unavailable.

The project combines **speech recognition, natural language interaction, knowledge retrieval, and a simple Tkinter GUI** into one lightweight desktop application.

---

## ✨ Features

* 🎤 **Voice Input** – Accepts questions through the microphone.
* 🗣️ **Speech-to-Text** – Uses Google Speech Recognition to convert spoken queries into text.
* 🧮 **WolframAlpha Integration** – Retrieves computational and factual answers.
* 📚 **Wikipedia Fallback** – Searches Wikipedia when WolframAlpha cannot provide an answer.
* 🖥️ **Graphical Interface** – Displays responses in a Tkinter window.
* ⏹️ **Voice Stop Command** – Say `stop` to terminate the application.
* ⚠️ **Error Handling** – Handles unclear speech, API errors, and unavailable Wikipedia pages.

---

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition** – Speech-to-text processing
* **PyAudio** – Microphone/audio input
* **WolframAlpha API** – Computational knowledge retrieval
* **Wikipedia API** – Knowledge lookup and fallback search
* **Tkinter** – Desktop graphical interface

---

## 🏗️ How It Works

```text
             🎤 User speaks
                   │
                   ▼
          Speech Recognition
                   │
                   ▼
             Text Query
                   │
                   ▼
            WolframAlpha
              /       \
          Answer      No Answer
             │            │
             │            ▼
             │        Wikipedia
             │            │
             └──────┬─────┘
                    ▼
             Tkinter GUI
                    │
                    ▼
             Display Answer
```

### Query Flow

1. The application activates the microphone.
2. The user speaks a question.
3. `SpeechRecognition` converts the audio into text.
4. The text is sent to **WolframAlpha**.
5. If WolframAlpha returns an answer, it is displayed.
6. If no answer is available, the application searches **Wikipedia**.
7. The result is displayed in a Tkinter window.
8. Saying **"stop"** terminates the application.

---

## 📁 Project Structure

```text
VoiceQuest/
│
├── voicequest.py
└── README.md
```

---

## ▶️ Running the Application

Run the Python file:

```bash
python voicequest.py
```
---
## 👩‍💻 Author

**Sruthy Suji**

Developed as a Python-based voice assistant project exploring speech recognition and knowledge retrieval.
