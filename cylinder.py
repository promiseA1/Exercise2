from math import pi
def volume_of_a_cylinder(radius , length):
    area = radius * radius * pi
    volume = area * length

    print(f"The area is {area:.4f}")
    print(f"The volume is {volume:.1f}")

radius , length = eval(input("Enter the radius and length of a cylinder: "))
(volume_of_a_cylinder(radius  ,  length))