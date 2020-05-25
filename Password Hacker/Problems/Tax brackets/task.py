income = int(input())
percent = 0
if income < 15528:
    percent = 0
elif income < 42708:
    percent = 15
elif income < 132407:
    percent = 25
else:
    percent = 28

calculated_tax = income * percent / 100

print(f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!')
