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
