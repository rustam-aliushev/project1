import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('weights_heights.csv', index_col='Index')

h = data['Height'].tolist()
H = [[i] for i in h]
w = data['Weight'].tolist()
W = [[i] for i in w]
data['BMI'] = data['Height'] / data['Weight'] ** 2
b = data['BMI'].tolist()
B = [[i] for i in b]

regHw = LinearRegression().fit(H, w)
w_pred = regHw.predict(H)
regBh = LinearRegression().fit(B, h)
h_pred = regBh.predict(B)
regWb = LinearRegression().fit(W, b)
b_pred = regWb.predict(W)

def plot():
    fig, ax = plt.subplots(1, 3)
    ax[0].scatter(H, w, color='#3399FF', label='Данные')
    ax[0].plot(H, w_pred, color='#004C99', label='Линия регрессии', linewidth=3)
    ax[0].set_xlabel('Рост')
    ax[0].set_ylabel('Вес')
    ax[0].set_title('Рост и Вес')

    ax[1].scatter(B, h, color='#3399FF', label='Данные')
    ax[1].plot(B, h_pred, color='#004C99', label='Линия регрессии', linewidth=3)
    ax[1].set_xlabel('ИМТ')
    ax[1].set_ylabel('Рост')
    ax[1].set_title('ИМТ и Рост')

    ax[2].scatter(W, b, color='#3399FF', label='Данные')
    ax[2].plot(W, b_pred, color='#004C99', label='Линия регрессии', linewidth=3)
    ax[2].set_xlabel('Вес')
    ax[2].set_ylabel('ИМТ')
    ax[2].set_title('Вес и ИМТ')

    return fig