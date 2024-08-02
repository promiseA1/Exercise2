def triangle_area(x1 , y1 , x2 , y2 , x3 , y3):
    area_of_triangle = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return f"{area_of_triangle:.1f}"
    

x1 , y1 = 1.5 , -3.4
x2 , y2 = 4.6 , 5
x3 , y3 = 9.5 , -3.4

print(triangle_area(x1 , y1 , x2 , y2 , x3 , y3))