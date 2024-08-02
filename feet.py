def feet_to_meters(feet):
    one_foot = 0.305
    feet_to_meters = feet * one_foot
    return f"{feet} feet is {feet_to_meters:.4f} meters"

feet = eval(input("Enter a value for feet: "))
print(feet_to_meters(feet))