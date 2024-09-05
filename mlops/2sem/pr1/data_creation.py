import pandas as pd
import numpy as np
import os

# create folders for source data
os.makedirs('training_data', exist_ok=True)
os.makedirs('testing_data', exist_ok=True)

def data_creation(num_days=26500, noise_level=0.5, anomaly_days=[20, 30, 40]):
    """create shuffle data"""

    days = np.arange(num_days)
    temperature = 20 + 10 * np.sin(2 * np.pi * days / 30)
    noise = np.random.normal(scale=noise_level, size=len(days))
    temperature += noise

    # anomaly became
    for day in anomaly_days:
        temperature[day] += np.random.choice([-10, 10])

    df = pd.DataFrame({'day': days, 'temperature': temperature})

    return df

full_data = data_creation()
train_data = full_data.sample(frac=0.7, random_state=42)
test_data = full_data.sample(frac=0.3, random_state=42)

train_data.to_csv('training_data/training_data.csv', index=False)
test_data.to_csv('testing_data/test_data.csv', index=False)

print('Data created')
