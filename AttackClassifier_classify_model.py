#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

AttackClassifier_classify_model.py

AttackClassifier_classify_model -c <data_to_classify>

The purpose of this script is to classify network connections
##  into potentially bad or good based on the type of attack or normal

"""


import sys, getopt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time 
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics     import classification_report, confusion_matrix

from sklearn.ensemble import RandomForestClassifier

#train_file_name = 'train_df.pkl'
#train_file_name = 'model_1'
#test_file_name = 'test'
#model_file_name = train_file_name + '_model.sav'
model_file_name = 'train_df.pkl_model.sav'

DOS = ['back.','land.','neptune.','pod.','smurf.','teardrop.']
R2L = ['ftp_write.','guess_passwd.','imap.','multihop.','phf.','spy.','warezclient.','warezmaster.']
U2R = ['buffer_overflow.', 'loadmodule.','perl.','rootkit.']
probing = ['ipsweep.','nmap.','portsweep.','satan.']
normal = 'normal.'
cat_feats = ['protocol_type','flag','service' ]

pd.set_option('display.max_columns',None)

def get_group(x):
# assign attack types for target variable

    if x in R2L:
        return 4
    elif x in U2R:
        return 3
    elif x in DOS:
        return 2
    elif x in probing:
        return 1
    elif x == normal:
        return 0
    else: return 10


def train_classifier(data_t):
    print('in train function: ',data_t)


def classify(data_c):
# classify network connection based on input file using
# model name listed in vars at the top of the file

#    print('in classify')
    

    #read in data to classify
    test_df = pd.read_csv(data_c, names=['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 
                                           'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 
                                           'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
                                           'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 
                                           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 
                                           'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 
                                           'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 
                                           'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 
                                           'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 
                                           'dst_host_srv_rerror_rate','category'])
#   test_df.shape
#   test_df.head()
    
    # create target variable and assign to data
    test_df['attack_type'] = test_df['category'].apply(get_group)
    
    #encode non numerical data    
    test_df_encoded = pd.get_dummies(test_df,columns=cat_feats,drop_first=True)
    
#test_df_encoded.shape 

    test_df_final = pd.DataFrame(test_df_encoded, columns=['duration', 'src_bytes', 'dst_bytes', 'logged_in', 'count', 'srv_count',
                                                           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
                                                           'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                                                           'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                                                           'dst_host_srv_diff_host_rate', 'dst_host_srv_serror_rate',
                                                           'protocol_type_tcp', 'protocol_type_udp', 'flag_SF', 'service_ecr_i',
                                                           'service_http','attack_type'])
    #set up test data
    X = test_df_final.drop(['attack_type'],axis=1)
    y = test_df_final['attack_type']
    
#    X.shape
#    y.shape

    # load model 
    i_file = open(model_file_name,'rb')
    loaded_model = pickle.load(i_file)
    i_file.close()
    
    # run the prediction and display model performance metrics
    loaded_model_pred_test = loaded_model.predict(X)
    cm = confusion_matrix(y,loaded_model_pred_test)
    #print(cm)
    print(confusion_matrix(y,loaded_model_pred_test,))
    print(classification_report(y, loaded_model_pred_test))

def main(argv):
    
    data_file = ''
    
    try:
        opts, args = getopt.getopt(argv,"hc:",["cclassify"])
    except getopt.GetoptError:
        print('AttackClassifier_classify_model.py -c <datafile>')
        sys.exit(2)
   
    for opt, arg in opts:
        if opt == '-h':
            print('AttackClassifier_classify_model.py -c <datafile>')
            sys.exit()
            
        elif opt in ('-c', '--classify'):
            data_file = arg
            classify(data_file)
    

if __name__ == "__main__":
    main(sys.argv[1:])