import yfinance as yf

stock = yf.download("AAPL",
                    start="2020-01-01",
                    end="2025-01-01")

print(stock.head())

import pandas as pd

stock['Prediction'] = stock['Close'].shift(-1)

stock = stock.dropna()

print(stock.head())


X = stock[['Close']]
y = stock['Prediction']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    shuffle=False
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions[:5])




from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MSE:", mse)
print("R² Score:", r2)


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.plot(y_test.values, label="Actual Price")
plt.plot(predictions, label="Predicted Price")

plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.legend()
plt.show()