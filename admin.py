class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def login(self):
        if self.username == "admin" and self.password == "1234":
            return True
        else:
            return False
