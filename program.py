from db import db
from agency import agency
from car import Car
from authentication import Authentication
from menu import Menu, Item
from menus import Menus
from config import config

# Pintamos Bienvenida
print(config["saludo"](agency.name))

# Nos identificamos como usuario
user = None
menu = None

def authenticate():
    print("Porfavor identificate")
    username = input("username: ")
    password = input("password: ")
    user = Authentication().signIn(username, password)
    if(user != False):
        return user
    print("Error de autenticacion")
    return authenticate()

def logUser():
    global user, menu
    user = authenticate()
    menu = getMenus()[0]
    Menu.render(menu)

# definimos el tipo de menu que vamos a utlizar
def getMenus():
    global user
    return Menus(user, {
        # Podemos definir items por defecto que esten presentes en los menus principales
        "defaults": [
            Item("logout", lambda: logUser()),
            Item("exit", lambda: exit()),
        ]
    })

logUser()