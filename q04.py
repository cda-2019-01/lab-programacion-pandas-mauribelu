##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
## Lectura de tabla
x1 = pd.read_csv('tbl1.tsv', sep = '\t')
##Imprimir Valores únicos
unicos = x1['_c4'].unique()
resultado = []
for x in unicos:
    resultado.append(x.upper())
resultado = sorted(resultado)
resultado


