import os
import playsound
from gtts import gTTS

class TextToSpeech:
    def __init__(self):
        self.fileName = "voice.mp3"
        self.tts = gTTS(text="None", lang="vi")

    def Read(self, message):
        self.tts.text = message
        self.tts.save(self.fileName)
        playsound.playsound(self.fileName)
        os.remove(self.fileName)