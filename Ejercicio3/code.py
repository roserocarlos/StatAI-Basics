# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos desde GitHub
url_sensores = 'https://raw.githubusercontent.com/roserocarlos/StatAI-Basics/main/Ejercicio3/datos_sensores.csv'
df_sensores = pd.read_csv(url_sensores)

# 2. Transformar los datos
# Convertir la columna de fechas a formato datetime
df_sensores['Fecha'] = pd.to_datetime(df_sensores['Fecha'])

# Revisar las primeras filas de los datos
print("Vista previa de los datos:")
print(df_sensores.head())

# 3. Agrupación y cálculo de métricas
# Promedio por Invernadero
df_agrupado_mean = df_sensores.groupby('Invernadero').mean(numeric_only=True)
print("\nPromedio por Invernadero:")
print(df_agrupado_mean)

# Contar registros por Invernadero
df_agrupado_count = df_sensores.groupby('Invernadero').count()
print("\nCantidad de registros por Invernadero:")
print(df_agrupado_count)

# Suma total por Invernadero (excluyendo columnas datetime)
df_agrupado_sum = df_sensores.select_dtypes(exclude=['datetime']).groupby('Invernadero').sum()
print("\nSuma total por Invernadero:")
print(df_agrupado_sum)

# 4. Visualización de datos agrupados
# Gráfico del promedio de Temperatura por Invernadero
df_agrupado_mean['Temperatura'].plot(kind='bar', title='Promedio de Temperatura por Invernadero')
plt.xlabel('Invernadero')
plt.ylabel('Temperatura Promedio')
plt.show()

# Gráfico del conteo de registros por Invernadero
df_agrupado_count['Fecha'].plot(kind='bar', title='Número de Registros por Invernadero')
plt.xlabel('Invernadero')
plt.ylabel('Cantidad de Registros')
plt.show()

# Gráfico del promedio de Humedad por Invernadero
df_agrupado_mean['Humedad'].plot(kind='bar', title='Promedio de Humedad por Invernadero')
plt.xlabel('Invernadero')
plt.ylabel('Humedad Promedio')
plt.show()
