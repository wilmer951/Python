import pandas as pd
from sqlalchemy import create_engine


try:

    engine = create_engine('mysql+mysqlconnector://root:@localhost/basededatos')




    archivo = 'C:/xampp/htdocs/Python/ExportMysql/estudiantesdesorden.xlsx'
    df=pd.read_excel(archivo)


    df = pd.read_excel(archivo,skiprows=5)






    #se muestran solo las columnas seleccioandas.

    df_filter = df[['Nombre','Materia','Edad','correo']]
    
    
    
    #se evita fias con campos vacios
    df_filter = df_filter.dropna(subset=['Nombre','Materia'])

    #se inserta en base de datos.
    df_filter.to_sql('tbprueba', con=engine, if_exists='append', index=False)

    print(df_filter)











except Exception as e:
    print("Error:", type(e).__name__, "-", e)