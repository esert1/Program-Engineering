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
