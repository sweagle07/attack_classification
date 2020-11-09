# attack_classification
#### Exercise looking at network traffic to classify potential good and bad connections.

### The exercise is broken down into 4 major parts:

#### 1) Data exploration/summary
#### 2) Data Classification
#### 3) Model Evaluation


## **Data Exploration**
#### notebook: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_EDA_Summary.ipynb]

## **Data Classification**
I chose to use an embedded feature selection technique using Random Forest classification. I began looking at ways to eliminate or create new features 
based on getting to know the data better. However, this approach was time consuming, therefore, I switched to something more automated.
I chose to use the random forest algorithm to build model due to the power of ensemble methods and the fact it supports multiple class classification. 
However, since this data set was quite unbalanced, another method may have been more effective. This was still a good place to start in any case.   

#### notebook to train the model: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_train_valid_set.ipynb]
#### notebook to classify new data against the model: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_classify_model.ipynb]
#### .py command line version to classify data: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_classify_model.py]
#### trained model: 

xCode for the trained classifier
A command to train the classifier and a command to run your classifier on new data
A brief description of the techniques you used, along with rationale for the choices you made and the features you built (if any new features were made)

## **Model Evaluation**

#### The model performed well for three of the attack types.
#### -normal f1 score: 83%
#### -Probing f1 score: 82%
#### -DOS f1 score: 100%

There was not enough data to get a good model for the R2L and U2R attack types. Nothing could be predicted for these attack types. 
At least not when combined with the large unbalanced data sets for DOS, probing, and normal. In the notebook are the actual numbers 
on performance along with brief comments.

Given more time, I would have spent more time with feature engineering. I used a group of features recommended from the feature selector object. However, I ran out of time to look further into the true impact of each feature as well as determine if feature correlation could have helped reduce the dimensionality  further. I also would have liked to understand #### address the impact of the training and test sets coming from different probability distributions.
