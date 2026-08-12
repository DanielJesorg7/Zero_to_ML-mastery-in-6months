import numpy as np
import pandas as pd

def generate_eda_report(df):
    print("==========================================")
    print("          EDA DIAGNOSTIC REPORT          ")
    print("==========================================")
    
    # 1. Shape and Column Names
    print(f"1. Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"   Column Names:  {list(df.columns)}")
    
    # 2. Missing Value Percentage
    print("\n2. Missing Value Percentages:")
    null_pct = (df.isnull().sum() / len(df)) * 100
    print(null_pct.map("{:.2f}%".format))
    
    # 3. Numeric Summary (mean, median, std)
    print("\n3. Numerical Features Distribution Metrics Summary:")
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 0:
        summary_frame = pd.DataFrame({
            'Mean': df[num_cols].mean(),
            'Median': df[num_cols].median(),
            'Std_Dev': df[num_cols].std()
        })
        print(summary_frame)
    else:
        print("   No numeric tracking columns found.")
        
    # 4. Categorical Summary (value counts)
    print("\n4. Categorical Feature Distributions Profile:")
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        for column in cat_cols:
            print(f"\n--- Value Distribution Breakdown for attribute '{column}' ---")
            print(df[column].value_counts())
    else:
        print("   No text/categorical structures captured.")
        
    # 5. Top 3 Correlated Numeric Column Pairs
    print("\n5. Top 3 Linear Correlation Matrix Associations Pairings:")
    if len(num_cols) > 1:
        corr_matrix = df[num_cols].corr()
        # Stack indices to transform from structural tables matrix format to structured index series mapping array format
        stacked_corr = corr_matrix.unstack()
        # Drop duplicates where properties reference identical values mapping back onto themselves
        filtered_pairs = stacked_corr[stacked_corr.index.get_level_values(0) != stacked_corr.index.get_level_values(1)]
        
        # Sort linear coefficients values in absolute scale
        sorted_pairs = filtered_pairs.abs().sort_values(ascending=False)
        # Drop directional mirroring matrices duplicates (e.g. tracking index mapping [X,Y] behaves identically to tracking index mapping [Y,X])
        top_3_pairs = sorted_pairs.iloc[::2].head(3)
        
        if not top_3_pairs.empty:
            for position, ((var1, var2), score) in enumerate(top_3_pairs.items(), 1):
                raw_coefficient = stacked_corr.loc[var1, var2]
                print(f"   Rank {position}: '{var1}' & '{var2}' -> Correlation Coeff: {raw_coefficient:.4f}")
        else:
            print("   No valid metric variance coefficients identified.")
    else:
        print("   Inadequate dimensional properties volume limits to generate comparative analytics matrix.")
    print("==========================================\n")


# --- RUNNING LOCAL COMPONENT VALIDATION STANDALONE TESTS ---
print("Running Standalone Function Pipeline Tests...\n")

# Test Run 1: Creating a small test DataFrame dynamically
simple_test_df = pd.DataFrame({
    'employee_age': [25, 30, 35, 40, 28],
    'years_experience': [2, 5, 8, 12, 3],
    'performance_score': [85, 90, 78, 88, 92],
    'department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering']
})

print("### TEST CASE A: SIMPLE MANUALLY CONSTRUCTED DATAFRAME ###")
generate_eda_report(simple_test_df)

# Test Run 2: Executing against the previously processed system state pipeline assets if available
try:
    df_engineered = pd.read_csv("sales_data_engineered.csv")
    print("### TEST CASE B: PRIMARY SYSTEM SALES PIPELINE OBJECTS ###")
    generate_eda_report(df_engineered)
except FileNotFoundError:
    print("Note: Skipping Test Case B target execution sequence profiles since 'sales_data_engineered.csv' asset tracking data was not initialized locally.")
