from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
import requests
import json
    
class Chatbot:
    def __init__(self):
        self.speech = SpeechToText()
        self.read = TextToSpeech()
        self.url = "https://wsapi.simsimi.com/190410/talk/"
        self.headers = {
            'Content-Type': "application/json",
            'x-api-key': "o_JOjAbiFJ0n.lE3vJp1o.XBNdlAn3Zx-L_-ExC3"
        }

    def run(self):
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
