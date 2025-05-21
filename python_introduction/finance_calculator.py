monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total onthly expenses: "))
rate = 0.05
time = 12
monthly_savings = monthly_income - monthly_expense
projected_savings = monthly_savings * time + (monthly_savings * 12 * rate)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
