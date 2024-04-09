import pandas as pd

archivo = pd.read_excel("xlsx/clientes.ods",engine="odf")
celda = archivo.iloc[1,1]
print(celda)
