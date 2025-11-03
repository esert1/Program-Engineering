# Тема 8. Работа с файлами (ввод, вывод)
Отчет по Теме #8 выполнил:
- Логинов Андрей Владимирович
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- Ассистент кафедры информационных технологий и статистики, Ротенштрайх Татьяна Викторовна.

## Лабораторная работа №1
### Создайте класс "Car" с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052347.png)

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину "поехать". Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.drive()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052401.png)

## Лабораторная работа №3
### Создайте новый класс "ElectricCar" с методом "charge" и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
from lab2 import Car


class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} witn {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052412.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make # Защищённый атрибут
        self.__model = model # Приватный атрибут

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make) #Доступ к защищённому атрибуту
# print(my_car._make) # Ошибка! Приватный атрибут недоступен
my_car.drive()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052423.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс "Shape", а также еще два класса "Rectangle" и "Circle". Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius 
    
shapes = []

shapes.append(Rectangle(4, 5)) 
shapes.append(Circle(3))

for shape in shapes:
    print(shape.area())
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052432.png)

## Самостоятельная работа по Python

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться от тех, что указаны в теоретическом материале и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Автомобиль: {self.brand} {self.model}")


car1 = Car("Toyota", "Camry")
car1.show_info()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052442.png)

## Выводы
Создан класс Car для моделирования автомобиля. Объект car1 инициализирован с брендом "Toyota" и моделью "Camry". Класс отличается от примеров в теории и лабораторных работах.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться от тех, что указаны в теоретическом материале и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def show_info(self):
        print(f"{self.brand} {self.model}, {self.year} года, цвет: {self.color}")

    def repaint(self, new_color):
        self.color = new_color
        print(f"Машина перекрашена в {self.color}")

car2 = Car("Honda", "Civic", 2020, "синий")
car2.show_info()
car2.repaint("красный")
car2.show_info()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052517.png)

## Выводы
Введены атрибуты year и color, а также метод repaint() для изменения цвета. Класс расширен характеристиками автомобиля, отличающимися от исходных примеров.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться от того, что указано в теоретическом материале и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
from sam2 import Car


class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Батарея заряжена на {self.battery_capacity} кВт")

ecar = ElectricCar("Tesla", "Model 3", 2023, "белый", 75)
ecar.show_info()
ecar.charge()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052524.png)

## Выводы
Разработан класс ElectricCar, наследующий от Car. Добавлен атрибут battery_capacity и метод charge(). Структура наследования отличается от лабораторных примеров.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться от того, что указано в теоретическом материале и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CarSecure:
    def __init__(self, brand, model, pin_code):
        self.brand = brand
        self.model = model
        self.__pin_code = pin_code  # закрытый атрибут

    def unlock(self, code):
        if code == self.__pin_code:
            print(f"{self.brand} {self.model} — доступ разрешен.")
        else:
            print("Неверный PIN-код! Доступ запрещен.")

# Проверка
secure_car = CarSecure("BMW", "X5", "1234")
secure_car.unlock("0000")
secure_car.unlock("1234")
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052531.png)

## Выводы
Инкапсуляция реализована с приватным атрибутом __pin_code. Доступ предоставляется через метод unlock(). Подход отличается от лабораторных заданий.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться от того, что указано в теоретическом материале и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def speak(self):
        print("Животное издает звук")

class Dog(Animal):
    def speak(self):
        print("Собака лает")

class Cat(Animal):
    def speak(self):
        print("Кошка мяукает")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()
```

### Результат.
![](https://github.com/esert1/Program-Engineering/blob/Theme_8/pic/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-11-03%20052543.png)

## Выводы
Полиморфизм продемонстрирован на животных. Цикл вызывает speak() для объектов Dog, Cat и Animal с общим интерфейсом. Отличается от геометрических фигур в лабораторной.

## Общий вывод

В работе освоены принципы ООП в Python.
Освоенные аспекты:

- Классы и объекты: Формирование классов, конструкторов и экземпляров.
- Методы: Интеграция функционала в классы.
- Наследование: Построение иерархий с использованием super().
- Инкапсуляция: Регулировка доступа к атрибутам (_ и __).
- Полиморфизм: Общий интерфейс для разнообразных объектов.

Работа подтверждает способность применять концепции ООП для создания модульного кода в различных областях.
