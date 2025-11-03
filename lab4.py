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