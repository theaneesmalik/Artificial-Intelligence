import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import PolynomialFeatures as pf

dataset = pd.read_csv("E:/Idrees/file.csv")
X = dataset.iloc[:, [0]].values
y = dataset.iloc[:, [1]].values

X_train, X_test, y_train, y_test = tts(X, y)

polyModel = pf(degree=4)
linearModel = lr()
polyFeatures = polyModel.fit_transform(X)
linearModel.fit(polyFeatures, y)

y_pred = linearModel.predict(polyFeatures)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title('Polynomial Regression')
plt.xlabel("Roll No.")
plt.ylabel("Marks")
plt.show()