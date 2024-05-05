class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña


usuario1 = Usuario("ABDELLAH", "contraseña198")


print("Nombre de usuario:", usuario1.nombre_usuario)
print("Contraseña:", usuario1.contraseña)
