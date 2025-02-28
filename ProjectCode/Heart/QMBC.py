# importing libraries 
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.svm import SVC 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.datasets import load_iris 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
  
# loading iris dataset 
data=pd.read_csv(path)
	X=data.iloc[1:data.shape[0],0:14]
	y=data.iloc[1:data.shape[0],14:15]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
	from sklearn.preprocessing import MinMaxScaler
	MinMax = MinMaxScaler(feature_range= (0,1))
	X_train = MinMax.fit_transform(X_train)
	X_test = MinMax.transform(X_test)
  
# group / ensemble of models 
estimator = [] 
estimator.append(('LR',  
                  LogisticRegression(solver ='lbfgs',  
                                     multi_class ='multinomial',  
                                     max_iter = 200))) 
estimator.append(('SVC', SVC(gamma ='auto', probability = True))) 
estimator.append(('DTC', DecisionTreeClassifier())) 
  
# Voting Classifier with hard voting 
vot_hard = VotingClassifier(estimators = estimator, voting ='hard') 
vot_hard.fit(X_train, y_train) 
y_pred = vot_hard.predict(X_test) 
  
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
result2=open("results/resultQMBC.csv","w")
result2.write("ID,Predicted Value" + "\n")
for j in range(len(y_pred)):
    result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
result2.close()
mse=mean_squared_error(y_test, y_pred)
mae=mean_absolute_error(y_test, y_pred)
ps=precision_score(y_test, y_pred, average='macro')
rs=recall_score(y_test, y_pred, average='macro')
f1=f1_score(y_test, y_pred, average='macro')

r2=r2_score(y_test, y_pred)
print("---------------------------------------------------------")
print("MSE VALUE FOR QMBC IS %f "  % mse)
print("MAE VALUE FOR QMBC IS %f "  % mae)
print("R-SQUARED VALUE FOR QMBC IS %f "  % r2)
rms = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE VALUE FOR QMBC IS %f "  % rms)
ac=accuracy_score(y_test,y_pred)
print ("ACCURACY VALUE QMBC IS %f" % ac)
print("Precision Score QMBC IS %f "  % ps)
print("Recall Score QMBC IS %f "  % rs)
print("F1 Score MV QMBC %f "  % f1)

print("---------------------------------------------------------")
result2=open('results/QMBCMetrics.csv', 'w')
result2.write("Parameter,Value" + "\n")
result2.write("MSE" + "," +str(mse) + "\n")
result2.write("MAE" + "," +str(mae) + "\n")
result2.write("R-SQUARED" + "," +str(r2) + "\n")
result2.write("RMSE" + "," +str(rms) + "\n")
result2.write("ACCURACY" + "," +str(ac) + "\n")
result2.write("Precision" + "," +str(ps) + "\n")
result2.write("Recall" + "," +str(rs) + "\n")
result2.write("F1" + "," +str(f1) + "\n")
result2.close()
df =  pd.read_csv('results/QMBCMetrics.csv')
acc = df["Value"]
alc = df["Parameter"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c"]
explode = (0.1, 0, 0, 0, 0,0,0,0)  
fig = plt.figure()
plt.bar(alc, acc,color=colors)
plt.xlabel('Parameter')
plt.ylabel('Value')
plt.title('MV Metrics Value')
fig.savefig('results/QMBCMetricsValue.png') 
plt.pause(5)
plt.show(block=False)
plt.close()