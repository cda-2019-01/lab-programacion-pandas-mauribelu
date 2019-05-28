##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
##Lectura de archivo
x = pd.read_csv('ltbl0.tsv', sep = '\t')
##Imprimir Promedio
x.groupby('_c1').mean()['_c2']
print(x)
