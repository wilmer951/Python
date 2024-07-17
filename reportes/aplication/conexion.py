import sqlalchemy as sa
import os
from sqlalchemy import create_engine


class Conexion:
    def __init__(self):

        self.server = '10.0.0.13,2616'
        self.database = 'ESP_TransactionPay'
        self.username = os.getenv('SQL_USERNAME')
        self.password = os.getenv('SQL_PASSWORD')
        # Esto puede variar según tu configuración
        self.driver = 'ODBC Driver 17 for SQL Server'
        # driver = 'ODBC+Driver+17+for+SQL+Server'  # Nombre del controlador

        try:
            self.engine = create_engine(
                f'mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver={self.driver}')
            self.connection = self.engine.connect()
        except Exception as e:
            print("Error:", type(e).__name__, "-", e)
            self.connection = None

    def conectar(self):
        return self.connection

    def cerrar(self):
        self.connection.close()
