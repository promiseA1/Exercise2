def sum_of_digits(number):
    sum = 0
    for i in number:
        sum  += int(i)
    return sum

number = input('enter a number: ')
print(sum_of_digits(number))