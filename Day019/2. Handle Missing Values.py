import pandas as pd
import numpy as np

# --- STEP 1: Create the CSV file manually in code ---
header = ['name', 'age', 'math_score', 'english_score']
data = [
    ['Adeleke', 25, 85, 78],
    ['Daniel', np.nan, 90, 82],       # Use np.nan for missing values
    ['Sarah', 24, 72, np.nan],       # Use np.nan for missing values
    ['John', 22, 60, 55],
    ['Mary', 23, 95, 92]
]

# Create DataFrame and save it as students.csv
df_initial = pd.DataFrame(data, columns=header)
df_initial.to_csv('students.csv', index=False)


# --- STEP 2: The Assignment Program ---

# 1. Reads the CSV
df = pd.read_csv('students.csv')

df['age'] = df['age'].fillna(df['age'].mean())
df['math_score'] = df['math_score'].fillna(0)
df['english_score'] = df['english_score'].fillna(df['english_score'].median())
print(df)
print(df.isnull().sum())
