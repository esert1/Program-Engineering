def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


filename = "fib.txt"

with open(filename, "w", encoding="utf-8") as file:
    for num in fib(200):
        file.write(str(num) + "\n")

print(f"Файл '{filename}' успешно создан и заполнен 200 числами Фибоначчи.")
