class UserDTO():
    name: str
    lastname: str
    phone: str
    email: str
    password: str

    def __init__(self, nombre, lastname, phone, email, password):
        self.name = nombre
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.password = password