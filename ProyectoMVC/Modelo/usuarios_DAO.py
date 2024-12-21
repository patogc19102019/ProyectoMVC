from conectorBD import ConectorBD 

class Usuario_DAO:
    
    def __init__(self, conector):
        self.conector = conector

    def busca_user(self, data_DTO):
        user = data_DTO['username']
        password = data_DTO['password']
        
        sql = f"SELECT * FROM usuarios WHERE username = '{user}' AND password = '{password}'"
        code, result = self.conector.ejecutarSelectOne(sql)
        
        if code == 0 and result:
            return True
        else:
            return False
        
    def crea_user(self, data_DTO):
        user = data_DTO['username']
        password = data_DTO['password']
        
        sql = f"INSERT INTO usuarios (username, password) VALUES ('{user}', '{password}')"
        code = self.conector.ejecutarInsert(sql)
        
        if code == 0:
            return True
        else:
            return False

# Ejemplo de uso
if __name__ == "__main__":
    print("Iniciando conexión a la base de datos...")  # Mensaje de depuración
    conector = ConectorBD("localhost", "root", "", "mi_base_de_datos")
    resultado, mensaje = conector.activarConexion()
    if resultado == 0:
        conector.comprobarConexion()
        
        usuario_dao = Usuario_DAO(conector)
        
        # Crear un nuevo usuario
        nuevo_usuario = {'username': 'nuevo_usuario', 'password': 'mi_contraseña'}
        if usuario_dao.crea_user(nuevo_usuario):
            print("Usuario creado exitosamente.")
        else:
            print("El usuario ya existe.")
        
        # Buscar un usuario
        buscar_usuario = {'username': 'nuevo_usuario', 'password': 'mi_contraseña'}
        if usuario_dao.busca_user(buscar_usuario):
            print("Usuario encontrado.")
        else:
            print("Usuario no encontrado.")
    else:
        print(f"Error al conectar: {mensaje}")
