import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
#import os
#import time
#from playsound import playsound
#from bs4 import BeautifulSoup

# Load and parse the HTML document
"""with open('documents.html', 'r') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
"""
# Initialize text-to-speech engine
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Uses the first available voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print('Say that again please....')
        return "None"
    return query

"""def helper(query):
    heading = soup.find('h2', text=query)
    if heading:
        speak("Problem:")
        speak(heading.text)
    
        paragraph = heading.find_next_sibling('p')
    
        if paragraph:
            speak("Solution:")
            print("Solution:")
            print(paragraph.text.strip())
        else:
            speak("Solution under progress")
            print("Solution under progress")
    else:
        speak(f"Solutions regarding '{query}' were not found in helper.")
        print(f"Solutions regarding '{query}' were not found in helper.")"""

if __name__ == "__main__":
    wishme()
    speak("This is Say Wakk. Please tell me how may I help you")
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print("According to Wikipedia:", results)
            speak("According to Wikipedia:")
            speak(results)
            speak(f"Do you want more information about '{query}'? [YES / NO]")
            
            query = takeCommand().lower()
            if 'yes' in query:
                results = wikipedia.summary(query, sentences=3)
                print("Here you go!")
                speak("Here you go!")
                print(results)
                speak(results)
                
            elif 'no' in query:
                print("Okay, as you wish!")
                speak("Okay, as you wish!")
            else:
                print("Sorry, I didn't understand that. Ending Wikipedia result.")
                speak("Sorry, I didn't understand that. Ending Wikipedia result.")



