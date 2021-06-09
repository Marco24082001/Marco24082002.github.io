import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import requests
import keyboard
import json

class SpeechTotext:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.message = None

    def Listen(self):
        check = True
        while check:
            try:
                print("SPEAK:")
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    self.message = self.recognizer.recognize_google(audio, language='vi').lower()
                    check = False
            except sr.RequestError:
                print("API was unreachable or unresponsive")
                print("\"ENTER\" to speak again")
                keyboard.wait("\n")
                self.recognizer = sr.Recognizer()
            except sr.UnknownValueError:
                print("speech was unintelligible")
                print("\"ENTER\" to speak again")
                keyboard.wait("\n")
                self.recognizer = sr.Recognizer()

class TextToSpeech:
    def __init__(self):
        self.fileName = "voice.mp3"
        self.tts = gTTS(text="None", lang="vi")

    def Read(self, message):
        self.tts.text = message
        self.tts.save(self.fileName)
        playsound.playsound(self.fileName)
        os.remove(self.fileName)
    
class Chatbot:
    def __init__(self):
        self.speech = SpeechTotext()
        self.read = TextToSpeech()
        self.url = "https://wsapi.simsimi.com/190410/talk/"
        self.headers = {
            'Content-Type': "application/json",
            'x-api-key': "o_JOjAbiFJ0n.lE3vJp1o.XBNdlAn3Zx-L_-ExC3"
        }

    def Chat(self):
        while True:
            try:
                self.speech.Listen()
                print(f"\033[95mYou: {self.speech.message}")
                payload = "{\n\t\"utext\": \"" + self.speech.message + "\", \n\t\"lang\": \"vi\" \n}"
                response = requests.post(self.url, data=payload.encode(), headers=self.headers)
                response = json.loads(response.text)
                print(f"\033[91mSimi : {response['atext']}")
                self.read.Read(response['atext'])
            except Exception as ex: 
                print(ex)
                        
chat = Chatbot()
chat.Chat()
