import pandas as pd
import sqlite3

# Load CSV file
df = pd.read_csv("../data/sales_data.csv")

# Show first 5 rows
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove empty values
df = df.dropna()

# Create database connection
conn = sqlite3.connect("../database/sales.db")

# Save data into SQL database
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded successfully!")
df.to_csv("../data/cleaned_sales_data.csv", index=False)
# Close connection
conn.close()