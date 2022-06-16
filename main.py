import os
import smtplib
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import pyjokes


engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('a very good morning to you')
        print('good morning')
    elif hour>=12 and hour<=18:
        speak('a very good afternoon to you')
        print('good afternoon')
    else:
        speak('good evening, how is your day')
        print('good evening')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement} \n")

        except Exception as e:
            speak("sorry, please say that again")
            return "None"
        return statement

def name():
    speak("what should i call you")
    uname = takeCommand()
    speak(uname)

def sendEmail (to, content):
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.ehlo ()
    server.starttls()
    server.login('amishasakhare04@gmail.com', 'amisha012345')
    server.sendmail('amishasakhare04@gmail.com', to, content)
    server.close()


print ('loading your AI personal assistant Alka')
speak('Hey, i am Alka. Your personal assistant')
wishMe()
name()

if __name__ == '__main__':
    while True:
        speak("what's on your mind? Tell me!")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if 'bye' in statement or 'good bye' in statement or 'stop' in statement:
            speak('Okay, Talk to you later. Bye')
            print('Okay, Talk to you later. Bye')
            print('assistant is shutting down')

            break

        if 'wikipedia' in statement:
            speak('Searching wikipedia...')
            print('Searching wikipedia...')
            statement = statement.replace('wikipedia','')
            results = wikipedia.summary(statement, sentences=5)
            speak('According to Wikipedia')
            speak(results)
            print(results)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {strTime}')
            print(f'the time is {strTime}')

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('some headlines from the Times of India')
            time.sleep(6)

        elif 'search' in statement:
            statement= statement.replace("search",'')
            webbrowser.open_new_tab(statement)
            time.sleep(6)

        elif 'who are you' in statement:
            speak('i am Alka.')
            print("I am Alka.")

        elif 'what you can do' in statement:
            speak('i can tell you time, search for you, tell you news, and many things whatever you want')
            print("I can tell you time, search for you, tell you news and many things whatever you want")

        elif 'who made you' in statement or 'who created you' in statement:
            speak('i was build by Amisha Sakhare')
            print('I was build by Amisha Sakhare')

        elif 'joke' in statement:
            speak(pyjokes.get_joke(language='en', category='all'))
            print(pyjokes.get_joke(language='en', category='all'))

        elif 'open youtube' in statement:
            speak('Opening youtube')
            print('Opening youtube...')
            webbrowser.open_new_tab('https://www.youtube.com/')

        elif 'play music' in statement or 'play song' in statement:
            speak('playing your playlist')
            print("Playing your playlist")
            music = 'H:\Songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[1]))

        elif 'send email' in statement or 'send mail' in statement:
            try:
                speak('To whom you want to send email')
                print('To whom you want to send email')
                to = takeCommand()
                speak('what should i say')
                print('What should I say?')
                content = takeCommand()
                sendEmail(to,content)
                speak('email has been sent')
                print('Email has been sent')
            except Exception as e:
                print(e)
                speak('i am not able to sent this email')
                print('I am not able to sent this email')
                speak('try it again')
                print('Try it again')

        elif 'how are you' in statement:
            speak('i am fine, Thank you')
            speak('how are you')

        elif "what's your name" in statement:
            speak("it starts with a and ends with a and is two syllable long. it's Alka")
            print("It starts with a and ends with a and is two syllable long. It's Alka")

# add more features using elif...
          
