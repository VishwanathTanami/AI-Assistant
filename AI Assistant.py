import pyttsx3
import speech_recognition as sr
import datetime
from datetime import time
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import json
from time import sleep
import subprocess
from ecapture import ecapture as ec
import pyjokes
import pyautogui
import base64
import operator
from bs4 import BeautifulSoup
import pyaudio
import winshell
import ctypes
import shutil
import win32com.client as wincl
import re
import numpy as np
import winsound






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

    extractedtime = open("Alarmtext.txt","rt")
    time = extractedtime.read()
    Time = str(time)
    extractedtime.close()

    deletetime = open("Alarmtext.txt","r+")
    deletetime.truncate(0)
    deletetime.close()




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")

    except:
        speak("say that again please..")
        return "none"
    return query

def Pass(pass_inp):
    password = "Vishwanath"
    passss = str(password)
    if passss==str(pass_inp):
         speak("access granted")
    else :
         speak("access denied")
         exit()
         
                 
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def play_on_youtube(video):
    kit.playonyt(video)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 534)
    server.ehlo()
    server.starttls()
    server.login('malladi.vishwanath2021@vitstudent.ac.in', 'MvTanmai@2003#')
    server.sendmail('malladi.vishwanath2021@vitstudent.ac.in', to, content)
    server.close()




def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=20057ada441445ceb121742a933357c1"
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's{day[1]} news is : {head[i]}")

def Wish():
    hour = int(datetime.datetime.now().hour)
    
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour >= 0 and hour <12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    
    speak("I am AI Assistant sir . Please tell me how may i help you ?")


if __name__ == "__main__":


    speak("AI Assistant is procted with password")
    speak("please give the voice command to access")
    passssssss = takeCommand()
    Pass(passssssss)


                
Wish()
    
while True:
        
        if 1:
           query = takeCommand().lower()
        

        if  "open notepad" in query:
                    
                    speak("Opening Notepad Application sir...")
                    os.startfile('C:\\Windows\\System32\\notepad.exe')    

                    while True:

                        notepadQuery = takeCommand().lower()
                        if "paste" in notepadQuery:
                            pyautogui.hotkey('ctrl','v')
                            speak("Done Sir!")

                        elif "save this file" in notepadQuery:
                            pyautogui.hotkey('ctrl','s')
                            speak("Sir, Please Specify a name for this file")
                            notepadSavingQuery=takeCommand().lower()
                            pyautogui.write(notepadSavingQuery)
                            pyautogui.press('enter')

                        elif 'note' in notepadQuery:
                            speak("Please Tell me what should I Write...")
                            while True:
                                writeInNotepad=takeCommand()
                                if writeInNotepad == 'exit typing':
                                    speak("Done Sir.")
                                    break
                                else:
                                    pyautogui.write(writeInNotepad)

                                
                        elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                            speak('quiting Notepad Sir...')
                            pyautogui.hotkey('ctrl', 'w')
                        break
        
        

        elif "open command prompt" in query :
            os.system("start cmd")


        
        elif "open webcam"  in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        
        elif  "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        
        elif "wikipedia" in query:
            speak("searching wikipedia..")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query , sentences =100)
        
            speak(results)
            # print(results)

                      
        
        elif 'open youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            play_on_youtube(video)


        elif"who invented you" in query:
            speak("i am invented by vishwanath")


        elif "who is vishwanath" in query:
            speak("vishwanath was the founder of AI Assistant and he is from hyderabad(Telangana). At present he is pursuing his UG at VIT(Vellore).")


        elif "Hi" in query or "Hey" in query:
            speak("Hello sir")


        elif "How are you" in query:
            speak("I am fine sir. what about you? ")
            speak("How was the day sir?")


        elif "That's great" in query or "Not well" in query:
            
            speak("Nice to hear sir.")
            
          
        elif "open google" in query:
            speak("what should i search on google sir !")
            search = takeCommand().lower()
            webbrowser.open(search)


        elif "where is" in query:
            query=query.replace("where is","")
            location=query
            speak("User asked to locate"+location)
            webbrowser.open_new_tab("https://www.google.nl/maps/place/"+location + " ")


        elif "send message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        
        

        elif 'close the window'in query:
                speak("closing the window")
                pyautogui.hotkey('alt','f4')
                

            

        elif 'minimise the windows 'in query or'minimise the window'in query :
                speak("minimize the window")
                pyautogui.hotkey('Win','d')

        elif 'maximize the windows'in query or'maximize the window'in query :
                speak("maximizeing windows")
                pyautogui.hotkey('Win', 'd')


        elif 'new tab'in query:
                pyautogui.hotkey('ctrl','t')


        elif 'new file'in query:
                pyautogui.hotkey('ctrl','n')


        elif 'switch the windows'in query  or 'switch the tab'in query:
                pyautogui.hotkey('ctrl','shift','tab')


        elif 'volume up' in query:
                speak('volume up sir')
                pyautogui.hotkey('volumeup')

        
        elif 'volume down' in query:
                speak('volume down sir')
                pyautogui.hotkey('volumedown')
        
        
        elif 'up'in query:
                pyautogui.press('up')

                
        elif 'down' in query:
                pyautogui.press('down')

                
        elif 'left' in query:
                pyautogui.press('left')

                
        elif 'right' in query:
                pyautogui.press('right')

                
        elif 'enter'in query:
                pyautogui.press('enter')
                
    
        elif "what is today weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        
        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.png")
            speak("Done sir")

        

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly")
            name = input("Enter the username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            pass



        elif "send email" in query:
                try:
                       
                       speak("what should is say sir?")
                       content = takeCommand()
                       to = 'm.vishwanathtanmai@gmail.com'
                       sendEmail(to,content)
                       speak("email sent successfully")
                except Exception as e :
                     speak("unable to send email")
             
                       
        elif "screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("Please sir hold the scree for few seconds , i am taking screenshot")
            
            img = pyautogui.screenshot()
            img = cv2.cvtColor(np.array(img),
                     cv2.COLOR_RGB2BGR)
   

            cv2.imwrite("image1.png", img)
            speak("i am done sir , the screenshot is saved in the folder")




        elif "hide all files" in query or "hide this folder" in query or "visible to everyone" in query:
            speak("sir please tell me you want to hide this folder or make it to visible to everyone.")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("all this files in foler are hidden sir ")

            elif "visible" in condition:
                os.system("attrib -h /s /s")
                speak("sir , all the files in folder are visible")

            
            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")


        elif "exit" in query:
            speak("Thanks for using me sir , have a great day.")
            sys.exit()

        
        elif 'what is present time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")



        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif "open window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "what is today news" in query :
            speak("please wait sir , fetching you latest news")
            news()
        
       

        elif "remember that" in query:
            speak("What should I remember sir?")
            memory=takeCommand().lower()
            speak("You asked me to remember"+memory)
            remember=open("memory.txt","w")
            remember.write(memory)
            remember.close()


        elif "did you remember" in query:

            file=open("memory.txt","r")
            speak("You asked me to remember that "+file.read())



        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            file.write(note)
            speak("note has been written sir")
            

         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))



        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        
        elif 'lock the window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                


        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

             
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

 


            

            

        
        
    

        

        
        














