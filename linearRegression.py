import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('student-mat.csv', sep=';')
data = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
data = df[['age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]

data['sex'] = data['sex'].map({'F': 0, 'M': 1})

prediction = 'G3'

X = np.array(data.drop([prediction], 1))
Y = np.array(data[prediction])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(accuracy*100)
