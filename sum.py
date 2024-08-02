def sum_of_digits(number):
    #To check if the value is between the specified range of values
    if 0 <= number < 1000:
        #To extract the digits and sum them
        sum_of_digits = 0

        

        while number > 0:
            extract_digits = number % 10
            sum_of_digits += extract_digits
            number //= 10

            #Display the result

        print(f"The sum of digits is {sum_of_digits}")
    else:
        print(f"Please re-enter a valid integer between 0 and 1000: ")


number = eval(input("Enter a number between 0 and 1000: "))
(sum_of_digits(number))