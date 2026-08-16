import pandas as pd
import numpy as np

np.random.seed(3)
data = {
    "region": np.random.choice(["North", "South", "East"], 20),
    "product": np.random.choice(["A", "B", "C"], 20),
    "sales": np.random.randint(10000, 100000, 20),
    "profit": np.random.randint(1000, 20000, 20)
}
df = pd.DataFrame(data)

pivot = df.pivot_table(
    values=["sales", "profit"],
    index="region",
    columns="product",
    aggfunc="sum",
    margins=True,
    fill_value=0
)
print(pivot)
