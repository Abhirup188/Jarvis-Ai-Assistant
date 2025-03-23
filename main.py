import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import wikipedia
import musicLibrary
import requests
import json
import client

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty(voices,id)

def greeting():
    current_hour = datetime.datetime.now().hour
    if 0<=current_hour<12:
        speak("Good Morning")
    elif 12<=current_hour<16:
        speak("Good Afternoon")
    elif 16<=current_hour<=18:
        speak("Good Evening")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio_text,language='en-in')
            r.pause_threshold = 1
            print(f"You Said:{query}")

        except Exception as e:
            print("Say That Again Please...")
            speak("Say That Again Please...")

    return query

if __name__ == "__main__":
    greeting()
    print("Jarvis Is Inactive Say \"Hello Jarvis\" to Activate Jarvis...")
    speak("Jarvis Is Inactive. Say Hello Jarvis to Activate Jarvis...")

    while True:
        text = takeCommand().lower()
        if 'hello jarvis' in text:
            speak("Hello Sir I Am Jarvis. How can i help you")
        if 'open google' in text:
            speak("opening google")
            webbrowser.open("www.google.com")
            text = ""
        if 'open youtube' in text:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
        
        if 'open ocean of games' in text:
            speak("opening ocean of games")
            webbrowser.open("www.oceanofgames.com")
            text = ""

        if 'wikipedia' in text:
            speak("Searching Wikipedia...")
            result = wikipedia.summary(text,sentences = 2)
            speak("According To Wikipedia...")
            print(result)
            speak(result)
            text = ""
        
        if "shutdown" in text:
            speak("Bye Sir. Have A Nice Day")
            print("Shutting Down Jarvis...")
            exit()
            text = ""


        if text.startswith("play"):
            text = text.replace("play"," ")
            song = text.strip()
            speak(f"Playing song {song}...")
            
            url = musicLibrary.music[song]
            webbrowser.open(url)
            text = ""

        if 'what is the temperature' in text:
            check = text.split(" ")
            
            if len(check)==6:
                city = text.split(" ")[5]
                speak("Wait A Minute Sir")
                url = f"https://api.weatherapi.com/v1/current.json?key=6e458967cb7a4fec86583607242712&q={city}"
                r = requests.get(url)
                dic = json.loads(r.text)
                print({dic["current"]["temp_c"]})
                speak(f"{dic["current"]["temp_c"]} degree celcius")

            elif len(check)>6:
                text = text.replace("what is the temperature"," ")
                city = text.strip()
                speak("Wait A Minute Sir")
                url = f"https://api.weatherapi.com/v1/current.json?key=6e458967cb7a4fec86583607242712&q={city}"
                r = requests.get(url)
                dic = json.loads(r.text)
                print({dic["current"]["temp_c"]})
                speak(f"{dic["current"]["temp_c"]} degree celcius")
        if 'what do you see in the image' in text:
            image_path = "images/butter_chicken.jpg"  # Or wherever your cabbage image is located
            prompt = "What is in this image?"
            ianswer = client.ask_gemini_with_image(prompt=text,image_path=image_path)
            print(ianswer)
            speak(ianswer)
            text = ""

        
        else:
            answer = client.ask_gemini(text)
            print(answer)
            speak(answer)
            text = ""
                
    
            
                


            

        


        

                




        