class Car:

    # Puede ser avaialable, rented, reserved 
    satatus: "available"

    def __init__(self, options):
        self.id = options['id']
        self.color = options['color']
        self.model = options['model']
        self.price = options['price']

    def isAvailable(self):
        if status == "available":
            return True
        else: 
            return False