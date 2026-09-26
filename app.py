#voicequest
import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time
import pyaudio

# Initialize the WolframAlpha client
app_id = "L6EUTJ-L4R95QYK7T"
client = wolframalpha.Client(app_id)

def main():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                if text.lower() == "stop":
                    print("Stopping the program.")
                    break
                else:
                    process_query(text)
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

def process_query(query):
    window = Tk()
    window.geometry("700x600")
    window.title("Query Result")

    answer = ""
    try:
        res = client.query(query)
        answer = next(res.results).text
    except StopIteration:
        answer = None
    except Exception as e:
        answer = f"An error occurred: {e}"
    
    if not answer:
        try:
            answer = wikipedia.summary(query, sentences=5)  
        except wikipedia.DisambiguationError as e:
            answer = f"Disambiguation error: {e.options}"
        except wikipedia.PageError:
            answer = "No page found for your query."
        except Exception as e:
            answer = f"An error occurred while searching Wikipedia: {e}"

    show_answer(window, answer)

def show_answer(window, answer):
    text_widget = Text(window, wrap=WORD, font="times 15 bold")
    text_widget.insert(END, answer)
    text_widget.pack(pady=20, padx=10)
    window.after(50000, window.destroy)  
    window.mainloop()


if __name__ == "__main__":
    main()
