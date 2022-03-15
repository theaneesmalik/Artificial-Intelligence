import pandas as pd
dataset = pd.read_csv("/dataset.csv")
dataset
X = dataset.iloc[:,1].values
y = dataset.iloc[:,0:1].values
X
y
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lr
X_train, X_test, y_train, y_test = tts(X,y, test_size=0.4, random_state=0)
X_train
X_test
y_train
y_test
model = lr()
model
model.fit(X_train, y_train)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
X_train
y_pred = model.predict(X_test)
X_test
y_pred
y_test
import matplotlib.pyplot as plt
plt.scatter(X_train, y_train)
plt.plot(X_test, y_pred)
from sklearn.metrics import r2_score as r2_score
r2_score(y_test,y_pred)



