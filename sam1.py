class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Автомобиль: {self.brand} {self.model}")


car1 = Car("Toyota", "Camry")
car1.show_info()
