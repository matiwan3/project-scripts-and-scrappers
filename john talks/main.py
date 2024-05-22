import speech_recognition as sr
import os

# Initialize recognizer
r = sr.Recognizer()

# Function to listen for trigger phrase
def listen_for_trigger():
    while True:
        with sr.Microphone() as source:
            print("Listening for trigger phrase...")
            audio = r.listen(source)
            
            try:
                # Use Google Web Speech API for speech recognition
                text = r.recognize_google(audio).lower()
                print("You said:", text)
                if "john banana" in text:
                    print("Turning off PC...")
                    os.system("shutdown /s /t 1")
                    break 
                elif "john hibernate" in text:
                    print("Hibernating PC...")
                    os.system("shutdown /h")
                    break
                elif "john lock" in text:
                    print("Locking PC...")
                    os.system("rundll32.exe user32.dll,LockWorkStation") # Program is still listening after locking down the PC, although needs some adjustments
                elif "bye john" in text:
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))


listen_for_trigger()

