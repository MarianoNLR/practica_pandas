import pandas as pd

# 1. Cargar los datos.

df = pd.read_csv('remuneracion-neta-sector-actividad-economica-sector-privado.csv')

# 2. Exploracion inicial de los datos.
#print(df.describe())

# Verifacion de valores faltantes
#print(df.isnull().sum())

# Columnas del dataset
#print(df.columns)

#### 3. Analisis Específico de las Preguntas

# 1. Minima y maxima remuneracion por año en cada sector
#print(df.select_dtypes(include=['number']).max())

# 2. Sector/Rubro con mayor remunearcion por periodo
df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'])
valores_maximo_fila = df.select_dtypes(include=['number']).max(axis=1)
maximos_columna = df.select_dtypes(include=['number']).idxmax(axis=1)
mayor_remuneracion_fila = pd.DataFrame({
    'Periodo': df['indice_tiempo'],
    'Sector': maximos_columna,
    'Remuneracion': valores_maximo_fila
})

#print(mayor_remuneracion_fila)

# 3. Sector/Rubro con menor remuneracion por periodo
valores_minimos_fila = df.select_dtypes(include=['number']).replace(0, None).min(axis=1)
minimos_columna = df.select_dtypes(include=['number']).idxmin(axis=1)
menor_remuneracion_fila = pd.DataFrame({
    'Periodo': df['indice_tiempo'],
    'Sector': minimos_columna,
    'Remuneracion': valores_minimos_fila
})

print(menor_remuneracion_fila)