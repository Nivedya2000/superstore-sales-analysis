import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/superstore_cleaned.csv")

# ✅ Drop Postal Code column if present
if "Postal Code" in df.columns:
    df.drop(columns=["Postal Code"], inplace=True)

print("✅ Data loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:", df.columns)

# Create folders for saving outputs
if not os.path.exists("plots"):
    os.makedirs("plots")

if not os.path.exists("reports"):
    os.makedirs("reports")

# --- 1. Basic Info & Summary Statistics ---
summary_report = []

summary_report.append("📊 DATA SUMMARY REPORT\n")
summary_report.append("="*50 + "\n")

summary_report.append(f"✅ Dataset Shape: {df.shape}\n\n")
summary_report.append("📌 Column Data Types:\n")
summary_report.append(str(df.dtypes) + "\n\n")

summary_report.append("📌 Missing Values:\n")
summary_report.append(str(df.isnull().sum()) + "\n\n")

summary_report.append("📌 Descriptive Statistics (Numerical):\n")
summary_report.append(str(df.describe()) + "\n\n")

# Save summary to a text file
with open("reports/summary_report.txt", "w") as f:
    f.write("\n".join(summary_report))

print("📄 Summary report saved in reports/summary_report.txt")

# --- 2. Correlation Heatmap ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.close()

# --- 3. Sales & Profit Over Time ---
sales_trend = df.groupby("Month_Name")[["Sales", "Profit"]].sum().reindex(
    ["January", "February", "March", "April", "May", "June", 
     "July", "August", "September", "October", "November", "December"]
)

plt.figure(figsize=(10, 5))
plt.plot(sales_trend.index, sales_trend["Sales"], label="Sales", marker="o")
plt.plot(sales_trend.index, sales_trend["Profit"], label="Profit", marker="o")
plt.title("Monthly Sales & Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/sales_profit_trend.png")
plt.close()

# --- 4. Top 10 Products by Sales ---
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_r")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("plots/top_products.png")
plt.close()

# --- 5. Sales by Category ---
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(7, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title("Sales by Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("plots/category_sales.png")
plt.close()

# --- 6. Sales by Region ---
region_sales = df.groupby("Region")["Sales"].sum().sort_values()

plt.figure(figsize=(7, 5))
sns.barplot(x=region_sales.values, y=region_sales.index, palette="magma")
plt.title("Sales by Region")
plt.xlabel("Total Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("plots/region_sales.png")
plt.close()

# --- 7. Profit Margin vs Discount ---
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Discount", y="Profit Margin", hue="Category", alpha=0.7)
plt.title("Profit Margin vs Discount")
plt.xlabel("Discount")
plt.ylabel("Profit Margin")
plt.tight_layout()
plt.savefig("plots/profit_discount.png")
plt.close()

# --- 8. Top 10 States by Sales ---
state_sales = df.groupby("State")["Sales"].sum().nlargest(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=state_sales.values, y=state_sales.index, palette="coolwarm")
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("plots/top_states.png")
plt.close()

# --- 9. Top 10 Cities by Sales ---
city_sales = df.groupby("City")["Sales"].sum().nlargest(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=city_sales.values, y=city_sales.index, palette="plasma")
plt.title("Top 10 Cities by Sales")
plt.xlabel("Total Sales")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("plots/top_cities.png")
plt.close()

print("🎉 EDA complete! Plots saved in 'plots/' and summary report in 'reports/'.")


