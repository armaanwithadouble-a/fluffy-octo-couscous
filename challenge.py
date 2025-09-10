from RealtimeSTT import AudioToTextRecorder
import pyttsx3
from pygame import mixer

if __name__ == "__main__":

    print("listen listen listen listen LISTEN!!!!!!!! PLEASE WAIT UNTIL IT say 'speak now' OK THANKUUU!!!!")
    recorder = AudioToTextRecorder()

    triggerWord = input("pls enter your trigger word/letter: ").lower()

    def process_text(text):
        print(text)
        if (text.lower()).find(triggerWord) != -1:
            msg = "You said: " + text
            print(msg)
            pyttsx3.speak(msg)
            mySound = mixer.Sound('audio.wav')
            mySound.set_volume(9999999999)
            mySound.play()

    mixer.init()

    while True:
        recorder.text(process_text)