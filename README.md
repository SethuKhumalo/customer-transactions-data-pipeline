# Customer Transactions Data Pipeline Project

## Overview
This project demonstrates a beginner-level data engineering workflow using Python, SQL, SQLite, and Power BI.

The project simulates a real-world ETL (Extract, Transform, Load) pipeline where raw sales transaction data is cleaned, processed, stored in a relational database, analyzed using SQL, and visualized through interactive dashboards.

---

## Objectives
- Build a beginner ETL pipeline using Python
- Clean and transform raw sales data
- Store processed data in a SQL database
- Perform business analysis using SQL queries
- Create a Power BI dashboard for visualization
- Practice real-world data engineering concepts

---

## Tools & Technologies Used
- Python
- Pandas
- SQLite
- SQL
- Power BI
- VS Code
- GitHub

---

## Project Workflow

### 1. Data Extraction
Imported raw CSV sales transaction data into Python using Pandas.

### 2. Data Cleaning & Transformation
Performed:
- Duplicate removal
- Missing value handling
- Data formatting
- Data validation

### 3. Database Loading
Loaded cleaned data into a SQLite relational database using Python.

### 4. SQL Data Analysis
Performed SQL analysis including:
- Revenue analysis
- Monthly sales trends
- Product category performance
- Customer spending analysis
- Above-average transaction analysis

### 5. Dashboard Visualization
Created interactive Power BI dashboards to visualize:
- Total revenue
- Sales trends
- Product category performance
- Customer demographics

---

## SQL Analysis Examples

### Sales by Product Category

```sql
SELECT "Product Category",
       SUM("Total Amount") AS Total_Sales
FROM sales
GROUP BY "Product Category"
ORDER BY Total_Sales DESC;
```

### Monthly Revenue Trend

```sql
SELECT substr(Date,1,7) AS Month,
       SUM("Total Amount") AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month;
```

---

## Project Structure

```text
Customer-Transactions-Project/
│
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
│
├── scripts/
│   └── etl_pipeline.py
│
├── database/
│   └── sales.db
│
├── sql/
│   └── analysis_queries.sql
│
├── dashboard/
│   ├── customer_sales_dashboard.pbix
│   └── dashboard_screenshot.png
│
└── README.md
```

---

## Key Skills Demonstrated
- ETL Pipeline Development
- Data Cleaning & Transformation
- SQL Querying & Analysis
- Database Management
- Data Visualization
- Python Programming
- Business Intelligence Reporting

---

## Future Improvements
- Automate pipeline scheduling using Apache Airflow
- Integrate cloud storage using AWS
- Add real-time data streaming
- Expand dashboard analytics

---

## Author
Sethu Kholiwe Khumalo

Aspiring Data Engineer | Computer Science Graduate | Passionate about Data, Cloud & Analytics