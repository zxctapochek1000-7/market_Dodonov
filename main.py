import classes
import commands
import json

def work():
    productStorage1 = classes.ProductStorage("FioletoviyArbuz", [])

    try:
        with open("storage.json", "r") as storage_file:
            packed_products = json.load(storage_file)
            for product in packed_products:
                productStorage1.storage.append(classes.Product(
                product["name"], product["cost"])
            )
    except json.decoder.JSONDecodeError:
        print("Пустое хранилище")
    prorab = classes.Prorab({
        "add": commands.AddCommand(productStorage1),
        "list": commands.ListCommand(productStorage1),
        "delete": commands.DeleteCommand(productStorage1),
        "quit": commands.QuitCommand()
    })
    prorab.spisok["help"] = commands.HelpCommand(prorab)

    while True:
        command_input = input()
        command_itog = classes.CommandInput(command_input)

        if command_itog.command in prorab.spisok:
            prorab.spisok[command_itog.command].execute(command_itog.params)
        else:
            print("Такой команды нет!")

if __name__ == "__main__":
    work()


