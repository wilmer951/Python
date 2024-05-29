import pandas as pd


try:

#extrear la informcion de df1csv
    df1 = pd.read_csv('C:/xampp/htdocs/Python/PythonDataset/df1.csv',encoding='latin-1').set_index('Nombre')
    
#extrear la informcion de df1csv    
    df2 = pd.read_csv('C:/xampp/htdocs/Python/PythonDataset/df2.csv',encoding='latin-1').set_index('Nombre') 


#extrear la informcion de df1csv    
    df3 = pd.read_csv('C:/xampp/htdocs/Python/PythonDataset/df3.csv',encoding='latin-1').set_index('Nombre')     





#********************************************************************************************************
#filtrado por filas
    
 #concatena la informacion de los dos csv axix es opcional 0 significa que agregara las fialas.   
    
   # df = pd.concat([df1,df2],axis=0)
#Imprime todo el df  
 #   print(df)

#Imprime el df filrado por mayores de 30.
 #   print(df[df.Edad>30])





#********************************************************************************************************
#filtrado por Columnas



 #concatena la informacion de los dos csv axix es opcional 1 significa que agregara las Columnas.   

# df4 = pd.concat([df1,df3],axis=1)
     #print(df4)



#********************************************************************************************************
#MEZCLA

    df5= pd.merge(df1,df3,on='Nombre',how='right')

    print(df5)










except Exception as e:
    print("Error Presentado:", e)





   


