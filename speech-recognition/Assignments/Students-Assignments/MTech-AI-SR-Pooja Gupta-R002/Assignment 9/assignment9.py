import speech_recognition as sr  
import playsound
from gtts import gTTS
import os
from transformers import pipeline

qa_model = pipeline("question-answering")

context = "Tourism is one of the world’s fastest-growing industries and a major foreign exchange and employment generation for many countries. It is one of the most remarkable economic and social phenomena.\
The word ‘tour’ is derived from the Latin word tornus, meaning ‘a tool for making a circle.’ Tourism may be defined as the movement of people from their usual place of residence to another place ( with the intention to return) for a minimum period of twenty-four hours to a maximum of six months for the sole purpose of leisure and pleasure.\
According to WTO (1993), ” Tourism encompasses the activities of persons traveling and staying in places outside their usual environment for not more than one consecutive year for leisure, business, and other purposes.”\
The Rome conference on tourism in 1963 defined tourism as ‘ a visit to a country other than one’s own or where one usually resides and works. This definition, however, did not take into account domestic tourism, which has become a vital money-spinner and job generator for the hospitality industry.\
The UNWTO defines tourists as ‘ people who travel to and stay in place outside their usual environment for not more than one consecutive year for leisure, business and other purposes not related to the exercise of an activity remunerated from within the place visited.\
According to the Tourism Society of Britain,” tourism is the temporary short-period movement of people to destination outside the places where they usually live, work; and activities during their stay at these destinations.” This definition includes the movement of people for all purposes.\
The development of technology and transportation infrastructure, such as jumbos jets, low-cost airlines, and more accessible airports, have made tourism affordable and convenient. There have been changes in lifestyle – for example, now retiree-age people sustain tourism around the year. The sale of tourism products on the internet, besides the aggressive marketing of the tour operators and travel agencies, has also contributed to the growth of tourism.\
27 September is celebrated as world tourism every year. This date was chosen as on that day in 1970, the Statutes of UNWTO were adopted. The purpose of this day is to raise awareness of the role of tourism within the international community.\
Tourism has two types and many forms based on the purpose of visit and alternative forms of tourism. Tourism can be categorized as international and domestic tourism.\
International Tourism is When people visit a foreign country, it is referred to as International Tourism. To travel to a foreign country, one needs a valid passport, visa, health documents, foreign exchange, etc.\
Inbound Tourism refers to tourists of outside origin entering a particular country. Traveling outside their host/native country to another country is called inbound tourism for the country where they are traveling. For example, when a tourist of Indian origin travels to Japan, it is  Inbound tourism for Japan because foreign tourists come to Japan.\
Outbound Tourism refers to tourists traveling from the country of their origin to another country. When tourists travel to a foreign region, it is outbound tourism for their own country because they are going outside their country. For example, when a tourist from India travels to Japan, it is outbound tourism for India and Inbound tourism for Japan.\
Domestic Tourism activity of the people within their own country is known as domestic tourism. Traveling within the same country is easier because it does not require formal travel documents and tedious formalities like compulsory health checks and foreign exchange. A traveler generally does not face many language problems or currency exchange issues in domestic tourism.\
Impacts of Tourism is Tourism is a multi-dimensional activity. The scope of tourism activities is so wide and varied that it cannot be restricted to any particular field of activity. Tourism has ramifications in almost all sectors and is influenced by the performance of each of these sectors directly or indirectly. Tourism in any country can be an apt reflection of the nation’s economic and social endowment apart from its natural wealth.\
Tourism has vast potential to bring about changes in the country’s economic, environmental, societal, and cultural edifice. Tourism has two basics: the supply of facilities and the demand for participation. The twin market forces of supply and demand interact to produce tourism patterns. These patterns are associated with economic, social, cultural, environmental, and ecological impacts.\
Establishing or developing a tourism industry involves expenditure, gains, costs, and benefits. If these impacts are considered from the outset of planning, strengths and opportunities can be maximized while weaknesses and threats can be minimized.\
Each destination will be different in terms of tourism characteristics. The cost and benefits of tourism will vary in each destination and can change over time, depending on tourism and other activities in a destination’s"

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

google_speaks("Hello,i'm here to help you know about tourism")
question = get_audio()
while question!= "bye":
    answer = qa_model(question = question, context = context)
    google_speaks(answer["answer"]+'.')
    question = get_audio()
