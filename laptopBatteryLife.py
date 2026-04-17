
import math
import os
import random
import re
import sys
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
    
def predict_hours(testX):
    X = []
    y = []
    full = -1
    with open('trainingdata.txt','r') as file:
        for line in file:
            data = line.split(",")
            if float(data[1]) < 8:
                X.append(float(data[0]))
                y.append(float(data[1]))
            else:
                if float(data[0]) > full:
                    full = float(data[0])

    if float(testX) > full:
        return 8.00

    # print(np.array(X).reshape(-1, 1))
    lr = LinearRegression()
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(np.array(X).reshape(-1, 1))
    lr.fit(X_poly, y)

    testX_poly = poly.transform(np.array([[testX]]))
    predicted = lr.predict(testX_poly)
    return round(predicted[0], 2)

if __name__ == '__main__':
    timeCharged = float(input().strip())
    print(predict_hours(timeCharged))