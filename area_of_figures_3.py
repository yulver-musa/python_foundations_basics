from math import pi

figure = input()

if figure == 'square':
    side_a = float(input())
    area_of_square = side_a * side_a
    print(f'{area_of_square:.3f}')

elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area_of_rectangle = side_a * side_b
    print(f'{area_of_rectangle:.3f}')

elif figure == 'circle':
    radius = float(input())
    area_of_circle = pi * (radius * radius)
    print(f'{area_of_circle:.3f}')

elif figure == 'triangle':
    side_a = float(input())
    side_b = float(input())
    area_of_triangle = (side_a * side_b) / 2
    print(f'{area_of_triangle:.3f}')
