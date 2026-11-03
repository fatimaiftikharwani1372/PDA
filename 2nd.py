import pandas as pd
import numpy as np

df = pd.read_csv("student_marks_cleaned.csv")

print("Original Marks:")
print(df[["Student_ID", "Marks"]].to_string(index=False))

# Calculate Q1, Q3 and IQR
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Lower Limit =", lower_limit)
print("Upper Limit =", upper_limit)

# Detect outliers
outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]

print("\nOutliers Detected:")
print(outliers.to_string(index=False))

# Create a copy of dataset
df_mean = df.copy()

# Calculate mean
mean_value = df_mean["Marks"].mean()

# Replace outlier with mean
df_mean.loc[(df_mean["Marks"] < lower_limit) | (df_mean["Marks"] > upper_limit), "Marks"] = mean_value

print("\nDataset After Replacing Outlier with Mean:")
print(df_mean.to_string())

# Create a copy of dataset
df_median = df.copy()

# Calculate median
median_value = df_median["Marks"].median()

# Replace outlier with median
df_median.loc[(df_median["Marks"] < lower_limit) | (df_median["Marks"] > upper_limit), "Marks"] = median_value

print("\nDataset After Replacing Outlier with Median:")
print(df_median.to_string())

print(df["Marks"].to_list())
print("Mean :", df["Marks"].mean())
print("Median :", df["Marks"].median())