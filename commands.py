import classes
import json
class AddCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        if len(params) != 2:
            print("Введите 2 параметра")
            return
        if params[0].isdigit():
            print("1 параметр должен быть текстом")
            return
        if not params[1].isdigit():
            print("2 параметр должен быть числом")
            return
        self.productStorage.storage.append(classes.Product(params[0], params[1]))
        with open("storage.json", "w") as storage_file:
            packed_product = []
            for product in self.productStorage.storage:
                packed_product.append(product.__dict__())
            json.dump(packed_product, storage_file)
    def __str__(self):
        return "Эта функция добавляет товар на склад "
class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        if not self.productStorage.storage:
            print("Склад пуст")
            return
        for x in self.productStorage.storage:
            print(x)
    def __str__(self):
        return "Эта функция выводит товары на складе"
class DeleteCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage


    def execute(self, params: []):
        if len(params) != 1 or not params[0].isdigit():
            print("Введите 1 параметр — индекс товара для удаления")
            return
        if len(params) != 1:
            print("нельзя удалять сразу несколько товаров")
            return
        index = int(params[0])

        if index < 0 or index >= len(self.productStorage.storage):
            print("Индекс вне диапозона")
        self.productStorage.storage.pop(int(params[0]))
        with open("storage.json", "w") as storage_file:
            packed_product = []
            for product in self.productStorage.storage:
                packed_product.append(product.__dict__())
            json.dump(packed_product, storage_file)

    def __str__(self):
        return "Эта функция удаляет товар который уже находится на складе"
class HelpCommand:
    def __init__(self, prorab: classes.Prorab):
        self.prorab = prorab
    def execute(self, params: []):
        for x in self.prorab.spisok.keys():
            print(x, self.prorab.spisok[x])
    def __str__(self):
        return "Эта функция выводит все возможные команды"
class QuitCommand:
    def __init__(self):
        pass
    def execute(self,params: []):
        print("Выход из приложения")
        exit()
    def __str__(self):
        return "Эта функция выходит из приложения"