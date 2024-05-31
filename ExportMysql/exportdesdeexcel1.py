import pandas as pd
from sqlalchemy import create_engine

archivo = 'C:/xampp/htdocs/Python/ExportMysql/estudiantes.xlsx'

try:
    # Configura la conexión usando SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:@localhost/basededatos')

    # Lee el DataFrame desde el archivo de Excel
    df = pd.read_excel(archivo)

    # Exporta el DataFrame a MySQL
    


    df_export = df[['Nombre','Materia','correo','Edad']]

    print(df_export)
    df_export.to_sql('tbprueba', con=engine, if_exists='append', index=False)

    print("Exportación exitosa del DataFrame a MySQL")

except Exception as e:
    print("Error presentado:", e)