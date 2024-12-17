#This script calculates and displays the user's monthly savings and projected annual savings

#User inputs their monthly income and monthly expenses
monthly_income = int(input("Enter your monthly income: " ))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculate the projected annual savings
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Display the results
print("Your monthly savings are:",monthly_savings)
print("Projected savings after one year,with interest,is:",projected_annual_savings) 
