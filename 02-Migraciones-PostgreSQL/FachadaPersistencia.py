#joaquin.soler.1979@gmail.com
# Interfaz entre el sistema y la base de datos

import mariadb

def ejecutarConsultaSinResultado(consulta):
    conexion = getConexion()

    cursor = conexion.cursor()    
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()

def ejecutarConsultaConResultado(consulta):

    conexion = getConexion()

    cursor = conexion.cursor()
    resultado = cursor.execute(consulta)
    conexion.commit()
    conexion.close()

    return resultado

def getConexion():

    return mariadb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'dummypass',
            database = 'db'
    )