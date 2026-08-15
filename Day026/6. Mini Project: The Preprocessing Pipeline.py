import numpy as np
import pandas as pd

# 1. Generate the simulated messy dataset
np.random.seed(5)
data = {
    "id": list(range(1, 51)),
    "age": np.random.randint(15, 75, size=50),
    # Concat standard salaries with two massive outliers to test IQR removal
    "income": np.concatenate([np.random.randint(30000, 120000, size=48), [650000, 950000]]),
    "city": np.random.choice(["Lagos", "Abuja", "Ibadan"], size=50),
    # Intentionally introducing missing values to test mode filling
    "gender": np.random.choice(["M", "F", None], size=50, p=[0.45, 0.45, 0.10]),
    "joined": pd.date_range("2020-01-01", periods=50, freq="ME")
}
df_messy = pd.DataFrame(data)

# Injecting intentional duplicates for testing
df_messy = pd.concat([df_messy, df_messy.iloc[[0, 1]]], ignore_index=True)


# 2. Create the Preprocessing Pipeline Function
def preprocess(df):
    # Keep a copy to avoid modifying the original data in place
    df_clean = df.copy()
    
    print(f"Shape before preprocessing: {df_clean.shape}")
    
    # Task 1: Drop duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Task 2: Fill missing gender with mode
    gender_mode = df_clean["gender"].mode()[0]
    df_clean["gender"] = df_clean["gender"].fillna(gender_mode)
    
    # Task 3: Remove income outliers using IQR method
    Q1 = df_clean['income'].quantile(0.25)
    Q3 = df_clean['income'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df_clean = df_clean[(df_clean['income'] >= lower_bound) & (df_clean['income'] <= upper_bound)]
    
    # Task 4: One-hot encode city and gender
    df_clean = pd.get_dummies(df_clean, columns=["city", "gender"], drop_first=False)
    
    # Task 5: Create age_group (Young: <30, Mid: 30-50, Senior: 50+)
    # Note: 0 to 29 is <30, 29 to 50 is 30-50, 50 to 100 handles 50+
    df_clean['age_group'] = pd.cut(df_clean["age"], 
                                   bins=[0, 29, 50, 120], 
                                   labels=["Young", "Mid", "Senior"])
    
    # Task 6: Create tenure_years from joined date to today
    df_clean['joined'] = pd.to_datetime(df_clean['joined'])
    df_clean['tenure_years'] = (pd.Timestamp.now() - df_clean["joined"]).dt.days / 365
    
    print(f"Shape after preprocessing: {df_clean.shape}")
    return df_clean

# 3. Execute the function
df_final = preprocess(df_messy)
print("\n--- Processed DataFrame (First 5 Rows) ---")
print(df_final.head().to_string())
