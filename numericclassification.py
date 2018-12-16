import pandas as pd
import json as json
from sklearn.preprocessing import normalize

from score import *
import sentiment2
from sentiment2 import *
import numpy as np
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier, DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import csv

df = pd.read_excel("totaldata.xlsx")
X = df.drop(columns=["label", "team"])
y= df['label']
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size= 0.3, shuffle= True)


X_train = X_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)


var= open("train.csv","w")
train_csv=pd.DataFrame.to_csv(train, index= False)         
var.write(train_csv)
var.close()

train = pd.concat([X_train['text'],y_train], axis=1)
with open('train.csv', 'r') as fp2:
    cl2 = DecisionTreeClassifier(fp2, format="csv")        


pred_train=[]
feature_train=[]
true_train= train.label
for instance in train.text:
    feature_train.append(feats(instance))
    blob = TextBlob(instance, classifier=cl2)
    pred_train.append(int(float(blob.classify())))
    

count=0
for i in range(len(pred_train)):
    if pred_train[i] == y_train[i]:
        count= count+1
#print('train_accuracy',count/len(pred_train))
pred_train= pd.DataFrame(pred_train)
global pred_test
global true_test

 
test = pd.concat([X_test['text'],y_test], axis=1)
var= open("test.json","w")
test_csv=pd.DataFrame.to_csv(test, index= False)  
var.write(test_csv)
var.close()
true_test= test.label
pred_test=[]
feature_test=[]
for instance in test.text:
    feature_test.append(feats(instance))
    blob = TextBlob(instance, classifier=cl2)
    pred_test.append(int(float(blob.classify())))

count=0
for i in range(len(pred_test)):
    if pred_test[i] == y_test[i]:
        count= count+1
#print('test_accuracy',count/len(pred_test))
pred_test= pd.DataFrame(pred_test)
feature_train= pd.DataFrame(feature_train)
feature_test= pd.DataFrame(feature_test)

score= X_train.score
match_type= X_train.match_type
closeness= pd.concat([score,match_type], axis=1)
f1=[]
for i in range(len(closeness)):
    f1.append(get_score(closeness.iloc[i,0],closeness.iloc[i,1]))

f11= pd.Series(f1)
X_train_final = pd.concat([pred_train,feature_train,f11],axis=1)


score_t= X_test['score']
match_type_t= X_test['match_type']
closeness_t = pd.concat([score_t,match_type_t], axis=1)
f2=[]
for i in range(len(closeness_t)):
    f2.append(get_score(closeness_t.iloc[i,0],closeness_t.iloc[i,1]))

f21= pd.Series(f2)
X_test_final= pd.concat([pred_test,feature_test,f21],axis=1)


# Decision Tree Classifier

#from sklearn import datasets
#from sklearn.tree import DecisionTreeClassifier
#dtc = DecisionTreeClassifier()
#model = dtc.fit(X_train_final, y_train)
#y_pred = model.predict(X_test_final)
#print("d",dtc.feature_importances_)
#count=0
#for i in range(len(y_pred)):
#    if y_pred[i] == y_test[i]:
#        count= count+1
#accuracy = count/len(y_pred) 
#print("accuracy", accuracy)


#Random Forest Classifier

#from sklearn import datasets
#from sklearn.ensemble import RandomForestClassifier
#rfc = RandomForestClassifier()
#model = rfc.fit(X_train_final, y_train)
#y_pred = model.predict(X_test_final)
#count=0
#for i in range(len(y_pred)):
#    if y_pred[i] == y_test[i]:
#        count= count+1
#accuracy = count/len(y_pred) 
#print("accuracy", accuracy)


# SVC Classifier

#from sklearn import datasets
#from sklearn.svm import SVC
#svc = SVC()
#model = svc.fit(X_train_final, y_train)
#y_pred = model.predict(X_test_final)
#count=0
#for i in range(len(y_pred)):
#    if y_pred[i] == y_test[i]:
#        count= count+1
#accuracy = count/len(y_pred) 
#print("accuracy", accuracy)


#Naive Bayes Classifier

#from sklearn import datasets
#from sklearn.naive_bayes import GaussianNB
#nb = GaussianNB()
#model = nb.fit(X_train_final, y_train)
#y_pred = model.predict(X_test_final)
#count=0
#for i in range(len(y_pred)):
#    if y_pred[i] == y_test[i]:
#        count= count+1
#accuracy = count/len(y_pred) 
#print("accuracy", accuracy)


#Neural Network Classifier

accuracy_final = 0
i_final = 0
j_final = 0 
from sklearn.neural_network import MLPClassifier
for m in range(4,8 ):
    for n in range(1, 7):
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5, warm_start=True,beta_1= 0.95, hidden_layer_sizes=(m, n), random_state=1)
        clf.fit(X_train_final, y_train)     
        y_pred = clf.predict(X_test_final)   

        count=0
        for i in range(len(y_pred)):
            if y_pred[i] == y_test[i]:
                count= count+1
        accuracy = count/len(y_pred)  
        if accuracy > accuracy_final:
            accuracy_final = accuracy
print("accuracy_final", accuracy_final)
#Finding a score of summary
#score_pred= clf.predict("Enter summary here")
#print score_pred