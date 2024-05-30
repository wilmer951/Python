import pandas as pd
from sqlalchemy import create_engine

try:
  engine = create_engine('mysql+mysqlconnector://root:@localhost/basededatos')
  sql_query = 'SELECT * FROM COVID'


  df = pd.read_sql(sql_query,engine)

  print(df.head(10))



except Exception as e:
    print("Error presentado:", e)