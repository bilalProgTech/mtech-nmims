import speech_recognition as sr  
import playsound
from gtts import gTTS
import os
import time
from transformers import AutoModelForQuestionAnswering, pipeline, AutoTokenizer

model_checkpoint = 'deepset/minilm-uncased-squad2'
model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
context = "Manali, Andaman and Ladakh are some of the popular tourist places in India. \
           Manali is one of the most popular hill stations in Himachal, Manali offers the most magnificent views of \
           the Pir Panjal and the Dhauladhar ranges covered with snow for most parts of the year.\
           Ladakh is a union territory in the Kashmir region of India. \
           Andaman Islands is a little slice of paradise tucked around 1,400 km away from the east coast of mainland India.\
           Best time to visit Manali is from October to June. Best time to visit Ladakh is from June to September. Best time to visit Anadaman is from October to June."
num = 1

def google_speaks(output):
    global num
    num += 1
    print("Text : ", output)
  
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    file = 'Audio-'+str(num)+'.mp3'  
    toSpeak.save(file)
    playsound.playsound(file, True)  
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

# time.sleep(5)
while True:
    google_speaks("Greetings! What's your question?")
    time.sleep(0.5)
    question = get_audio()
    pipe = pipeline("question-answering",model=model,tokenizer=tokenizer)
    result = pipe(question=question, context=context, top_k=1)
    if 'thank you' in result:
        break
    time.sleep(0.5)
    google_speaks(result['answer'] + '.')