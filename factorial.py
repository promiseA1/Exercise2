"""def factorial(number):
    result = number
    while number >= 2:
        print("number is", number)
        print("number -1 is",number - 1)
        print(number - 1)
        result = (number - 1) *  result 
        number -= 1
    return f"{result}"



print(factorial(8))"""

def factorial(number):
    result = 1
    while number >= 1:
        print(number)
        print("number is ", number)
        result = result * number
        number -= 1
    return result


number = eval(input("Enter a number: "))
print(factorial(number))