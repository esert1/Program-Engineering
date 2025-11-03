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
