import os

def Speak(text):
    text = text.replace('"', '')
    os.system(f'pico2wave -w=/tmp/speech.wav \"{text}\" && aplay /tmp/speech.wav && rm /tmp/speech.wav')

Speak("Hi There hlo its me")