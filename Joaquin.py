#Librerías
import pandas as pd
import numpy as np

# Leer las hojas del archivo Excel
df_tabla1 = pd.read_excel('DatosEjemplo.xlsx', sheet_name='Hoja1')
df_tabla2 = pd.read_excel('DatosEjemplo.xlsx', sheet_name='Hoja2')
df_tabla3 = pd.read_excel('DatosEjemplo.xlsx', sheet_name='Hoja3')

# 1. Agregar columna 'correo' en la tabla 2
df_tabla2['Correo'] = df_tabla2['Representante'].str.split().str[0] + df_tabla2['Representante'].str.split().str[-1] + '@work.com'

# 3. Separar el apellido de la columna 'Representante' y colocarlo en 'Apellido'
df_tabla2['Apellido'] = df_tabla2['Representante'].str.split().str[-1]

# 2. Crear tabla 'tiempo' con todas las fechas de la tabla 1
tiempo = df_tabla1.copy()
tiempo['Fecha'] = pd.to_datetime(tiempo['Fecha'])
tiempo['Número Mes'] = tiempo['Fecha'].dt.day
tiempo['Nombre Mes'] = tiempo['Fecha'].dt.month_name()
tiempo['Número Año'] = tiempo['Fecha'].dt.year

# 4. Generar columnas de precio de venta y costo de producción aleatorios para la tabla 3
np.random.seed(42)
df_tabla3['Precio Venta'] = np.random.randint(500000, 1000000, size=len(df_tabla3))
df_tabla3['Costo Producción'] = np.random.randint(100000, 300000, size=len(df_tabla3))
print(df_tabla3)

# Guardar los DataFrames en un nuevo archivo Excel
with pd.ExcelWriter('Resultados.xlsx') as writer:
    df_tabla1.to_excel(writer, sheet_name='Tabla1', index=False)
    df_tabla2.to_excel(writer, sheet_name='Tabla2', index=False)
    df_tabla3.to_excel(writer, sheet_name='Tabla3', index=False)
    tiempo.to_excel(writer, sheet_name='Tiempo', index=False)