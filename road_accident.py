# -*- coding: utf-8 -*-
"""road accident

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RzF7ldyp41rcAjsPG5Ggqi78sRto8D9Y
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

data = pd.read_csv('/content/accident.csv')
data.head()

X = data[['weather', 'time', 'road', 'speed', 'traffic', 'age', 'vehicle']]
y = data['condition']  # Dependent variable (accident condition)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

joblib.dump(model, 'accident_condition_model.pkl')
print("Model saved as 'accident_model.pkl'")

example_data = np.array([[1, 3, 2, 60, 4, 30, 1]])  # input for prediction
predicted_condition = model.predict(example_data)
print(f"Predicted Accident condition: {predicted_condition[0]}")