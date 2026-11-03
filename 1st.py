%pip install openpyxl

import pandas as pd

df = pd.read_excel('student_performace_dataset.xlsx')

print("Original Dataset:")
print(df.head(15))

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].median())

df["Attendance (%)"] = df["Attendance (%)"].fillna(df["Attendance (%)"].median())

print("\nMissing Values After Filling:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

print("\nCleaned Dataset:")
print(df)

print("\nData Cleaning Completed Successfully.")

df.to_csv("student_marks_cleaned.csv", index=False)