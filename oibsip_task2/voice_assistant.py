from selenium_web import info
import pyttsx3 as p #module to convert text to speech
import speech_recognition as sr #module to convert speech to text

engine = p.init() #instance of p.init class inside the pyttsx3 module; used to initiate the pyttsx3 used to convert text to speech
rate = engine.getProperty('rate') #adjust speed of the voice, default is 200
engine.setProperty('rate', 170) #to change it to slower speed
voices = engine.getProperty('voices') #to have a look at the range of voices my OS offers
engine.setProperty('voice', voices[1].id) #to listen to the 1st of 2 voices offered
# print(voices)

# engine.say("Hello there. My name is Asiri and I am your Voice Assistant")
# engine.runAndWait() computer to wait until the sentence gets finished

#for computer to say something from the user instead of typing it out in the code
def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() #create instance of the recogniser class, which creates an instance that helps us retrive info (audio) from a source (microphone)

speak("Hello Eunice. My name is Asiri and I am your Voice Assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000 #background property that increases spectrum of a voice. If increased, will capture even low voices
    r.adjust_for_ambient_noise(source, 1.2) #background property that cancels all the noise around you and captures your voice only
    print("listening")
    audio = r.listen(source) #listens to what we say, captures it in a mic and saves the audio in the audio variable
    text = r.recognize_google(audio) #send the audio to the Google API engine which will convert it to a text
    print(text)

if "what" and "about" and "you" in text:
    speak("I am fine, thank you!")
speak("What can I do for you at the moment?") #mandatory line

#add automation - search online sites for info I say - using Selenium WebDrive to scrape data (collecting specific information from websites.)
