import pandas as pd

# Cargar el dataset desde el archivo CSV
df = pd.read_csv("dataset.csv")

# Separar el dataset en características (X) y etiquetas (y)
X = df.drop('Aprendizaje Suficiente', axis=1)
y = df['Aprendizaje Suficiente']

# Contar el número de instancias de cada clase
instancias_totales = len(y)
conteo_si = y.value_counts()['Sí']
conteo_no = y.value_counts()['No']

# Calcular las probabilidades previas
P_si = conteo_si / instancias_totales
P_no = conteo_no / instancias_totales

