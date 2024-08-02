def program():
    number_list = number_sequence.split(',')
    number_tuple = tuple(number_list)
    print(number_list)
    print(number_tuple)

number_sequence = input("Enter sequence of numbers seperated by comma: ")
(program())