# Sentiment Analysis Test

## The project
This repository contains all the work that I have done in order to propose a solution to the sentiment analysis task proposed by Synthesio. It contains:
1. A data analysis notebook in which I apply made analysis on the train dataset.
2. A training notebook that can be run on google colaboatory or on local machine containing the training process of the different model that I tested. I also present in this notebook the result of the different models and choose the best one. 
3. An evaluation notebook in which I dig into the results returned by the best trained model
4. TODO: code source of a python library that can be used in inference


## Requirement 
* If you choose to run the notebooks on google colaboratory, you can juste run the cells containing commands for extra-libraries installation
* If you run the notebooks on local machine, 
* If you want to use the library please check the part library building # todo 
*
## Models' training 

I fine-tune three language models on the available train dataset. 
* xlm-r
* deberta
* xlm-r pre-trained and fine-tuned on tweets dataset

I evaluate the previous models on a validation dataset along with a xlm-r pre-trained and fine-tuned on tweets dataset model without fine-tuning. 
I choose the best model based one based on classification metrics. I restart the fine-tuning of this model on the whole dataset available (train+validation) in order to obtain the final model.

## Inference
In order to use the final model, 

