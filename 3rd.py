%pip install matplotlib

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student_marks_cleaned.csv")

# 1. Dataset Shape
print("Dataset Shape:")
print(df.shape)

# 2. Dataset Information
print("\nDataset Information:")
print(df.info())

# 3. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 4. Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# 5. Histogram
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()

# 6. Box Plot
plt.figure(figsize=(8,5))
df.boxplot()
plt.title("Box Plot")
plt.xticks(rotation=45)
plt.show()


# 7. Scatter Plot

# Study Hours vs Marks
plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# Attendance vs Marks
plt.figure(figsize=(6,4))
plt.scatter(df["Attendance (%)"], df["Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.show()

# Sleep Hours vs Marks
plt.figure(figsize=(6,4))
plt.scatter(df["Sleep_Hours"], df["Marks"])
plt.xlabel("Sleep Hours")
plt.ylabel("Marks")
plt.title("Sleep Hours vs Marks")
plt.show()


# 8. Pair Plot
from pandas.plotting import scatter_matrix
scatter_matrix(df.select_dtypes(include=['number']),
 figsize=(10,10))
plt.show()


# 9. Heat Map
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
plt.imshow(corr, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heat Map")
plt.show()