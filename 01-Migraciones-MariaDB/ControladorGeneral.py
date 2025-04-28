# joaquin.soler.1979@gmail.com
# Controlador que coordina todas las actividades de la rutina de migración

import ExpertoCargarDataFrame as ecdf
import ExpertoGuardarDatos as egd

# 1) Cargar datos de los archivos csv a un dataframe
df = ecdf.getDF()

# 2) Guardar el dataframe en la BD
egd.guardarDF(df)
