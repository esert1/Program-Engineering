class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(f"Помидор {self._index} перешел в стадию: {self.states[self._state]}")
        else:
            print(f"Помидор {self._index} уже полностью созрел!")

    def is_ripe(self):
        return self._state == 3

    def get_state(self):
        return self.states[self._state]

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(1, num_tomatoes + 1)]

    def grow_all(self):
        print("Всем помидоркам +1 к созреванию")
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        print("Урожай собран!!!")
        self.tomatoes = []

    def get_tomatoes_info(self):
        if not self.tomatoes:
            print("На кусте нет томатов.")
            return
        print("Информация о томатах на кусте:")
        for tomato in self.tomatoes:
            print(f"Помидор {tomato._index}: {tomato.get_state()}")

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растениями...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не созрели! Нужно продолжать ухаживать.")
            return False

    @staticmethod
    def knowledge_base():
        print("СПРАВКА ПО САДОВОДСТВУ")
        print("Стадии созревания томата:")
        for key, value in Tomato.states.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    Gardener.knowledge_base()
    print()

    print("Создаем куст с 3 помидорами")
    tomato_bush = TomatoBush(3)

    print("Нанимаем садовника Михаила")
    gardener = Gardener("Михаил", tomato_bush)
    print()

    gardener.work()
    tomato_bush.get_tomatoes_info()
    print()

    print("Попытка сбора урожая, получиться ли?")
    gardener.harvest()
    print()

    gardener.work()
    gardener.work()
    gardener.work()

    success = gardener.harvest()

    if success:
        print("Урожай успешно собран!")
    else:
        print("Что-то пошло не так...")

    tomato_bush.get_tomatoes_info()