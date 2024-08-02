def financial_pay(monthly_saving_amount):
    annual_rate = 5 / 100
    monthly_interest_rate = annual_rate / 12
    total = monthly_saving_amount * (1 + monthly_interest_rate)
    for i in range(2 , 7):
        total = (monthly_saving_amount + total) * (1 + monthly_interest_rate)
    return f"After the sixth month, the account value is {total:.2f}"

monthly_saving_amount = eval(input("Enter the monthly saving amount: "))
print(financial_pay(monthly_saving_amount))