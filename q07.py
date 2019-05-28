##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
##Leer tabla
x = pd.read_csv('tbl0.tsv', sep = '\t')
##Suma de columnas
x['suma_c0_c2'] = x['_c0'] + x['_c2']
x.head()

