monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total onthly expenses: "))
rate = 0.05
time = 12
savings_monthly = monthly_income - monthly_expense
projected_savings = savings_monthly * time + (savings_monthly * 12 * rate)
print(f"Your monthly savings are ${savings_monthly}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
