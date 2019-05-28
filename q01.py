##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd
import numpy as np
## Leer el archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
## Cantidad de registros por cada letra
x.groupby'(_c1').count()['_c0']
print(x)
