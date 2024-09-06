from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd


train_data = pd.read_csv('training_data/temperature_train_scaled.csv')
X_train = train_data['day'].values.reshape(-1, 1)
y_train = train_data['temperature']
model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, 'model/model.pkl')

print('Data preparation done')