# Unsupervised Learning on Hindi Speech Audio Files

## What is Unsupervised Learning ?
- Unsupervised learning is a type of algorithm that learns patterns from untagged data. The hope is that through mimicry, which is an important mode of learning in people, the machine is forced to build a compact internal representation of its world and then generate imaginative content from it.
- Here the task of the machine is to group unsorted information according to similarities, patterns, and differences without any prior training of data. 
- Since the audio files can be of varying lengths our job is to first find out the min number of features that explain a reasonable amount of variability in the data.
- Followed by this we can then proceed with our unsupervised modelling to find the groups using the naturally occurring patterns.

![This is an image](https://fullcircle-cms.com/fullcircle/storage/uploads/2019/07/03/5d1ca1b9199dbClustering-GIF-2.gif)

## Data Used
- Hindi Speech Classification: https://www.kaggle.com/datasets/vivmankar/hindi-speech-classification

To view the visualizations please visit the kaggle notebook: https://www.kaggle.com/code/quadeer15sh/unsupervised-learning-on-hindi-speech-audio-files

Python libraries required

```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install librosa
pip install scikit-learn
pip install plotly
```
