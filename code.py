import pyautogui # pip install pyautogui
import os # preinstalled
import pyttsx3 # pip install pyttsx3
import datetime # preinstalled
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib # preinstalled
import pyjokes # pip install pyjokes
import psutil # pip install psutil
import webbrowser as wb
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 180
engine.setProperty('rate', newVoiceRate)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

my_email = "test@test.com"
my_passwd = "testpasswd"
r_email = "test2@test.com"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon")
    elif hour >=17 and hour <= 24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    except sr.UnknownValueError:    # if the value is unknown then this will be called
            speak('Sorry, I did not get that')
    except sr.RequestError:    # if for some reason the program is unable to record audio then this will be called
            speak('Sorry, my speech service is down')

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(my_email,my_passwd)
    server.sendmail(my_email, to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    i = 0
    file = "D:\ss\ss_",i,".png"
    img.save(file)
    i += 1

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    #battery = psutil.sensor_battery
    #speak("Battery is at")
    #speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)
        elif "search in google" in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = 'https://google.com/search?q=' + search
            wb.get().open(url)
        elif "search in yahoo" in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = 'https://in.search.yahoo.com/search?p=' + search
            wb.get().open(url)
        elif "search in duckduckgo" in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = 'https://duckduckgo.com/?q=' + search
            wb.get().open(url)
        elif 'find location' in query:
            speak('What place do you want to find?')
            location = takeCommand().lower
            url = 'https://google.nl/maps/place/' + location + '/&amp;'    # this saves the url link
            wb.get().open(url)    # this opens the link in the default web browser
            speak('Here is the location of '+ location)
        elif "make directory" in query:
            username = getpass.getuser()
            speak("What should be the name of the folder?")
            name = takeCommand().lower()
            name = name.replace(" ","_")
            command = 'mkdir c:\\Users\\'+username+'\\Desktop\\'+name
            os.system(command)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = r_email
                sendmail(to, content)
                speak("The mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the email")
        elif "search in chrome" in query:
            speak("What should I search?")
            search = takeCommand().lower()
            wb.get(chrome_path).open(search + ".com")        
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play song" in query:
            songs_dir = "D:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            speak("That's all from my side enjoy the music.")
            quit()
        elif "remember that" in query:
            speak("What should I Remember?")
            data = takeCommand()
            speak("you said me to remember "+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that "+ remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        else:
            speak("Sorry I cannot do what you said. Maybe I could do that in future")