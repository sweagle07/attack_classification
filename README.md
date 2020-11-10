# attack_classification
#### Exercise looking at network traffic to classify potential good and bad connections.

### The exercise is broken down into 3 major parts:

#### 1) Data exploration/summary
#### 2) Data Classification
#### 3) Model Evaluation


## **Data Exploration**
#### notebook: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_EDA_Summary.ipynb]

## **Data Classification**
I chose to use an embedded feature selection technique using Random Forest classification. I began looking at ways to eliminate and/or create new features 
based on getting to know the data better. However, this approach was time consuming, therefore; I switched to a more automated approach.

I chose to use the random forest algorithm to build the model due to the power of ensemble methods and the fact it supports multiple class classification. 
However, since this data set was quite unbalanced, another method may have been more effective. This was still a good place to start in any case.   

#### train the model notebook: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_train_valid_set.ipynb]
#### classify data with the model notebook: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_classify_model.ipynb]
#### .py command line version to classify data: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_classify_model.py]
#### trained model: [https://github.com/sweagle07/attack_classification/blob/main/train_df.pkl_model.sav] 

## **Model Evaluation**

#### The model performed well for three of the attack types.
#### -normal f1 score: 83%
#### -Probing f1 score: 82%
#### -DOS f1 score: 100%

There was not enough data to get a good model for the R2L and U2R attack types. Nothing could be predicted for these attack types. At least not when combined with the large data sets for DOS, probing, and normal. I also have additional comments and on performance within the classification notebook: [https://github.com/sweagle07/attack_classification/blob/main/AttackClassifier_classify_model.ipynb].

Given more time, I would have spent more time with the feature engineering process. I used a group of features recommended from the feature selector object. However, I ran out of time to look further into the true impact of each feature as well as determine if feature correlation could have helped reduce the dimensionality further. 

I also would have liked to understand and address the impact of the training and test sets coming from different probability distributions.
