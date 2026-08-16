import pandas as pd

data = {
    "name": ["  adeleke jesorg  ", "DANIEL ORIOLA", "  sarah SMITH  ", "john DOE"],
    "email": ["Adeleke@Gmail.com", "daniel@YAHOO.com", "Sarah@Hotmail.COM", "John@Outlook.com"],
    "phone": ["+234-80-1234-5678", "+234-81-8765-4321", "+234-70-9999-8888", "+234-90-1111-2222"]
}
df = pd.DataFrame(data)

# Clean name: strip + Title Case
df["clean_name"] = df["name"].str.strip().str.title()

# Extract username (before @), lowercase
df["username"] = df["email"].str.split("@").str[0].str.lower()

# Extract domain (after @), lowercase
df["domain"] = df["email"].str.split("@").str[1].str.lower()

# Extract network code (second group after splitting by "-")
df["network_code"] = df["phone"].str.split("-").str[1]

print(df)
