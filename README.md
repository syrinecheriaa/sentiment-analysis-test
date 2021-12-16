# Sentiment Analysis Test

## The project
This repository contains all the work that I have done in order to propose a solution to the sentiment analysis task proposed by Synthesio. It contains:
1. A data analysis notebook in which I apply made analysis on the train dataset.
2. A training notebook that can be run on google colaboatory or on local machine containing the training process of the different model that I tested. I also present in this notebook the result of the different models and choose the best one. 
3. An evaluation notebook in which I dig into the results returned by the best trained model
4. A source code of a python library that can be build and used to detect sentiments in text. 
https://drive.google.com/file/d/12TIoICzmKOXzmKb-50ZDd4-NtCxLDPCu/view?usp=sharing
5. An 'output.csv' file if the Data directory containing the result of the best model applied to the test dataset.

## Requirement 
* If you choose to run the notebooks on google colaboratory, you can just run the cells containing commands for extra-libraries installation
* If you run the notebooks on local machine, you can find all the required libraries in the 'requirement.txt' TODO
* If you want to use the library please check the part library building  
*
## Models' training 

I fine-tune three language models on the available train dataset. 
* xlm-r
* deberta
* xlm-r pre-trained and fine-tuned on tweets dataset

I evaluate the previous models on a validation dataset along with a xlm-r pre-trained and fine-tuned on tweets dataset model without fine-tuning. 
I choose the best model based one based on classification metrics. I restart the fine-tuning of this model on the whole dataset available (train+validation) in order to obtain the final model.

## Inference
In order to use the final model, you can either build the library and used it or follow the instruction in the Inference part of the Train notebook.


# Build the library 
Once the repository is cloned, you have to download the model weights and save them in the folder sentiment_analysis/sentiment_analysis/data.<br /> 
You can download the model's weights using this url https://drive.google.com/file/d/12TIoICzmKOXzmKb-50ZDd4-NtCxLDPCu/view?usp=sharing  <br />

You can build the library by running the "build.sh" file in a terminal.
```
sh build.sh
```
# Use the library 
In order to use the classifier provided by the library, the input have to be in one of the next three formats: 
* a csv file that have all the texts in the first column
* a string containg the text 
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


*   In this work, I chose to deal with the problem a classification task but one can investigate using regression models with thresholds to determine the sentiment in the text.

*   As in the evaluation notebook, there are some annotation typos in the data. We can use semi-supervised mehtod when we only look into the examples where the model has difficulty deciding whcih category to attribute to the example (for example when the maximum probability is less than 0.8)

* We show that Deberta model showed promessing results compared to xlm-r. If enough ressources are available, one can continue the pre-training of deberta by using the tweets dataset.

* In this work, no hyperparameters optimization was done in this work. One can use some time in order to fine tune those paramaters such as optimizers' parameters.
