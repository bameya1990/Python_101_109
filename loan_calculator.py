"""
Calculating the monthly loan amount for a car 
"""



#ask for the loan amount
loan_amount = int(input("What is the loan amount in $?" ))

#ask for the annual percentage rate
annual_rate = float(input("What is the APR %? "))

#ask for the loan duration in years
loan_duration_year = float(input("What is the loan duration in years? "))


#convert APR into monthly rate
monthly_rate = annual_rate / (12*100)

#convert loan duration into months
loan_duration_months = loan_duration_year * 12

#calculate monthly payment
monthly_payment = loan_amount * (monthly_rate/ (1 - (1 + monthly_rate) ** (-loan_duration_months)))

#print monthly payment in $ and cents
print(f'Your monthly payment is $ {monthly_payment:.2f}')
