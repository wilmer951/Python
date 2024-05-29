import pandas as pd


try:
    
    archivoestudiantes = 'C:/xampp/htdocs/Python/PythonDataset/estudiantes.xlsx'
    archivonotas = 'C:/xampp/htdocs/Python/PythonDataset/notas.xlsx'

    df1 =pd.read_excel(archivoestudiantes)    
    print(df1)




    df2 =pd.read_excel(archivonotas)    
    print(df2)



    resumen = pd.merge(df1,df2 ,on='Nombre')

    print(resumen)


except Exception as e:
    print("Error Presentado:", e)



