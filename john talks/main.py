import speech_recognition as sr
import os

# Initialize recognizer
r = sr.Recognizer()

def instructions():
    os.system("cls")
    print("[*] 'close' - shutdown the PC\n[*] 'hibernate' - hibernate the PC\n[*] 'lock' - locks the PC\n[*] 'adios' - closes JohnTalks\n[*] 'help' - prints the help menu\n")
    
def listen_for_trigger():
    print("[*] Welcome to JohnTalks | v.3 | This version supports only windows platform\n[*] To interact with the program make sure that your microphone is unmuted and ready to listen. Say 'help' for instructions.")
    while True:
        with sr.Microphone() as source:
            print("[+] Listening for trigger phrase...")
            audio = r.listen(source, phrase_time_limit=2.5)  # listening timeframe = 2.5 sec
            
            try:
                text = r.recognize_google(audio).lower()
                print("[*] You said:", text)
                if "close" in text:
                    print("[*] Turning off PC...")
                    os.system("shutdown /s /t 1")
                    break 
                elif "hibernate" in text:
                    print("[*] Hibernating PC...")
                    os.system("shutdown /h")
                elif "lock" in text:
                    print("[*] Locking PC...")
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                elif "adios" in text:
                    break
                elif "help" in text:
                    instructions()
            except sr.UnknownValueError:
                print("[*] Could not understand audio")
            except sr.RequestError as e:
                print("[*] Could not request results; {0}".format(e))

listen_for_trigger()