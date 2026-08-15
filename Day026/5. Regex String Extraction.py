import pandas as pd

# Recreating the DataFrame with complete dummy data
data = {
    "email": ["adeleke@gmail.com", "chioma@yahoo.com", "jide@outlook.com"],
    "phone": ["080-1234-5678", "081-5678-1234", "090-9999-8888"]
}
df = pd.DataFrame(data)

# 1. Extract the domain after @
df['domain'] = df['email'].str.extract(r"@(.+)$")

# 2. Extract the area code (first 3 digits) from phone
df['area_code'] = df['phone'].str.extract(r"^(\d{3})-")

# Display results
print(df)
