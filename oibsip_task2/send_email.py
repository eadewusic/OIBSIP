import speech_recognition as sr
import yagmail

def send_email():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("clearing background noise...")
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('Your message:', text)

            # Confirmation prompt for sending email
            confirmation = input("Do you want to send this email? (y/n): ")
            if confirmation.lower() == 'y':
                receiver = 'euniceadewusic@gmail.com'
                message = text
                sender = yagmail.SMTP('climiradiroberts@gmail.com', 'your_app_password')  # To whomever forks this: Replace with your Gmail account password
                sender.send(to=receiver, subject="Automated mail from Asiri", contents=message)
                print("Email sent successfully!")
            else:
                print("Email cancelled.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    send_email()  # Call the send_email function