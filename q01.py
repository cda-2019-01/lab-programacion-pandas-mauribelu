##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
## Leer el archivo
##x = pd.read_csv('tbl0.tsv', sep = '\t')
## Cantidad de registros por cada letra
x.groupby'(_c1').count()['_c0']
