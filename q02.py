##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
##Lectura
x = pd.read_csv('ltbl0.tsv', sep = '\t')
##Promedio
x.groupby(['_c1'])['_c2'].mean()