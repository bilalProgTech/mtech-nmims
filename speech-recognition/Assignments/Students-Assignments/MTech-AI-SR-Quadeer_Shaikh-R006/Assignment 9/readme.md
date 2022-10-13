# Spoken Dialog System

A spoken dialog system (SDS) is a computer system able to converse with a human with voice. It has two essential components that do not exist in a written text dialog system: a speech recognizer and a text-to-speech module (written text dialog systems usually use other input systems provided by an OS). It can be further distinguished from command and control speech systems that can respond to requests but do not attempt to maintain continuity over time.

## Question Answering Bot
Question Answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. Some question answering models can generate answers without context. In our case the Question Answering bot is given a context of Indian tourist places, their short description and what is the best time to visit that place.

![This is an image](https://blog.cloudera.com/wp-content/uploads/2020/04/QAworkflow.png)

Python libraries required
```
pip install SpeechRecognition
pip install playsound==1.2.2
pip install gTTS
pip install transformers
pip install PyAudio
```

