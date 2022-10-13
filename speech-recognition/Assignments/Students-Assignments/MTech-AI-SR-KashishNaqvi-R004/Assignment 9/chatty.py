import speech_recognition as sr
import playsound
from gtts import gTTS
import os

num = 1

# import necessary libraries
import io
import random
import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.\
    feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages

# uncomment the following only the first time
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only


# Reading in the corpus
with open('knowledge_base1', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# TOkenisation
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello","hello, chatty", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return google_speaks(robo_response)
    else:
        robo_response = robo_response + sent_tokens[idx]
        return google_speaks(robo_response)

def google_speaks(output):
    global num
    num += 1
    print("Chatty : ", output)

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
google_speaks("Good day! My name is Chatty. I will answer your queries about Tourism in India.")
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
                sent_tokens.remove(user_response)
    else:
        flag = False
        google_speaks("Bye! take care..")

