from utilities import Utilities

class Menu:
    items = []
    def __init__(self, title, items, prevMenu = None):
        self.title = title
        self.items = items
        self.prevMenu = prevMenu

    def setPrevMenu(self, menu):
        self.prevMenu = menu
        return self

    @staticmethod
    def render(menu):
        if(menu.title):
            print("\n" + menu.title)
        print("\nindex - Acción")
        for i, item in enumerate(menu.items):
            print(f"{i}     - {item.label}")
        if(menu.prevMenu != None):
            print(f"{len(menu.items)}     - atrás")
        print("\n")

        choice = input("Escribe el index de la accion que deseas: ")
        if(Utilities.RepresentsInt(choice)):
            choice = int(choice)
            if(choice < len(menu.items) or choice < len(menu.items) + 1 and menu.prevMenu):
                if(choice == len(menu.items)):
                    return Menu.render(menu.prevMenu)
                item = menu.items[choice]
                item.execute()
                return Menu.render(Menu("", [], menu))
            else:
                print("Opción no disponible")
                return Menu.render(menu)
        else:
            print("Formato no adecuado")
            return Menu.render(menu)

    @staticmethod
    def RepresentsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

class Item:
    def __init__(self, label, action):
        self.label = label
        self.__action = action

    def execute(self):
        self.__action()