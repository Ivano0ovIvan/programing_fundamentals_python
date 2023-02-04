def rectangle_area_calculator(side_a, side_b):
    rectangle_area = side_a * side_b
    return rectangle_area


width = float(input())
height = float(input())
print(int(rectangle_area_calculator(width, height)))