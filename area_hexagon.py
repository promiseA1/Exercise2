from math import sqrt
def area_of_a_hexagon(side):
    area = (3 * sqrt(3)) / 2 * (side)**2
    return f"The area of the hexagon is {area:.4f}"

side = eval(input("Enter the side: "))
print(area_of_a_hexagon(side))