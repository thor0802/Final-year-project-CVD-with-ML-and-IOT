import os
import pandas as pd
import numpy as np
import csv
import glob
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier

def process(path,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14):
    data=pd.read_csv(path)
    X=data.iloc[1:data.shape[0],0:14]
    y=data.iloc[1:data.shape[0],14:15]
    l=[]
    #l.append("eswar")
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)
    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)
  
    
    #l.append(a11)
    
    
    
     
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model2=RandomForestClassifier()
    X_test =pd.DataFrame([l])
    print("Testing data",X_test)
    model2.fit(X_train, y_train)
    y_pred = model2.predict(X_test)
    print("predicted")
    print(y_pred)
    result=""
    treat=""
    if y_pred[0]==0:
        result="Stage Normal"
        treat="dexrazoxane is no longer contraindicated"
    elif y_pred[0]==1:
        result="Stage Mild"
        treat="Adeno-associated virus gene therapy"
        
    elif y_pred[0]==2:
        result="Stage Moderate"
        treat="anti–interleukin-6 receptor antagonist such as tocilizumab "
    elif y_pred[0]==3:
        result="Stage Severe"
        treat="Immediate surgey need to given"
    else:
        result="No Disease"
    return result,treat



