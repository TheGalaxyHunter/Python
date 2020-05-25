def final_deposit_amount(*args, amount):
    for n in args:
        amount *= (1 + (n / 100))
    return round(amount, 2)
