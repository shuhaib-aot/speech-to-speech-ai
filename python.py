import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is", Time)

def date() -> None:
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")

def wishme() -> None:
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See you tomorrow.")
    speak("Jarvis at your service sir, please tell me how may I help you.")
    print("Jarvis at your service sir, please tell me how may I help you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(img_path)

def takecommand() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return "Try Again"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "Try Again"
    except Exception as e:
        print(e)
        speak("Please say that again.")
        return "Try Again"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. Kishan, and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Kishan, and I'm a desktop voice assistant.")
        elif "how are you" in query:
            speak("I'm fine sir, what about you?")
            print("I'm fine sir, what about you?")
        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!")
            print("Glad to hear that sir!")
        elif "wikipedia" in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else.")
        elif "open youtube" in query:
            wb.open("https://youtube.com")
        elif "open google" in query:
            wb.open("https://google.com")
        elif "open stack overflow" in query:
            wb.open("https://stackoverflow.com")
        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(song_dir, song))
            else:
                speak("No music files found in the Music folder.")
        elif "open chrome" in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                search = takecommand()
                wb.get(chrome_path).open_new_tab(f"https://www.google.com/search?q={search}")
                print(search)
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            speak("You told me to remember that " + data)
            print("You told me to remember that " + data)
            with open("data.txt", "w") as remember_file:
                remember_file.write(data)
        elif "do you remember anything" in query:
            try:
                with open("data.txt", "r") as remember_file:
                    remembered_data = remember_file.read()
                    speak("You told me to remember that " + remembered_data)
                    print("You told me to remember that " + remembered_data)
            except FileNotFoundError:
                speak("I don't have anything to remember.")
        elif "screenshot" in query:
            screenshot()
            speak("I've taken a screenshot, please check it.")
        elif "offline" in query:
            speak("Going offline. Goodbye!")
            quit()
