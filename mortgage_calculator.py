'''
Calculate the monthly payments of a fixed term mortgage over Nth terms at a given interest rate.
Also figure out how long it will take the user to pay back the loan.
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually)
'''

annual_interest_rate = 7
monthly_interest_rate = annual_interest_rate / (12 * 100)
principal = 500000  # amount of loan borrowed
loanterm_in_years = 30
loanterm_in_month = loanterm_in_years * 12
N = loanterm_in_month
r = monthly_interest_rate
P = principal

M = P * ((r * (1 + r)**N) / (((1+r)**N) - 1))

print(f'Monthly Payment(monthly compounding): ${round(M, 2)}')
print(f"It takes {loanterm_in_years} years to pay off the loan.")

weekly_interest_rate = annual_interest_rate / (52 * 100)
monthly_interest_rate = ((1 + weekly_interest_rate) ** 4.33) - 1
r = monthly_interest_rate
M = P * ((r * (1 + r)**N) / (((1+r)**N) - 1))
print(f'\nMonthly Payment (weekly compounding): ${round(M, 2)}')
print(f"It takes {loanterm_in_years} years to pay off the loan.")

daily_interest_rate = annual_interest_rate / (365 * 100)
monthly_interest_rate = ((1 + daily_interest_rate) ** 30) - 1
r = monthly_interest_rate
M = P * ((r * (1 + r)**N) / (((1+r)**N) - 1))
print(f'\nMonthly Payment (daily compounding): ${round(M, 2)}')
print(f"It takes {loanterm_in_years} years to pay off the loan.")
