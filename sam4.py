def cache_decorator(func):
    """
    Декоратор для кэширования результатов функции.
    Сохраняет результаты вызовов функции и возвращает их при повторных вызовах с теми же аргументами.
    """
    cache = {}
    
    def wrapper(*args):
        # Проверяем, есть ли результат в кэше
        if args in cache:
            print(f"Результат для аргументов {args} взят из кэша")
            return cache[args]
        
        # Если нет в кэше, вычисляем и сохраняем
        result = func(*args)
        cache[args] = result
        print(f"Результат для аргументов {args} вычислен и сохранен в кэш")
        return result
    
    return wrapper

# Первая функция с декоратором - вычисление факториала
@cache_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Вторая функция с декоратором - вычисление суммы квадратов
@cache_decorator
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

if __name__ == '__main__':
    print("=== Тестирование декоратора кэширования ===")
    
    print("\n1. Тест функции factorial:")
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(5) = {factorial(5)}")  # Должен взять из кэша
    print(f"factorial(3) = {factorial(3)}")
    print(f"factorial(5) = {factorial(5)}")  # Снова из кэша
    
    print("\n2. Тест функции sum_of_squares:")
    print(f"sum_of_squares(4) = {sum_of_squares(4)}")
    print(f"sum_of_squares(4) = {sum_of_squares(4)}")  # Должен взять из кэша
    print(f"sum_of_squares(3) = {sum_of_squares(3)}")
    print(f"sum_of_squares(4) = {sum_of_squares(4)}")  # Снова из кэша
