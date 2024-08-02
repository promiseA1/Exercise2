def investment_amount(final_account_value , annual_interest_rate_in_percent , number_of_years):
    number_of_months = 12 * number_of_years
    monthly_interest_rate = annual_interest_rate_in_percent / 1200
    initial_deposit_amount = final_account_value / (1 + monthly_interest_rate)**number_of_months
    return f"initial deposit value is {initial_deposit_amount}"

final_account_value = eval(input("Enter final account value: "))
annual_interest_rate_in_percent = eval(input("Enter annual interest rate in percent: "))
number_of_years = eval(input("Enter number of years: "))
print(investment_amount(final_account_value , annual_interest_rate_in_percent , number_of_years))