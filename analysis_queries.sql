SELECT "Product Category",
       SUM("Total Amount") AS Total_Sales
FROM sales
GROUP BY "Product Category"
ORDER BY Total_Sales DESC;

SELECT Gender,
       SUM("Total Amount") AS Revenue
FROM sales
GROUP BY Gender;

SELECT substr(Date,1,7) AS Month,
       SUM("Total Amount") AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month;