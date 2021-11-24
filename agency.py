from rent import Rent

class Agency:
    reservationsAccount = 0
    reservations = []
    rentsAccount = 0
    rents = []
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

    def getCars(self):
        return self.cars

    def getCar(self, _id):
        car = None
        for _car in self.cars:
            if  _car.id == _id:
                car = _car
                break
        return car

    def getCarsByStatus(self, status = "available" or "reserved" or "rented"):
        cars = []
        for _car in self.cars:
            if _car.status == status:
                cars.append(_car)
        return cars

    def setCarStatus(self, _id, status = "available" or "reserved" or "rented"):
        updated = False
        for i, _car in enumerate(self.cars):
            if(_car.id == _id):
                self.cars[i].status = status
                updated = True
                break
        return updated

    def getReserves(self):
        return self.reservations

    def getReserve(self, _id):
        reserve = None
        for _reserve in self.reservations:
            if _reserve.id == _id:
                reserve = _reserve
                break
        return reserve

    def createReserve(self, reserve):
        self.setCarStatus(reserve.car.id, "reserved")
        self.reservationsAccount = self.reservationsAccount + 1
        reserve.id = self.reservationsAccount
        self.reservations.append(reserve)

    def removeReserve(self, reserveId):
        removed = False
        for i, _reserve in enumerate(self.reservations):
            if reserveId == _reserve.id:
                self.reservations.remove(self.reservations[i])
                removed = True
                break
        return removed

    def getRents(self):
        return self.rents

    def getRent(self, _id):
        rent = None
        for _rent in self.rents:
            if(_rent.id == _id):
                rent = _rent
                break
        return rent

    def addRent(self, reserveId):
        rent = None
        for i, _reserve in enumerate(self.reservations):
            if(_reserve.id == reserveId):
                rent = Rent(_reserve.car, _reserve.user)
                rent.car.status = "rented"
                self.rentsAccount = self.rentsAccount + 1
                rent.id = self.rentsAccount
                self.setCarStatus(_reserve.car.id, "rented")
                self.removeReserve(reserveId)
                break
        return rent

    def removeRent(self, rentId):
        removed = False
        for i, _rent in enumerate(self.rents):
            if(_rent.id == rentId):
                self.rents.remove(self.rents[i])
                self.setCarStatus(_rent.car.id, "available")
                removed = True
                break
        return removed
