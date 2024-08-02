def average_acceleration(v0 , v1 , t):
    a = (v1 - v0) / t
    return f"The average acceleration is {a:.4f}"
v0 , v1 , t = eval(input("Enter v0 , v1,  and t:  "))
print(average_acceleration(v0 , v1 , t))