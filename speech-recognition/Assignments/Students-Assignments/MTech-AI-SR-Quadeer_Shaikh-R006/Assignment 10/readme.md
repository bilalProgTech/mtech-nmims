# Emotion Detection Using Autoencoders

## Emotion Detection
- It is a system through which various audio speech files are classified into different emotions such as happy, sad, anger and neutral by computers. Speech emotion recognition can be used in areas such as the medical field or customer call centers.
- In this kernel the emotions will be classified into only 2 categories: happy or sad

![](https://miro.medium.com/max/1185/1*6erovyvVqpraE2VR0f3vfw.jpeg)

**Note:** Here the emotion detection is being performed on the acoustic features of the data and not the semantic understanding of the sentences spoken by a person

## Feature Extraction 
- The acoustic features of an audio can be extracted using different methods, but in this kernel only 2 methods will be used
1. MFCCs
2. Mel Spectrograms

![](https://images.deepai.org/converted-papers/2005.12779/x3.png)

## Modelling
- The following models will be used for building the models for emotion detection
1. Logistic Regression on MFCC and Mel Spec Features
2. CNNs on MFCC and Mel Spec Features
3. Autoencoders and Variational Autoencoders on whichever features are giving better performance in the above models

## Variational Autoencoders
- The essence of this repo is to use autoencoders for evaluating the reconstruction loss for audios with different emotions. A variational autoencoder captures this really well.
![](https://www.jeremyjordan.me/content/images/2018/03/Screen-Shot-2018-03-18-at-12.24.19-AM.png)

## Python Libraries Required
```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install tensorflow
pip install tqdm
pip intall glob
pip install librosa
pip instal scikit-learn
```
