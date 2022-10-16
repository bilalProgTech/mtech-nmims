import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import json

num = 1

import io
import random
import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import tensorflow
import pickle

warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)

nltk.download('punkt')
nltk.download('wordnet')


model = tensorflow.keras.models.load_model('chat_model')

# load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# parameters
max_len = 20

with open('starwarsintents.json') as file:
    data = json.load(file)

# Keyword Matching
GREETING_INPUTS = ("hello","hello, chatty", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response = ''
    result = model.predict(tensorflow.keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_response]),
                                                                      truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            return google_speaks(np.random.choice(i['responses']))


def google_speaks(output):
    global num
    num += 1
    print("JediBot : ", output)

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
google_speaks("Good day! My name is JediBot. I will answer your queries about StarWars.")
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