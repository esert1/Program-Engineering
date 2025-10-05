from heron import calculate_heron_area

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

area = calculate_heron_area(a, b, c)
print(f"Площадь треугольника: {area:.2f}")