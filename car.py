class Car:
    def __init__(self, options):
        self.id = options['id']
        self.color = options['color']
        self.model = options['model']
        self.price = options['price']
        # Puede ser avaialable, rented, reserved
        self.status = "available"

    def isAvailable(self):
        if self.status == "available":
            return True
        else: 
            return False