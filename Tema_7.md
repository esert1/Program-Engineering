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
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
```

### Результат.
![]()

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

``` input.txt
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
```

```python
f = open ('input.txt', 'r')
print(f.readline())
f.close()

```
### Результат.
![](pic/lab2.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

``` input.txt
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
```

```python
f = open ('input.txt', 'r')
print(f.readlines())
f.close()

```
### Результат.
![](pic/lab3.png)
  
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

input.txt
```
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
```

```python
with open('input.txt', 'r') as f:
    print(f.readlines())
```

### Результат.
![](pic/lab4.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

``` input.txt
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
```

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![](pic/lab5.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

``` input_1.txt
Hello Volvo!
Give DIRETIDE ༼ つ ◕_◕ ༽つ
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
![](pic/lab6.png)

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
![](pic/lab7.png)

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
![](pic/lab8.png)

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
![](pic/lab9.png)

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
![](pic/lab10.png)
