.def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_200 = None
for i, value in enumerate(fib(200), start=1):
    if i == 200:
        fib_200 = value
        break

print("200-е число Фибоначчи:", fib_200)