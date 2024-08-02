def square_dictionary():
    square_dict = {i:i * i for i in range(1 , n + 1)}
    return(square_dict)

def square_dictionary2():
    square_dict = dict()
    for i in range(1, n+1):
        square_dict[i] = i * i
    return(square_dict)


n = int(input("Enter an integer: "))
print(square_dictionary2())