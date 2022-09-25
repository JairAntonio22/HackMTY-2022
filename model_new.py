import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

from joblib import dump

#Label Encoding function
def label_encoding(df):
    
    cols = df.select_dtypes(include = 'object').columns

    for col in cols:
        le = LabelEncoder()
        df[col + 'Encode'] = le.fit_transform(df[col])
    
    df.drop(columns = cols, inplace = True)

#Make a fancy confusion matrix  
def confusion_matrix_graph(ytrue,ypred,title):
    
    matrix = confusion_matrix(ytrue,ypred)
    
    labels = ["{}\n{}\n{}".format(x,y,z) for x,y,z in zip(
        ('True Negative','False Positive','False Negative','True Positive'),
        [str(np.round(i,2)) for i in matrix.flatten()],
        [str(np.round(i,2)) for i in matrix.flatten()/np.sum(matrix)])]
    
    plt.figure(figsize = (16,9))
    plt.title(title)
    sns.heatmap(matrix, annot = np.asarray(labels).reshape(2,2), cmap = 'viridis', fmt = '')
    plt.show()


#Run the model
def model_run(data,col,name,title):
    y = data[col]
    x = data.drop(columns=[col])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state = 314)

    models = [
        DecisionTreeClassifier(class_weight='balanced'),
        KNeighborsClassifier(),
        GaussianNB(),
        LogisticRegression(solver = 'liblinear',class_weight='balanced'),
        RandomForestClassifier(class_weight='balanced'),
        AdaBoostClassifier(),
        MLPClassifier(),
        GradientBoostingClassifier()
    ]

    model_max = 0
    best_model = 0
    best_score = 0 #delete

    for model in models:
        model.fit(x_train, y_train)
        score = model.score(x_test, y_test)
        y_pred = model.predict(x_test)
        area = roc_auc_score(y_test, y_pred)
        #print('score', score)
        #print('area', area)
        if area > model_max:
            model_max = area
            best_model = model
            best_score = score #delete

    dump(best_model,"{}.joblib".format(name))
    print(best_model,model_max,best_score,name) #delete
    confusion_matrix_graph(y_test,y_pred,title)


#Main
#Diabetes.
data_diabetes = pd.read_csv('diabetes-dataset.csv')
data_diabetes.drop(columns = 'DiabetesPedigreeFunction', inplace = True)
model_run(data_diabetes,'Outcome','model_diabetes','Diabetes Confusion Matrix')

#Brain Stroke
data_stroke = pd.read_csv('healthcare-dataset-stroke-data.csv', index_col = 0)
data_stroke.dropna(inplace = True)
data_stroke.reset_index(drop = True, inplace = True)
label_encoding(data_stroke)
model_run(data_stroke,'stroke','model_stroke','Brain Stroke Confusion Matrix')

#Lung Cancer
data_lung = pd.read_csv('survey lung cancer.csv')
label_encoding(data_lung)
model_run(data_lung,'LUNG_CANCEREncode','model_lung','Lung Cancer Confusion Matrix')