def pounds_to_kilograms(pounds):
    one_pound = 0.454
    pounds_to_kilograms = pounds * one_pound
    return f"{pounds} pounds is {pounds_to_kilograms:.3f} kilograms"

pounds = eval(input("Enter a value in pounds: "))
print(pounds_to_kilograms(pounds))