import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения функции: {execution_time:.6f} секунд")
        return result
    return wrapper

@timer_decorator
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()