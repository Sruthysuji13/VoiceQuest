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

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/VoiceQuest.git
cd VoiceQuest
```

### 2. Install the required libraries

```bash
pip install wolframalpha wikipedia SpeechRecognition pyaudio
```

> **Note:** PyAudio installation can require additional setup depending on your operating system.

### 3. Configure WolframAlpha

The application requires a **WolframAlpha App ID**.

For security, it is recommended to store the App ID as an environment variable instead of directly placing it in the source code.

Example:

```python
import os
import wolframalpha

app_id = os.getenv("WOLFRAM_APP_ID")
client = wolframalpha.Client(app_id)
```

Then configure the environment variable:

```bash
WOLFRAM_APP_ID=your_app_id
```

---

## ▶️ Running the Application

Run the Python file:

```bash
python voicequest.py
```

You should see:

```text
Speak something...
```

Speak a question such as:

```text
What is the capital of France?
```

or:

```text
What is 25 multiplied by 16?
```

The recognized query is processed and the answer is displayed in a GUI window.

To exit the application, say:

```text
stop
```

---

## 🧩 Main Components

### Speech Recognition

The project uses the `SpeechRecognition` library to capture microphone input and convert spoken language into text.

```python
audio = r.listen(source)
text = r.recognize_google(audio)
```

### WolframAlpha

WolframAlpha is used as the primary source for answering queries, particularly computational and factual questions.

```python
res = client.query(query)
answer = next(res.results).text
```

### Wikipedia Fallback

If WolframAlpha does not return a result, the application attempts to retrieve a summary from Wikipedia.

```python
answer = wikipedia.summary(query, sentences=5)
```

### Tkinter GUI

The retrieved answer is displayed using a simple Tkinter text window.

```python
text_widget = Text(window, wrap=WORD)
text_widget.insert(END, answer)
```

---

## 🧪 Example

**User:**

> What is the square root of 144?

**VoiceQuest:**

```text
12
```

Another example:

**User:**

> Who is Albert Einstein?

If WolframAlpha does not return a suitable result, VoiceQuest attempts to retrieve a summary from Wikipedia.

---

## ⚠️ Error Handling

VoiceQuest handles several common runtime situations:

* Speech that cannot be understood
* Google Speech Recognition service errors
* WolframAlpha query failures
* Wikipedia disambiguation results
* Wikipedia pages that do not exist
* Unexpected runtime errors

---

## 🚀 Future Improvements

Potential improvements include:

* 🔐 Secure API-key management using `.env`
* 🗣️ Support for multiple languages
* 🔊 Text-to-speech responses
* 💬 Conversation history
* 🎨 Improved graphical interface
* 🤖 Integration with modern LLMs
* 🌐 Support for additional knowledge sources
* ⚡ Asynchronous query processing
* 🧠 Context-aware conversations

---

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python programming
* API integration
* Speech recognition
* Exception handling
* GUI development with Tkinter
* External knowledge retrieval
* Microphone/audio processing
* Basic voice-assistant architecture

---

## 📄 License

This project is available for educational and personal use. Add a license such as **MIT License** if you want others to freely reuse and modify the code.

---

## 👩‍💻 Author

**Sruthy Suji**

Developed as a Python-based voice assistant project exploring speech recognition and knowledge retrieval.
