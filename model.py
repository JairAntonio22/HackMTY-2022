import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from joblib import dump

data = pd.read_csv('diabetes-dataset.csv')

y = data['Outcome']
x = data.drop(columns=['Outcome', 'DiabetesPedigreeFunction'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10)

models = [
    DecisionTreeClassifier(),
    KNeighborsClassifier(),
    GaussianNB(),
    LogisticRegression(solver='liblinear')
]

model_arr = []

for model in models:
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    y_pred = model.predict(x_test)
    area = roc_auc_score(y_test, y_pred)
    print('score', score)
    print('area', area)
    model_arr.append((area,model))

dump(max(model_arr)[1],"model_diabetes.joblib")

