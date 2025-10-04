# Тема 4. Функции и модули
Отчет по Теме #4 выполнил:
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
### Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя «точку входа».

```python
def main():
    print(2+2)

if __name__ == '__main__':
    main()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045511.png)
## Лабораторная работа №2
### Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя «точку входа».

```python
def main():
    result = 2+2
    return result

if __name__ == '__main__':
    answer = main()
    print(answer)
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045536.png)

## Лабораторная работа №3
### Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле.

```python
def main(one, two):
    return one+two

for i in range(5):
    answer = main(one=1, two=10)
    print(answer)
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045550.png)
  
## Лабораторная работа №4
### Напишите функцию, на вход которой подается какое-то изначально неизвестное количество аргументов, над которыми будет производиться арифметические действия. Для выполнения задания необходимо использовать кортеж «*args».

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0 , 1, 2, -1 , 0, -1, 1, 2)
    print(f"\nresult={result}")
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045558.png)

## Лабораторная работа №5
### Напишите функцию, которая на вход получает кортеж «**kwargs» и при помощи цикла выводит значения, поступившие в функцию.

```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    
    print()

    for key in kwargs:
        print(f"{key}={kwargs[key]}")

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3,3,0])
    print()
    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045620.png)

## Лабораторная работа №6
### Напишите две функции. Первая – получает в виде параметра «**kwargs». Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя «точку входа» и минимум 4 аргумента.

```python
def main(**kwargs):
    
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])  
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045630.png)

## Лабораторная работа №7
### Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи «точки входа» вызовите эту функцию.

```python
from import7 import say_hello

if __name__ == '__main__':
        say_hello()
```

Файл import7.py
```python
def say_hello():
    print('Hello students!')
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045705.png)

## Лабораторная работа №8
### Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.

```python
from math import *

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045730.png)

## Лабораторная работа №9
### Напишите программу, которая будет рассчитывать какой день будет через n-ное количество дней, которое укажет пользователь.

```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели -  {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today +td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели -  {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20050559.png)

## Лабораторная работа №10
### Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади необходимой фигуры.

```python
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a*b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 *a*h

figure = input('1-прямоугольник, 2-треугольник: ')

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```
### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_4/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-04%20045916.png)
