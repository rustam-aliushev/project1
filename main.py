import shiny
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('weights_heights.csv', index_col='Index')
X1 = data['Height'].tolist()
X1 = [[x] for x in X1]
y1 = data['Weight'].tolist()

reg = LinearRegression().fit(X1, y1)

y_pred = reg.predict(X1)
plt.scatter(X1, y1, color='blue', label='Данные')
plt.plot(X1, y_pred, color='red', label='Линия регрессии')
plt.xlabel('X1')
plt.ylabel('y1')
plt.title('Линейная регрессия')
plt.legend()
plt.show()