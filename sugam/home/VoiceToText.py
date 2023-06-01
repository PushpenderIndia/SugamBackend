import speech_recognition as sr

class VoiceToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Unable to recognize speech")
            except sr.RequestError as e:
                print("Error: {0}".format(e))

if __name__ == "__main__":
    converter = VoiceToText()
    audio_file = "voice.mp3"  
    text = converter.convert(audio_file)
    print("Converted text:", text)
