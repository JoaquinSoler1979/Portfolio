#joaquin.soler.1979@gmail.com
#Interfaz entre el sistema y el DBMS (MariaDB)

import mariadb, time

# Variables generales
latencia = 0.005
ruta = 'C:/Users/jsoler/Downloads/Python/01-Migraciones-MariaDB/logs.txt'

def ejecutarConsultaSinResultado(consulta):
    
    conexion = getConexion()
    cursor = conexion.cursor()

    try:        
        cursor.execute(consulta)

    except BaseException as dbe:
        ecribirLog(dbe, consulta)

    except mariadb.ProgrammingError as mdbPE:
        ecribirLog(mdbPE, consulta)

    conexion.commit()
    conexion.close()
    time.sleep(latencia)
    
def ejecutarConsultaConResultado(consulta):
    conexion = getConexion()
    cursor = conexion.cursor()
    resultado = 0

    try:   
        cursor.execute(consulta)
        resultado = cursor.fetchall()
    except BaseException as dbe:
        ecribirLog(dbe, consulta)
    except mariadb.ProgrammingError as mdbPE:
        ecribirLog(mdbPE, consulta)

    conexion.commit()
    conexion.close()
    return resultado

def getConexion():
    return mariadb.connect(
        host="localhost",
        port = 3306,
        database = "db",
        user="root",
        password="root")

def ecribirLog(exepcion, consulta):
    
    archivo = 0

    try:
        archivo = open(ruta, "x")
    except:
        archivo = open(ruta, "a")

    archivo.write(f"{str(exepcion)}\n")
    archivo.write("====Consulta====\n")
    archivo.write(f"{consulta}\n")
    archivo.close()
