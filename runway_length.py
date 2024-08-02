def minimum_runway_length(speed , acceleration):
    v = speed
    a = acceleration
    length = (v)**2 / (2 * a)
    return f"The minimum runway length for this airplane is {length:.3f} meters"

speed , acceleration = eval(input("Enter speed and acceleration:  "))
print(minimum_runway_length(speed , acceleration))