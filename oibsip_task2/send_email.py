# from selenium import webdriver
# import pyttsx3 as p
import speech_recognition as sr
# import time
import yagmail

r = sr.Recognizer()

with sr.Microphone() as source:
    print("clearing background noise...")
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)

        print('Your message:{}'.format(text))

    except Exception as e:
        print(f"An error occurred: {e}")

#add automation to send emails
receiver = 'euniceadewusic@gmail.com'
message = text
sender = yagmail.SMTP('climiradiroberts@gmail.com')
sender.send(to=receiver, subject="This is an automated mail from Asiri", contents=message)
