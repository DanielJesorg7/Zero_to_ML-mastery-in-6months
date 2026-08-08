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

# 2. Prints shape, columns, dtypes
print("___ Shape ___")
print(df.shape)
print("\n___ Columns ___")
print(df.columns)
print("\n___ Dtypes ___")
print(df.dtypes)

# 3. Prints df.isnull().sum() to show missing count per column
print("\n___ Missing Count Per Column ___")
print(df.isnull().sum())

# 4. Prints rows with ANY missing values
print("\n___ Rows with ANY Missing Values ___")
print(df[df.isnull().any(axis=1)])
