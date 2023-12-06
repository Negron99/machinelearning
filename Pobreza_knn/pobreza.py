import pandas as pd
import numpy as np

# Cargar el DataFrame utilizando la codificación 'ISO-8859-1'
df = pd.read_csv(r'C:\Users\Axel Esdras\Desktop\machine\Indicadores_municipales_sabana_DA.csv', sep=",", encoding='ISO-8859-1')

# Resto del código...

# Eliminar las columnas no deseadas
df = df.drop(columns=['nom_mun', 'nom_ent'])

# Definir las categorías a buscar
categorias = ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto']

# Crear un diccionario para almacenar los valores promedio de cada categoría en gdo_rezsoc00
valores_promedio_gdo_rezsoc00 = {}

# Calcular el valor de reemplazo para cada categoría en gdo_rezsoc00
for categoria in categorias:
    valores_promedio_gdo_rezsoc00[categoria] = np.nanmean(df[df['gdo_rezsoc00'] == categoria].select_dtypes(include=[np.number]))

# Reemplazar las categorías en gdo_rezsoc00 con los valores calculados
for categoria in categorias:
    df['gdo_rezsoc00'] = df['gdo_rezsoc00'].replace(categoria, valores_promedio_gdo_rezsoc00[categoria])

# Utilizar los valores reemplazados de gdo_rezsoc00 para calcular valores promedio en gdo_rezsoc05
valores_promedio_gdo_rezsoc05 = {}

for categoria in categorias:
    valores_promedio_gdo_rezsoc05[categoria] = np.nanmean(df[df['gdo_rezsoc05'] == categoria].select_dtypes(include=[np.number]))

# Reemplazar las categorías en gdo_rezsoc05 con los valores calculados
for categoria in categorias:
    df['gdo_rezsoc05'] = df['gdo_rezsoc05'].replace(categoria, valores_promedio_gdo_rezsoc05[categoria])

# Utilizar los valores reemplazados de gdo_rezsoc00 para calcular valores promedio en gdo_rezsoc10
valores_promedio_gdo_rezsoc10 = {}

for categoria in categorias:
    valores_promedio_gdo_rezsoc10[categoria] = np.nanmean(df[df['gdo_rezsoc10'] == categoria].select_dtypes(include=[np.number]))

# Reemplazar las categorías en gdo_rezsoc10 con los valores calculados
for categoria in categorias:
    df['gdo_rezsoc10'] = df['gdo_rezsoc10'].replace(categoria, valores_promedio_gdo_rezsoc10[categoria])

# Calcular el valor de reemplazo como el promedio de todos los valores numéricos
promedio_global = np.nanmean(df.select_dtypes(include=[np.number]))

# Reemplazar los valores NaN con el promedio global
df = df.fillna(promedio_global)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Mostrar todas las filas de las 3 columnas con el proceso realizado
print(df[['gdo_rezsoc00', 'gdo_rezsoc05', 'gdo_rezsoc10']])


