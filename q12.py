##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
import pandas as pd
import numpy as np
## Leer tabla
x2 = pd.read_csv('tbl2.tsv', sep = '\t')
## suma de tablas
x2 = x2.groupby('_c5a')['_c5b'].sum()
print(x2)

