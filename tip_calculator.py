bill = int(input('What is the bill? '))
tip_percentage = int(input('What is the tip percentage? '))

tip = (tip_percentage / 100) * bill
total_bill = bill + tip 


print(f'The tip is {tip: .2f}')
print(f'The total is {total_bill: .2f}')