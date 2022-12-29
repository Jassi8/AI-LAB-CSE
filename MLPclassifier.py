import numpy as np
import pandas as pd

data=pd.read_csv('/content/HR_comma_sep (1).csv')

data.head()

data['Departments']

from sklearn import preprocessing

le=preprocessing.LabelEncoder()

data['salary']=le.fit_transform(data['salary'])
data['Departments']=le.fit_transform(data['Departments'])

x=data[['satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','Departments','salary']]
y=data['left']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
x_train

#import MLP classifier
from sklearn.neural_network import MLPClassifier

clf=MLPClassifier(hidden_layer_sizes=(6,5),
                  random_state=5,
                  verbose=True,
                  learning_rate_init=0.01)
clf.fit(x_train,y_train)

ypred=clf.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,ypred )