import numpy as np
import pandas as pd

# 1. Create DataFrames with exact values derived from the image
employees = pd.DataFrame(
    {
        "emp_id": [1, 2, 3, 4],
        "name": ["Adeleke", "Daniel", "Sarah", "Brian"],
        "dept_id": [101, 102, 101, 103],
    }
)

departments = pd.DataFrame(
    {
        "dept_id": [101, 102, 103],
        "dept_name": ["Engineering", "Sales", "Marketing"],
        "budget": [5000000, 3000000, 2000000],
    }
)

# 2. Merge DataFrames (left join on dept_id)
merged_df = pd.merge(employees, departments, on="dept_id", how="left")

# 3. Add a salary column with random values between 300000 and 800000
np.random.seed(42)  # For consistent reproducible outputs
merged_df["salary"] = np.random.randint(300000, 800001, size=len(merged_df))

# 4. Group by dept_name and calculate average salary
avg_salary_per_dept = merged_df.groupby("dept_name")["salary"].mean()

# 5. Print the department with the highest average salary
highest_dept = avg_salary_per_dept.idxmax()
highest_value = avg_salary_per_dept.max()

print("--- Average Salary Per Department ---")
print(avg_salary_per_dept.to_string())
print("\n--- Highest Earner ---")
print(f"Department: {highest_dept} (Average Salary: ${highest_value:,.2f})")
