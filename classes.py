class Product:
    def __init__(self, name: str, cost: float):
        self.name = name
        self.cost = cost

    def __str__(self):
        return self.name + " по цене(за кг): " + str(self.cost) + "р."

    def __dict__(self):    return {
        "name": self.name, "cost": self.cost
    }

class CommandInput:
    def __init__(self, command_str: str):
        command_split = command_str.split(" ")

        self.command = command_split[0]
        self.params = command_split[1:]


class Prorab:
    def __init__(self, spisok: {}):
        self.spisok = spisok


class ProductStorage:
    def __init__(self, name: str, storage: [Product]):
        self.name = name
        self.storage = storage