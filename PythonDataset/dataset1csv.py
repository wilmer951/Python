import pandas as pd




df = pd.read_csv('C:/xampp/htdocs/Python/PythonDataset/dataset1.csv',encoding='latin-1',sep=';')


# SE REALIZA FILTRO DEL CSV POR AÑO MAYOR A 20 Y NUMER MAYOR A 5
filtrar = (df['Year']>2020) & (df['Numer']> 5)


# EL FILTROSE GUARDA EN OTRO DATAFRAME DF2 Y SE RESETEA LOS INDICES PARA NUEVAS CONSULTAS DEL DF2
df2=df[filtrar].head(5).reset_index(drop=True)



#IMPRIMIR DF2
print(df2.sort_values('Numer',ascending=True))

print('Otro resultado')
print(df2.loc[0,'Year'] )


#este es un cambio de prueba