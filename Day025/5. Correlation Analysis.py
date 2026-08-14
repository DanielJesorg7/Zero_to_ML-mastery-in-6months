import numpy as np
import pandas as pd

np.random.seed(42)
data = {
    "study_hours": np.random.randint(1, 10, 50),
    "sleep_hours": np.random.randint(4, 9, 50),
    "exam_score": np.random.randint(40, 100, 50)
}
df  = pd.DataFrame(data)
correlation_matrix = df.corr()
print(correlation_matrix)

#Study_hour correlates more with exam score (sleep_hour was negative)