import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "region": ["Lagos", "Lagos", "Abuja", "Abuja", "Kano"],
    "product": ["Laptop", "Phone", "Laptop", "Monitor", "Phone"],
    "amount": [500000, 200000, 450000, 80000, 180000]
})

# pivot_table = Excel-style summary
# index = rows, columns = columns, values = what to aggregate, aggfunc = how
pivot = sales.pivot_table(
    values="amount",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0  # replace NaN with 0
)

print(pivot)
