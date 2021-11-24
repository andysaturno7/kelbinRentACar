class User:
    car = None
    def __init__(self, options):
        self.id = options['id']
        self.username = options['username']
        self.record = options['record']
        self.isAdmin = options['isAdmin']

user = User({"username": "cud", "id": 1, "record": "good", "isAdmin": False})

print(user.isAdmin)