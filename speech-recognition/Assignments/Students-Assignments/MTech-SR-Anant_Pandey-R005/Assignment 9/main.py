import speech_recognition as sr
import playsound
from gtts import gTTS
import json
import io
import os
import random
import numpy as np
import tensorflow
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
model = tensorflow.keras.models.load_model('intent_model')
with open('tok.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('l_e.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)
num = 1
max_len = 20
with open('Intent.json') as file:
    data = json.load(file)

GREETING_INPUTS = ("hello","hello, chatty", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
def response(user_response):
    robo_response = ''
    result = model.predict(tensorflow.keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_response]),
                                                                      truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['intent'] == tag:
            return google_speaks(np.random.choice(i['responses']))
def google_speaks(output):
    global num
    num += 1
    print("IntentBot : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = 'Audio-' + str(num) + '.mp3'
    toSpeak.save(file)
    playsound.playsound(file)
    os.remove(file)
def get_audio():
    srObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Please Speak")
        audio = srObject.listen(source, phrase_time_limit=5)
    try:
        text = srObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        google_speaks("Not able to hear you properly")
        return 0
flag = True
google_speaks("Good day! My name is IntentBot. Whats Your Intent?.")
while (flag == True):
    user_response = get_audio()
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            google_speaks("You are welcome..")
        else:
            if (greeting(user_response) != None):
                google_speaks("" + greeting(user_response))
            else:
                print(" ", end="")
                response(user_response)
    else:
        flag = False
        google_speaks("Bye! take care..")