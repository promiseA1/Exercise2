def interest_rate_of_year(balance , interest_rate):
    annual_interest_rate = interest_rate
    interest = balance * (annual_interest_rate / 1200)
    return f"The interest is {interest:.5f}"

balance , interest_rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
print(interest_rate_of_year(balance , interest_rate))