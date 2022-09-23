import speech_recognition as sr  
import playsound
from gtts import gTTS
import os


num = 1
def google_speaks(output): 
    global num 
    num += 1
    print("Text : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    file = 'Audio-'+str(num)+'.mp3'  
    toSpeak.save(file) 
    playsound.playsound(file)
    os.remove(file) 


def get_audio(): 
    srObject = sr.Recognizer() 
    audio = '' 
    with sr.Microphone() as source: 
        print("Please Speak") 
        audio = srObject.listen(source, phrase_time_limit = 5)  
    print("Stop.")
    try: 
        text = srObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
    except: 
        google_speaks("Not able to hear you properly") 
        return 0


google_speaks("Hello, Greetings! What's your name?") 
name = get_audio() 
google_speaks("Hello, " + name + '.')