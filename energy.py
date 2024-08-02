def energy(amount_of_water , initial_temperature , final_temperature):
    M = amount_of_water
    Q = M * (final_temperature - initial_temperature) * 4184
    return f"The energy needed is {Q:.1f}"

amount_of_water = eval(input("Enter the amount of water in kilograms: "))
initial_temperature = eval(input("Enter the initial temperature: "))
final_temperature = eval(input("Enter the final temperature: "))
print(energy(amount_of_water , initial_temperature , final_temperature))