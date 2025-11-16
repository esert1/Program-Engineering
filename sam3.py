def add_two_to_user_input():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"2 + {number} = {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    print("Тест 1: Ввод корректного числа")
    add_two_to_user_input()
    
    print("\nТест 2: Ввод строки вместо числа")
    add_two_to_user_input()
    
    print("\nТест 3: Ввод другого корректного числа")
    add_two_to_user_input()