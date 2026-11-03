# Step 1: Install Scikit-learn

%pip install scikit-learn


# Step 2: Import Libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# Step 3: Load Dataset
df = pd.read_csv("student_marks_cleaned.csv")


# Step 4: Perform One-Hot Encoding
print("Original Study_Method Column")
print(df["Study_Method"])

df_onehot = pd.get_dummies(
    df,
    columns=["Study_Method"],
    dtype=int
)

print("\nAfter One-Hot Encoding")

print(df_onehot.head().to_string())


# Step 5: Perform Label Encoding
label = LabelEncoder()

df["Gender_Encoded"] = label.fit_transform(
    df["Gender"]

)

print(
    df[["Gender", "Gender_Encoded"]]

    .to_string(index=False)
)


# Step 6: Calculate Skewness
print("\nSkewness of Numerical Columns")
print(df.skew(numeric_only=True))


# Step 7: Perform Standard Scaling
scaler = StandardScaler()
columns = [

    "Study_Hours",

    "Attendance (%)",

    "Previous_Marks",

    "Sleep_Hours"

]


df[columns] = scaler.fit_transform(df[columns])


print("\nAfter Standard Scaling")

print(df.head().to_string())


# Step 8: Perform Min-Max Scaling
df = pd.read_csv("student_marks_cleaned.csv")
minmax = MinMaxScaler()

df[columns] = minmax.fit_transform(df[columns])

print("\nAfter Min-Max Scaling")
print(df.head().to_string())


# Step 9: Perform Feature Creation
df["Study_Efficiency"] = (
    df["Study_Hours"] *
    df["Attendance (%)"] / 100

)

print("\nFeature Created")
print(

    df[[

         "Study_Hours",

         "Attendance (%)",

         "Study_Efficiency"

    ]]

)


# Step 10: Perform Feature Selection
print("\nCorrelation with Target (Marks)")
corr = df.corr(numeric_only=True)
print(corr["Marks"].sort_values(ascending=False))