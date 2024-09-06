from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


model = joblib.load('model/model.pkl')
test_data = pd.read_csv('testing_data/temperature_test_scaled.csv')

X_test = test_data.index.values.reshape(-1, 1)
predictions = model.predict(X_test)

test_data['Predicted Temperature'] = predictions

test_data.to_csv('model/temp_prediction_test.csv', index=False)

actual_values = test_data['temperature']

mae = mean_absolute_error(actual_values, predictions)
mse = mean_squared_error(actual_values, predictions)
r2 = r2_score(actual_values, predictions)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')

print('Data Prediction complete')