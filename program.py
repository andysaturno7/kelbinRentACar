from db import db
from agency import Agency
from car import Car
from authentication import Authentication

# Leemos carros de la base de datos e inicalizamos nuestra instncia de agencia con ellos
cars = []
for _car in db['cars']:
    cars.append(Car(_car))

# Creamos instancia global de Agencia
agency = Agency("Super Agencia de Kelbin", cars)

# Pintamos Bienvenida
print(f"Bienvenidos a {agency.name}")

def login():
    print("Porfavor identificate")
    username = input("username: ")
    password = input("password: ")
    return {
        'username': username,
        'password': password
    }

def authenticate(log):
    user = Authentication().signIn(log['username'], log['password'])
    if(user != False):
        return user
    print("Error de autenticacion")
    return authenticate(login())

# Nos identificamos como usuario
user = authenticate(login())

print(user.isAdmin)

if(user.isAdmin):
    # Aplicar logica para administrador
    print("Usuario Administrador")
else:
    # Aplicar logica para cliente
    print("Usuario Cliente")