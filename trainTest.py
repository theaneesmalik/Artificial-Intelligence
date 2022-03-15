import pandas as pd
dataset = pd.read_csv("/kc_house_data.csv.zip")
dataset
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lr
dataset = dataset.drop(columns=['sqft_living','sqft_lot','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','lat','long','sqft_living15','sqft_lot15'])
dataset
X = dataset.iloc[:,[0,3,4,5,6]].values
X
Y = dataset.iloc[:,[2]].values
Y
X_train, X_test, Y_train, Y_test = tts(X,Y, test_size=0.4, random_state=0)
X_train
X_test
Y_train
Y_test
model = lr()
model
model.fit(X_train, Y_train)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
X_train
Y_pred = model.predict(X_test)
