import FachadaPersistencia as fp
from Expediente.models import Expediente

consulta = "SELECT * FROM Expediente_expediente"
resultado = fp.ejecutar_consulta_con_resultado(consulta)

print(resultado)
