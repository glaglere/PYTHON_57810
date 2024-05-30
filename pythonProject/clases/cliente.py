import bcrypt


class Cliente:
    def __init__(self, nombre, apellido, email, telefono, username, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "username": self.username,
            "password": self.password,
            "tipo": self.__class__.__name__
        }

    @staticmethod
    def from_dict(data):
        return Cliente(data["nombre"], data["apellido"], data["email"], data["telefono"], data["username"], data["password"])

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}, Usuario: {self.username}"


class ClienteRegular(Cliente):
    def __init__(self, nombre, apellido, email, telefono, username, password, frecuencia_compra):
        super().__init__(nombre, apellido, email, telefono, username, password)
        self.frecuencia_compra = frecuencia_compra

    def to_dict(self):
        data = super().to_dict()
        data["frecuencia_compra"] = self.frecuencia_compra
        return data

    @staticmethod
    def from_dict(data):
        return ClienteRegular(data["nombre"], data["apellido"], data["email"], data["telefono"], data["username"], data["password"], data["frecuencia_compra"])

    def __str__(self):
        return f"{super().__str__()}, Frecuencia de Compra: {self.frecuencia_compra} veces por mes"


class ClienteVIP(Cliente):
    def __init__(self, nombre, apellido, email, telefono, username, password, descuento, puntos):
        super().__init__(nombre, apellido, email, telefono, username, password)
        self.descuento = descuento
        self.puntos = puntos

    def to_dict(self):
        data = super().to_dict()
        data["descuento"] = self.descuento
        data["puntos"] = self.puntos
        return data

    @staticmethod
    def from_dict(data):
        return ClienteVIP(data["nombre"], data["apellido"], data["email"], data["telefono"], data["username"], data["password"], data["descuento"], data["puntos"])

    def __str__(self):
        return f"{super().__str__()}, Descuento: {self.descuento}%, Puntos: {self.puntos}"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, apellido, email, telefono, username, password, empresa, descuento_corporativo):
        super().__init__(nombre, apellido, email, telefono, username, password)
        self.empresa = empresa
        self.descuento_corporativo = descuento_corporativo

    def to_dict(self):
        data = super().to_dict()
        data["empresa"] = self.empresa
        data["descuento_corporativo"] = self.descuento_corporativo
        return data

    @staticmethod
    def from_dict(data):
        return ClienteCorporativo(data["nombre"], data["apellido"], data["email"], data["telefono"], data["username"], data["password"], data["empresa"], data["descuento_corporativo"])

    def __str__(self):
        return f"{super().__str__()}, Empresa: {self.empresa}, Descuento Corporativo: {self.descuento_corporativo}%"
