import pandas as pd

archivo = pd.read_excel("xlsx/clientes.xlsx")
print(archivo)
celda = archivo.iloc[1,1]
print(celda)
