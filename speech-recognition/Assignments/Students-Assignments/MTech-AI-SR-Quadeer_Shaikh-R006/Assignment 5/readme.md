# Recognition of Urdu Words using Machine Learning

## Recognition of Urdu Words
**Speech recognition**, in general also known as automatic speech recognition (ASR), computer speech recognition, or speech-to-text, is a capability which enables a program to process human speech into a written format.

- Recognition of speech in languages native to some country can be a challenging task due to the different accents, dialects and pronunciations.
- This problem accounts for acoustic modelling that can take audio speech signals as input and model its text output based on some feature extraction method that captures the variations in the way a word can be spoken.
- In this kernel I have used MFCC features of audio inputs to build simple models that can classify the 1 second long audio files (in Urdu) into their respective texts.

## Feature Extraction
MFCC features of the audios are extracted

![This is an image](https://miro.medium.com/max/1400/1*ObZV1Ay9CTH4YJPySIPpWA.png)

## Inference on Custom Input Audios
- My custom input sequence is Subah, Dopahar, Mangal, Budh
- A window is slided over the audio signal so that we convert the audio within each window into MFCC features and then predict the label to recognize the word
- Window size is determined on the basis of sampling rate, length of the audio and average time length of each word

![This is an image](https://global-uploads.webflow.com/5fac161927bf86485ba43fd0/6229d40f625c70840c12bcd7_BlogGif_2.gif)

## Python Libraries Required
```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install librosa
pip install scikit-learn
pip install tensorflow
pip install joblib
```
