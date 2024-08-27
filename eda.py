import pandas as pd

# Cargar el dataset
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

# Mostrar primeras y ultimas 5 filas
#print(df)

# Informacion general del dataset
#print(df.info())

# Resumen estadistico de las columnas numericas
#print(df.describe())

# Mostras las columnas
#print(df.columns)

# Contar valores faltantes por columna
#print(df.isnull().sum())

# Eliminar filas con valores faltantes
df_limpio = df.dropna()

# Eliminar filas duplicadas
df_sin_duplicados = df_limpio.drop_duplicates()

####
# 3 Analisis estádistico y Distribucion de datos

# 3.1 Analisis de Variables Categoricas
# Distribucion de las variables numericas
#print(df['Age'].describe())

# 3.1 Analisis de Variables categoricas
#print(df['Gender'].value_counts())
#print(df['Sleep Disorder'].value_counts(dropna=False))
#print(df['Occupation'].value_counts())

####
# 4 Identificacion de Patrones y Relaciones
# 4.1 Relacion entre variables numericas

df_columnas_corr = df[['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']]
print(df_columnas_corr.corr())

###### Conclusiones que podemos hacer viendo la tabla de correlaciones

# Correlacion moderada entre la edad y la calidad del sueño (0.47). Es decir que a medida que la edad aumenta la calidad del sueño tiende a mejorar de manera moderada

# Correlacion inversa entre el nivel de estres y calidad del sueño (-0.89). Mientras aumenta el estres la calidad de sueño disminuye drásticamente.

# Correlacion casi inexistente entre el nivel de estres y activdad fisica (-0.034).

# Correlacion positiva entre la calidad del sueño y la duracion del sueño (0.88). Indica que mientras mas sea la duracion del sueño, mejor la calidad.
