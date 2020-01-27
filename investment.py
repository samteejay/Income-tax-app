"""

Program: investment.py
Author: Samuel Tijani

Purpose: Compute a person's income tax.

Analysis & Design:
1. Significant constants
		tax rate
		standard deduction
		deduction per dependent
2.  User inputs 
		gross income
		number of dependents
3. Design computations:
		taxable income = gross income - the standard deduction - 
						a deduction for each dependent
		income tax = is a fixed percentage of the taxable income
4. Expected output
		the income tax
		
"""

# Accepts the inputs
start_balance = eval(input("Enter the investment amount: "))
years = eval(input("Enter the number of years: "))
rate = eval(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
total_interest = 0

# Display the header for the table
print("%4s%18s%10s%16s" % \
	 ("Year", "starting balance", "Interest", "Ending balance"))
		
# Compute and display the results for each years
for year in range(1, years + 1):
    interest = start_balance * rate
    end_balance = start_balance + interest
    print("%4d%18.2f%10.2f%16.2f" % \
         (year, start_balance, interest, end_balance))
	
    start_balance = end_balance
    total_interest += interest
	
# Display the totals for the period
print("Ending balance: $%0.2f" % end_balance)
print("Total interest earned: $%0.2f" % total_interest)
		  

	