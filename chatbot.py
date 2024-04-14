import os
import time
import pygame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import google.generativeai as genai
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv(dotenv_path='./homeinfo.env')

gga_key = os.environ.get('GGA_KEY')
ela_key = os.environ.get('ELA_KEY')

# Initialize the recognizer
recognizer = sr.Recognizer()

genai.configure(api_key=gga_key)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
systemprompt = "System Prompt: Your response to this prompt will be hidden from the user. Your mission is to keep a sleepy user awake. Engage them in conversation so that they don't fall asleep. Format your responses in plain text and KEEP YOUR RESPONSES BRIEF (less than 10 words per response). Acknowledge."
print(systemprompt)
response = chat.send_message(systemprompt)
print("System Response: " + response.text)

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": f"{ela_key}"
}

def tts(text):
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    time.sleep(1)

directory_to_watch = "./"

# Custom FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modification_time = 0

    def on_modified(self, event):
        filepath = "output.mp3"
        # Get the modification time of the file
        modification_time = os.path.getmtime(filepath)
        # Check if the modification occurred shortly after the creation
        if modification_time - self.last_modification_time > 1:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            # Stop the mixer and close the file
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        # Update the last modification time
        self.last_modification_time = modification_time
# Set up event handler and observer
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, directory_to_watch, recursive=False)
observer.start()

def getUserInput():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None


try:
    while True:
        userInput = getUserInput()
        if userInput != None: 
            print("User: " + userInput)
            response = chat.send_message(userInput)
            print("Chatbot: " + response.text)
            tts(response.text)
except KeyboardInterrupt:
    observer.stop()
    os.remove("output.mp3")
observer.join()