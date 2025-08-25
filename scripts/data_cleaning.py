# data_cleaning.py

import pandas as pd

# Load dataset
df = pd.read_csv("data/Superstore.csv", encoding='latin1')

print("🔍 Original dataset shape:", df.shape)

# --- Basic Cleaning ---
# Remove duplicates
df = df.drop_duplicates()
print("✅ Removed duplicates. Shape:", df.shape)

# Handle missing values
df = df.dropna()  # drop rows with missing values
print("✅ Handled missing values. Shape:", df.shape)

# Convert Order Date and Ship Date to datetime
date_columns = ["Order Date", "Ship Date"]
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Drop rows with invalid dates
df = df.dropna(subset=["Order Date", "Ship Date"])

# Ensure numeric columns
for col in ["Sales", "Quantity", "Discount", "Profit"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# --- Feature Engineering ---
# Add Year and Month from Order Date
if "Order Date" in df.columns:
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month_Name"] = df["Order Date"].dt.strftime("%B")

# Add Profit Margin
if "Profit" in df.columns and "Sales" in df.columns:
    df["Profit Margin"] = (df["Profit"] / df["Sales"]).round(2)

# Save cleaned dataset
df.to_csv("data/superstore_cleaned.csv", index=False)

print("🎉 Cleaning complete! Cleaned file saved as data/superstore_cleaned.csv")
