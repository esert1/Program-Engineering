def expense_tracker():
    while True:
        print("\n1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            category = input("Категория расхода: ")
            amount = input("Сумма: ")
            with open('expenses.txt', 'a', encoding='utf-8') as file:
                file.write(f"{category}: {amount}\n")
        elif choice == '2':
            try:
                with open('expenses.txt', 'r', encoding='utf-8') as file:
                    print("\nИстория расходов:")
                    print(file.read())
            except FileNotFoundError:
                print("Файл с расходами пуст.")
        elif choice == '3':
            break
        else:
            print("Неверный ввод")

expense_tracker()