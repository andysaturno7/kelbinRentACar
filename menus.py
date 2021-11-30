from menu import Menu, Item
from agency import agency
from db import db
from car import Car
from reserve import Reserve
from utilities import Utilities

activeUser = None

def Menus(user, options = {"defaults": []}):
    global activeUser
    activeUser = user
    # Definimos los menus, el primero de la lista siempre es el que inicia el programa
    menus = {
        "Administrator":[
            Menu("Menu Principal", [
                Item("CRUD Carros", lambda: pointMenu(1, 0)),
                Item("CRUD Reservas", lambda: pointMenu(2, 0)),
                Item("CRUD Rentas", printRents),
                Item("listar usuarios", printUsers),
            ] + options['defaults']),
            Menu("CRUD Cars", [
                Item("ver carros", printCars),
                Item("ver carros disponibles", lambda: printCars("available")),
                Item("ver carros reservados", lambda: printCars("reserved")),
                Item("ver carros rentados", lambda: printCars("rented")),
                Item("agregar carro", addCar)
            ] + options["defaults"]),
            Menu("Menu de Reservas", [
                Item("listar reservas", printReserves),
            ] + options['defaults'])
        ],
        "Customer":[
            Menu("Menu Principal", [
                Item("reservas", lambda: pointMenu(1, 0)),
            ] + options['defaults']
            ),
            Menu("Menu de Reservas", [
                Item("reservar", addReserve)
            ] + options['defaults'])
        ]
    }
    def pointMenu(_to, _from = None):
        # global activeUser
        menu = menus[activeUser.type][_to]
        if(_from != None):
            menu = menu.setPrevMenu(menus[activeUser.type][_from])
        Menu.render(menu)

    return menus[user.type]




# Metodos menu de carros

def printCars(status = None):
    cars = None
    if(status != None):
        cars = agency.getCarsByStatus(status)
    else:
        cars = agency.getCars()
    if(len(cars) == 0):
        return print("No tienes carros en esta lista.")
    for item in cars:
        print(f"{item.id} {item.color} {item.model} {item.price} {item.status}\n")
    return cars

def addCar():
    color = input("color: ")
    modelo = input("modelo: ")
    precio = input("precio: ")
    newcar = agency.addCar({"color": color, "model": modelo, "price": precio})
    print("Agregado satisfactoriamente carro modelo" + modelo)

# Metodos menu de reservas

def printReserves():
    reserves = agency.getReserves()
    if(len(reserves) == 0):
        return print("\nNo tienes reservas")
    for item in reserves:
        print(f"{item.car.model} - {item.user.username}")

def addReserve():
    global activeUser
    cars = printCars("available")
    choice = input("Escoge un carro por su id: ")
    if(choice == "cancel" or choice == "c"): return print("Reserva Cancelada")
    if(Utilities.RepresentsInt(choice)):
        choice = int(choice) - 1
        if(choice < len(cars)):
            agency.createReserve(Reserve(activeUser, cars[choice]))
        else:
            print("Opcion no disponible")     
            addReserve()   
    else:
        print("Formato inadecuado")
        addReserve()

# Metodos menu de renta

def printRents():
    rents = agency.getRents()
    if(len(rents) == 0):
        return print("\nNo tienes carros rentados.")
    for item in rents:
        print(f"{item.car.id} {item.car.color} {item.car.model} {item.car.status} {item.user.username}\n")

def printUsers():
    users = db["users"]
    print("\n")
    for user in users:
        username = user["username"]
        usertype = user["type"]
        record = user["record"]
        print(f"{username} {usertype} {record}\n")