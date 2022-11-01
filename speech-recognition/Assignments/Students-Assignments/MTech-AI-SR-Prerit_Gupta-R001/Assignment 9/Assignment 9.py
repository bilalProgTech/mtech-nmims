import speech_recognition as sr  
import playsound
from gtts import gTTS
import os
from transformers import pipeline

qa_model = pipeline("question-answering")

context = 'Banking is defined as “Accepting of deposits of money from public for the purpose of Lending or Investment, repayable on demand or otherwise and withdrawable by cheque, draft, or otherwise” \
Banking can be defined as the business activity of accepting and safeguarding money owned by other individuals and entities, and then lending out this money in order to earn a profit. However, with the passage of time, the activities covered by banking business have widened and now various other services are also offered by banks. The banking services these days include issuance of debit and credit cards, providing safe custody of valuable items, lockers, ATM services and online transfer of funds across the country / world. \
Objective of Bank are Business objectives, Social objectives. \
Business objectives, Making profits, Providing services, Currency issue, Creation of transaction media, Receiving deposit, Making loan, Ensuring safety, Investment.\
Social objectives Creating savings, Capital formation, Industrialization, Employment, Developing living standard, Economic development.\
Features of Banking, The bank accept deposits from the public and advancing them as loans to the needy people. The deposits may be current, fixed saving etc.\
The banks are the institutions that can create credit i.e. creation of additional money for lending Thus ‘creation of credit is the unique features of banking.\
Banks make extra money by providing loans for different Product to the loan. The bank makes the extra money by lending money to the eligible person at certain rates.Nowadays, banks provide loans for various requirements such as study loan, car loan, home loan, personal loans, etc.Different banks provide different loans at different interest rates. You can compare the interest rates of different banks to get a loan at minimum interest rates\
Banks serve as a middle man from the money surplus unit to be money deficit unit. They are intermediaries, who transfer funds from savers to investors through grants for business, commerce, education, housing etc.\
The deposits are usually withdrawable on demand. it may be withdrawable by cheque, draft or otherwise.\
Bank is that modern banks are also providing internet services. The development of the internet and its inclusion in the banking sector has made it even more easy for people to carry out various transactions.\
Banks are providing online services through their apps. You can pay bills, buy food, go shopping without having cash with you. With the help of banking apps, you can pay for everything online.\
Nowadays, more and more banks are taking their business online. It helps in making safe and risks free transactions, and there are fewer chances of stealing taxes. There are specific terms for these types of transactions, such as internet banking and mobile banking.\
Since all the banking activities of Commercial banks are carried on with the aim of Making profit, it is regarded as an commercial institution .\
The bank uses our money to lend it to others or by investing it in profitable businesses to make profits. If you think your money is sitting in a banks locker, then you are wrong.\
You might have digits of the money mentioned in your passbook, but you might be rotating between one person to another to make more money to the investor.\
Bank Create a reservoir of fund from the numerous small deposits collect from customer ,and than provide large loan to Investor.\
Beside the basic function of accepting deposits and lending money as a loan ,bank ,possess the characteristics of an agent because of its various agency services . '

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
    try: 
        text = srObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
    except: 
        google_speaks("Not able to hear you properly") 
        return 0

google_speaks("Hello, How can I help you with banking.")
question = get_audio()
while question!= "bye":
    answer = qa_model(question = question, context = context)
    google_speaks(answer["answer"]+'.')
    question = get_audio()