# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
- Логинов Андрей Владимирович
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- Ассистент кафедры информационных технологий и статистики, Ротенштрайх Татьяна Викторовна.

## Лабораторная работа №1
### Создайте текстовый файл и поместите его в одну директорию с программой на Python. Текстовый файл должен содержать минимум из двух строк.

``` input.txt
Hello students!
Lets talk about work with files on Python
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034429.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

``` input.txt
Hello students!
Lets talk about work with files on Python
```

```python
f = open ('input.txt', 'r')
print(f.readline())
f.close()

```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034441.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

``` input.txt
Hello students!
Lets talk about work with files on Python
```

```python
f = open ('input.txt', 'r')
print(f.readlines())
f.close()

```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034452.png)
  
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

input.txt
```
Hello students!
Lets talk about work with files on Python
```

```python
with open('input.txt', 'r') as f:
    print(f.readlines())
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034500.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

``` input.txt
Hello students!
Lets talk about work with files on Python
```

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034505.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

``` input_1.txt
Hello students!
Lets talk about work with files on Python
Im additional line
```

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034524.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить, что измененная вами информация сохранилась в файле.

``` input_2.txt
Cycle run one
Cycle run two
Cycle run three
```

```python
lines = ['one', 'two', 'three']
with open('input_2.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run '+line)
    print('Done!')
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034645.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-'*48)

print_docs('/Enginering/2')
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034718.png)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:

Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.

Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

``` input_3.txt
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днём рождения!
Удача!
Я тебя люблю.
```

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
    
print(longest_words('input_3.txt'))
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034725.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах.

Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv 
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1,301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20034859.png)

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово.
Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

``` article.txt
С недавнего времени программирование на языке Python введено
в учебные планы подготовки специалистов многих направлений. 
Это обусловлено тем, что язык программирования Python имеет широкий 
набор возможностей для применения в разных аспектах (например, удобен 
при веб-разработках, анализе данных, написании скриптов и игр). 
Исходя из анализа практической деятельности, можем определить, 
что такой набор его возможностей нечасто нужен специалистам конкретной области. 
Отсюда возникает необходимость выбора приоритета при изучении языка 
программирования Python. Цель исследования изучить особенности программирования 
на языке Python при формировании цифровой компетентности студентов. 
Научная новизна: обосновывается необходимость выбора приоритетного 
направления обучения программированию на языке Python для студентов 
разных направлений подготовки. Теоретическая и практическая значимость 
заключается в выявлении возможности и особенностей программирования на 
языке Python при формировании цифровой компетентности студентов разных 
направлений подготовки. В представленной статье обобщен опыт и описаны 
результаты практического исследования, направленного на обоснование 
особенностей обучения программированию на языке Python студентов разных 
направлений подготовки. В качестве результатов контрольной группы приводятся 
критерии сформированное™ цифровой компетенции студентов, которые обучались 
программированию в 2020/2021 и в 2021/2022 учебных годах. В качестве результатов 
экспериментальной группы рассматриваются критерии сформированное™ цифровой 
компетенции студентов, которые обучались программированию в 2022/2023 и 
в 2023/2024 учебных годах. Проведенное исследование подтвердило, что преподавание 
программирования для студентов разных направлений подготовки методом выбора 
приоритетного направления применения языка Python является эффективным средством 
формирования их цифровой компетенции. В качестве критериев эффективности 
формирования цифровой компетенции студентов рассмотрены показатели 
общекультурной, общепрофессиональной и профессиональной компетенций. 
Эффективность выбора приоритетного направления программирования на языке 
Python экспериментально подтверждена повышением у студентов экспериментальной 
группы таких профессиональный показателей цифровой компетенции студентов, как 
способность применять теоретические знания и методы программирования при работе 
с нестандартными задачи профессиональной деятельности; способность отбирать и 
использовать методы комплексного решения профессиональных задач, которые имеют 
стандартные условия реализации; способность работать с HTML-страницами.
```

```python
import re
from collections import Counter

def analyze_article():
    with open('article.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    most_common_word, frequency = Counter(words).most_common(1)[0]
    
    print(f"Общее количество слов: {word_count}")
    print(f"Самое частое слово: '{most_common_word}' (встречается {frequency} раз)")

analyze_article()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20035733.png)

## Выводы
Программа эффективно обрабатывает текст, показывая основные операции с файлами и методы работы со строками. Применение Counter облегчает подсчет частоты слов.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходам, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
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
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20035907.png)

## Выводы
Программа интерактивно обрабатывает данные, записывая их в файл. Это демонстрирует применение файлового ввода/вывода для сохранения состояния между запусками.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

- Текст в файле:
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.

- Ожидаемый результат:
  Input file contains:
   108 letters
   20 words
   4 lines

``` input_4.txt
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
```

```python
def text_statistics():
    with open('input_4.txt', 'r') as file:
        lines = file.readlines()
    
    letter_count = 0
    word_count = 0
    
    for line in lines:
        letter_count += sum(c.isalpha() for c in line)
        word_count += len(line.split())
    
    print(f"Input file contains:\n{letter_count} letters\n{word_count} words\n{len(lines)} lines")

text_statistics()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20035918.png)

## Выводы
Программа успешно применяет строковые методы для анализа текста, подсчитывая символы, слова и строки. Результаты соответствуют ожиданиям.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exam должны быть заменены на ****.  

- Запрещенные слова:  
  hello email python the exam wor is  
- Предложение для проверки:  
  Hello, world! Python IS the programming language of thE future. My  
  EMAIL is....  
  PYTHON is awesome!!!!  
- Ожидаемый результат:  
  ***** **id! ****** ** programming language of *** future. My  
  ****** **...  
  ****** ** awesome!!!!

```python
import re

def filter_text():
    with open('forbidden.txt', 'r') as file:
        forbidden_words = file.read().split()
    
    text = "Hello, world! Python is the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    print("Исходный текст:")
    print(text)
    
    for word in forbidden_words:
        text = re.sub(rf'\b{re.escape(word)}\b', '*' * len(word), text, flags=re.IGNORECASE)
    
    print("\nОтфильтрованный текст:")
    print(text)

filter_text()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_7/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-27%20035930.png)

## Выводы
Решение иллюстрирует использование регулярных выражений для интенсивной обработки текста. Учет регистра и границ слов гарантирует точность фильтрации.
  
