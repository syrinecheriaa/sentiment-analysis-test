# Sentiment Analysis Test

## The project
This repository contains all the work that I have done in order to propose a solution to the sentiment analysis task proposed by Synthesio. It is composed of:
1. A data analysis notebook in which I analyse the train dataset.
2. A training notebook (that can be run on google colaboatory or on local machine) containing the training process of the different models that I tested. I also present in this notebook the results of the different models and choose the best one. 
3. An evaluation notebook in which I dig into the results returned by the best obtained model
4. A source code of a python library that can be built and used to detect sentiments in text (can be found in the "sentiment_analysis" folder)
5. An output file 'predictions.csv' contained in the Data directory with the results of the best model on the test dataset.

## Requirement 
* If you choose to run the notebooks on google colaboratory, you can just run the cells containing commands for libraries installation
* If you run the notebooks on local machine, you can find all the required libraries in the file 'requirement.txt'
* If you want to use the library please check the part **Build the library**
 
## Models' training 

I fine-tuned three language models on the available train dataset:
* xlm-r
* deberta
* xlm-r pre-trained and fine-tuned on tweets dataset

I evaluate the previous models on a validation dataset along with a an xlm-r model pre-trained and fine-tuned on tweets dataset without fine-tuning it. 
I choose the best model based on classification metrics. I restart the fine-tuning of this model on the whole dataset available (train+validation) in order to obtain the final model.

## Inference
In order to use the final model, you can either build the library or use the Inference.ipynb notebook.


## Build the library 
The library is developed in python3.7<br />
It is recommended to create a new environment before building the library. <br />
Steps to build the library:
1. Clone the repository
2. Download the model weights and save them in the folder sentiment_analysis/sentiment_analysis/data.<br /> 
You can download the model's weights using this url https://drive.google.com/file/d/12TIoICzmKOXzmKb-50ZDd4-NtCxLDPCu/view?usp=sharing  <br />
3. Build the library by running the "build.sh" file in a terminal.
```
sh build.sh
```
## Use the library 
In order to use the library, you have to provide an input in one of the next three formats: 
* a csv file that have all the texts in the first column
* a string containing the text 
* a list of texts

```
from sentiment_analysis import classifier
clf = classifier.Classifier()
# clf.predict("test.csv") where test.csv is a file conraining the texts in which we want to detect the sentiments
clf.predict('I loved the look of this neck lace.  I was very surprised that pearls of this quality could be purchased at this price')
# output: ['positive']
clf.predict(['I loved the look of this neck lace.  I was very surprised that pearls of this quality could be purchased at this price',
             'Makes me mad'])
# output: ['positive', 'negative']
```



## Next steps:


*   In this work, I chose to deal with the problem as a classification task, but one can investigate regression models with thresholds to determine the sentiment in the text.

*   As mentioned in the evaluation notebook, there are some annotation erros in the data. We can use semi-supervised methods to correct those mistakes by only looking into the examples where the model has difficulty deciding which category to attribute (for example when the maximum probability is less than 0.8)

* We show that Deberta model has promising  results compared to xlm-r. If enough resources are available, one can continue the pre-training of deberta on the tweets dataset.

* In this work, no hyperparameters optimization was done. One can use some time in order to fine tune some parameters such as the optimizers' parameters.
