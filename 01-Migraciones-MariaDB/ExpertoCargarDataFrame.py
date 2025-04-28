# joaquin.soler.1979@gmail.com
# Experto responsable de obtener un gran DataFrame a partir de multiples archivos cvs en multiples subcarpetas

import pandas as pd
import glob

def getDF():
    # carpeta base 
    rutaBase = 'C:/Users/jsoler/Downloads/Python/01-Migraciones-MariaDB/db/'
    # inicialización de la lista que contendrá los dataframes individuales de cada archivo
    dataFrames = []

    # iterador por carpetas desde 1960 hasta 2024
    for i in range (1960, 2025):
        # la ruta definitiva para un archivo específico en una subcarpeta
        rutaFinal = f'{rutaBase}{i}/merged_movies_data_{i}.csv'
        # agregar el dataframe específico a la lista
        dataFrames.append(pd.read_csv(rutaFinal))

    # se concatenan todos los dataframes que estaban en la lista
    granDF = pd.concat(dataFrames, ignore_index = True)    

    return granDF