class User:
    car = None
    def __init__(self, options):
        self.id = options['id']
        self.username = options['username']
        self.record = options['record']
        self.isAdmin = options['isAdmin']
        self.type = options['type']