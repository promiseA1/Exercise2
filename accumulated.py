def financial_accumulated_value(investment_amount , annual_interest_rate , number_of_years):
    number_of_months = 12
    monthly_interest_rate = annual_interest_rate / 1200
    future_investment_value = investment_amount * (1 + monthly_interest_rate)**number_of_months
    return f"Accumulated value is {future_investment_value:.2f}"

investment_amount = eval(input("Enter investment amount: "))
annual_interest_rate = eval(input("Enter annual interest rate: "))
number_of_years = eval(input("Enter number of years: "))
print(financial_accumulated_value(investment_amount , annual_interest_rate , number_of_years))