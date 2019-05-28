##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
##Lectura de tabla
x = pd.read_csv('tbl0.tsv', sep = '\t')
##Agrega el año como una columna al final
x['year'] = [i.split('-')[0] for i in x['_c3']]
x.head()
