import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = {
    "name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "gender": ["M", "F", "M", "F", "M", None, "F", "M", "F", "M"],
    "age": [25, 30, None, 35, 28, 40, 22, None, 33, 29],
    "city": ["Lagos", "Abuja", "Lagos", "Kano", "Abuja", "Lagos", "Kano", "Abuja", "Lagos", "Kano"],
    "salary": [500000, 800000, 300000, None, 600000, 1000000, 200000, 750000, None, 550000],
    "churn": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

def prepare_for_ml(df, target_col):
    df = df.copy()
    
    # 1. Drop name
    df = df.drop(columns=["name"])
    
    # 2. Fill missing gender with mode
    df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
    
    # 3. Fill missing age with median
    df["age"] = df["age"].fillna(df["age"].median())
    
    # 4. Fill missing salary with mean
    df["salary"] = df["salary"].fillna(df["salary"].mean())
    
    # 5. One-hot encode gender and city
    df = pd.get_dummies(df, columns=["gender", "city"])
    
    # 6. Split
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = prepare_for_ml(df, "churn")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
