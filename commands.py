import classes
class AddCommand:
    def __init__(self, productStorage:classes.ProductStorage):
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
    def __str__(self):
        return "Эта функция добавляет товар на склад "
class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        for x in self.productStorage.storage:
            print(x)
    def __str__(self):
        return "Эта функция выводит товары на складе"
class DeleteCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.pop(int(params[0]))
        index = int(params[0])

        if index <= 0 or index >= len(self.productStorage.storage):
            print(f"выйди отсюда розбийнк")
            return
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
        exit()
    def __str__(self):
        return "Эта функция выходит из приложения"
