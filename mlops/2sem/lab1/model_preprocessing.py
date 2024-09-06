import pandas as pd
from sklearn.preprocessing import StandardScaler

# loading data
train_data = pd.read_csv('training_data/training_data.csv')
test_data = pd.read_csv('testing_data/test_data.csv')

# Preprocessing data
scaler = StandardScaler()

train_data_scaled = scaler.fit_transform(train_data[['temperature']])
train_data_scaled_df = pd.DataFrame(train_data_scaled, columns=['temperature'])
train_data_scaled_df['day'] = train_data['day']

test_data_scaled = scaler.transform(test_data[['temperature']])
test_data_scaled_df = pd.DataFrame(test_data_scaled, columns=['temperature'])
test_data_scaled_df['day'] = test_data['day']

# Saving data
pd.DataFrame(test_data_scaled_df).to_csv('training_data/temperature_train_scaled.csv', index=False)
pd.DataFrame(test_data_scaled_df).to_csv('testing_data/temperature_test_scaled.csv', index=False)

print('Data preprocessing complete')