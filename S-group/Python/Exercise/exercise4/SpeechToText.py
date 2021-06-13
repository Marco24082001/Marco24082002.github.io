import speech_recognition as sr
import keyboard

class SpeechToText:
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
            except sr.UnknownValueError:
                print("speech was unintelligible")
                print("\"ENTER\" to speak again")
                keyboard.wait("\n")
            except Exception as ex:
                print(ex)
                print("\"ENTER\" to speak again")
                keyboard.wait("\n")
            self.recognizer = sr.Recognizer()

x = 'Vo thah vi'