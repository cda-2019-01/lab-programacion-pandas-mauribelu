##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
##Leer archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
##Construcción de tabla
xtemp = x.groupby('_c1')['_c2'].apply(list)
xb = pd.DataFrame()
xb['_c1'] = xtemp.keys()
xb['_c2'] = [elem for elem in xtemp]
xb['_c2'] = [":".join(str(v) for v in sorted(elem)) for elem in xb['_c2']]


