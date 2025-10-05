def calculate_average(*args):
    return sum(args) / len(args) if args else 0

if __name__ == '__main__':
    result = calculate_average(10, 20, 30, 40, 50)
    print(f"Среднее арифметическое: {result}")