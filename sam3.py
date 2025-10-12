import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_a = min(one)
min_b = min(two)
min_c = min(three)

max_a = max(one)
max_b = max(two)
max_c = max(three)

min_triangle_area = triangle_area(min_a, min_b, min_c)
max_triangle_area = triangle_area(max_a, max_b, max_c)

print(f"Минимальные элементы: {min_a}, {min_b}, {min_c}")
print(f"Максимальные элементы: {max_a}, {max_b}, {max_c}")
print(f"Площадь треугольника из минимальных элементов: {min_triangle_area:.2f}")
print(f"Площадь треугольника из максимальных элементов: {max_triangle_area:.2f}")