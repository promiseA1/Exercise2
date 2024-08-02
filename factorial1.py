def program(number):
    result = 1
    while number >= 1:
        print(number)
        print("number is", number)
        result = result * number
        number -= 1
    return result

number = eval(input("Enter a number: "))
print(program(number))