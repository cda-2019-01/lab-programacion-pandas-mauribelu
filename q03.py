##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
##Lectura de la tabla
x = pd.read_csv('tbl0.tsv', sep = '\t')
## Imprime el máximo
x.groupby ('_c1').max()['_c2']
print(x)

