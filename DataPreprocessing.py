# Task 1: Data Preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = {'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 75000, 90000]}
df = pd.DataFrame(data)

# Normalize salary
scaler = StandardScaler()
df['Salary_Scaled'] = scaler.fit_transform(df[['Salary']])

print(df)
