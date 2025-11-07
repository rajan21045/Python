import numpy as np

# Dataset Creation 
sales_data = np.random.randint(50, 500, size=(10, 7))
print("--- Sales Data (10 Employees x 7 Days) ---")
print(sales_data)

# Step 2: Total Sales for each employee
total_sales_per_employee = np.sum(sales_data, axis=1)
print("\n--- Total Sales for Each Employee (Sum across 7 days) ---")
print(total_sales_per_employee)

# Step 3: Average Sales per Day
average_daily_sales = np.mean(sales_data, axis=0)
print("\n--- Average Sales Across All Employees per Day (Mean across 10 employees) ---")
print(average_daily_sales)

# Step 4: Increase sales by 10%
increased_sales = sales_data * 1.10
print("\n--- Increased Sales Data: After 10% Boost ---")
print(increased_sales)

# Step 5: Identify employees with total sales > 2000
high_sales_employees_mask = total_sales_per_employee > 2000
high_sales_totals = total_sales_per_employee[high_sales_employees_mask]
high_sales_indices = np.where(high_sales_employees_mask)[0] + 1

print(f"\n--- Employees with Total Sales > 2000 ---")
print(f"Total Sales > 2000: {high_sales_totals}")
print(f"Employee IDs (1-indexed): {high_sales_indices}")

# Step 6: Overall statistics
mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)
std_dev_sales = np.std(sales_data)
print("\nOverall Mean Sales:", mean_sales)
print("Overall Median Sales:", median_sales)
print("Overall Standard Deviation of Sales:", std_dev_sales)

# Step 7: Maximum Sales in a Day for Each Employee
max_sales_in_a_day = np.max(sales_data, axis=1)
print("\n--- Maximum Sales in a Day for Each Employee ---")
print(max_sales_in_a_day)

# Step 8: Employee with Highest Total Sales
best_employee = np.argmax(total_sales_per_employee)
print("\nEmployee with Highest Total Sales (0-indexed):", best_employee)
print("Employee ID (1-indexed):", best_employee + 1)
