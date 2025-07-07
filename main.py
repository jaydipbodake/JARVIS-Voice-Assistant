import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import mtranslate
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice',voices)
engine.setProperty('rate',130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content=" "
    while content==" ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content=r.recognize_google(audio,language='en-in')
            print("You said... "+content)
        except Exception as e:
            print("Please try again....")

        return content

def main_process():
    while True:
        request=command().lower()
        if "hello" in request:
            speak("Wellcome, How can i help you.!")
        elif "play music" in request:
            speak("Playing music")
            song=random.randint(1,3)
            if song==1:
                webbrowser.open("https://www.youtube.com/watch?v=yJg-Y5byMMw")
            elif song==2:
                webbrowser.open("https://www.youtube.com/watch?v=L-VMCv4Y9l8")
            elif song==3:
                webbrowser.open("https://www.youtube.com/watch?v=19Iuib716m0")
        elif "current time" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+str(now_time))
        elif "current date" in request:
            now_date=datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+str(now_date))
        elif "new task" in request:
            task=request.replace("new task","")
            task=task.strip()
            if task!="":
                speak("Adding task : "+task)
                with open("todo.txt","a") as file:
                    file.write(task+"\n")
        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("you are work : "+file.read())
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks=file.read()
            notification.notify(
                title="today,s work",
                message=tasks
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query=request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)   
            pyautogui.sleep(1)
            pyautogui.press("enter")
        elif "screenshot" in request:
            im1 = pyautogui.screenshot()
            im1.save('my_screenshot.png')
            speak("screenshot ghetlaaa  ")
        elif "wikipedia" in request:
            request=request.replace("jarvis ","")
            request=request.replace("search wikipedia ","")
            try:
                speak(f"Searching Wikipedia for {request}")
                result = wikipedia.summary(request, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't find any information on Wikipedia for that.")
        elif "search google" in request:
            request=request.replace("jarvis ", "")
            request=request.replace("search google ", "")
            pwk.search(request)
        elif "send whatsapp" in request:
            speak("Sending WhatsApp message now")
            pwk.sendwhatmsg_instantly(
            phone_no="+919767308113",
            message="Hi, I am JARVIS",
            wait_time=10,   
            tab_close=True, 
            close_time=5    
            )
        elif "shutdown" in request:
            os.system("shutdown /s /t 5")
            speak("Shutting down in 5 seconds.")
                   
speak("Hello, I am JARVIS")
main_process()
