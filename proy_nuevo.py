

import pyodbc
import pandas as pd

# Configura tu conexión
conexion = pyodbc.connect(
    'DRIVER={IBM INFORMIX ODBC DRIVER (64-bit)};'
    'HOSTNAME=192.168.20.62;'
    'SERVER=ol_serverdev;'
    'SERVICE=1528;'
    'PROTOCOL=olsoctcp;'
    'DATABASE=seguros;'
    'UID=informix;'
    'PWD=DevReplika.25*;',autocommit=True
)





cursor = conexion.cursor()

#CONSULTAR DATOS EXISTENTES
cursor.execute("SELECT * FROM tabla002")
columnas = [column[0] for column in cursor.description]
datos = cursor.fetchall()
df = pd.DataFrame.from_records(datos, columns=columnas)

# INSERTAR EN sw_prueba_resp UNA COLUMNA DE df
insert_sql = """
INSERT INTO sw_prueba_rep (nombre, fecha_actual)
VALUES (?, CURRENT)
"""

for nombre in df['descripcion']:
    cursor.execute(insert_sql, (nombre,))




# Cierra la conexión
conexion.close()

# Muestra el DataFrame en una tabla en Colab
