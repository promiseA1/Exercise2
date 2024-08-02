def bmi(weight_in_pounds , height_in_inches):
    one_pound = 0.45359237
    one_inch = 0.0254
    weight_in_kilograms = weight_in_pounds * one_pound
    height_in_meters = height_in_inches * one_inch
    body_mass_index = weight_in_kilograms / (height_in_meters)**2
    return f"BMI is {body_mass_index:.4f}"

weight_in_pounds = eval(input("Enter weight in pounds: "))
height_in_inches = eval(input("Enter height in inches: "))
print(bmi(weight_in_pounds , height_in_inches))