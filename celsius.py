def celesius_fahreheit(celsius):
    fahreheit = (9/5) * celsius + 32
    return f"{celsius} Celsius is {fahreheit:.1f} Fahreheit"

celsius = eval(input("Enter a degree in celsius: "))
print(celesius_fahreheit(celsius))