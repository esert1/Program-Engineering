def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print(f"Содержимое файла '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

def create_test_files():
    with open('Пустой_файл.txt', 'w', encoding='utf-8') as f:
        pass
    
    with open('Файл_с_текстом.txt', 'w', encoding='utf-8') as f:
        f.write("Это тестовый файл с содержимым.\n")
        f.write("Здесь есть несколько строк текста.\n")
        f.write("Файл не пустой и должен быть успешно прочитан.")

if __name__ == '__main__':
    create_test_files()
    print("Тест с пустым файлом:")
    read_file_content('Пустой_файл.txt')
    print("\nТест с файлом, содержащим данные:")
    read_file_content('Файл_с_текстом.txt')
    print("\nТест с несуществующим файлом:")
    read_file_content('Несуществующий_файл.txt')