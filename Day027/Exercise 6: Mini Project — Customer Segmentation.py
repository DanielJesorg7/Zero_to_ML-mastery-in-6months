import pandas as pd
import numpy as np

np.random.seed(7)
data = {
    "customer_id": range(1, 51),
    "gender": np.random.choice(["M", "F"], 50),
    "age": np.random.randint(18, 70, 50),
    "city": np.random.choice(["Lagos", "Abuja", "Kano", "PH"], 50),
    "total_spend": np.random.randint(50000, 2000000, 50),
    "transactions": np.random.randint(1, 50, 50)
}
df = pd.DataFrame(data)

def segment_customers(df):
    # 1. Crosstab: gender vs city (counts)
    ct = pd.crosstab(df["gender"], df["city"])
    print("--- Gender vs City Counts ---")
    print(ct)
    
    # 2. Average total_spend by gender and city
    avg_spend = pd.crosstab(df["gender"], df["city"], values=df["total_spend"], aggfunc="mean")
    print("\n--- Average Spend by Gender & City ---")
    print(avg_spend)
    
    # 3. Spend per transaction
    df["spend_per_transaction"] = df["total_spend"] / df["transactions"]
    
    # 4. Segment using pd.cut
    bins = [0, 200000, 1000000, float("inf")]
    labels = ["Budget", "Regular", "VIP"]
    df["segment"] = pd.cut(df["total_spend"], bins=bins, labels=labels)
    
    # 5. Pivot table: avg spend_per_transaction by segment and gender
    pivot = df.pivot_table(
        values="spend_per_transaction",
        index="segment",
        columns="gender",
        aggfunc="mean"
    )
    print("\n--- Avg Spend Per Transaction by Segment & Gender ---")
    print(pivot)
    
    return df

df = segment_customers(df)
