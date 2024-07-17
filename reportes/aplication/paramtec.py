from datetime import datetime, timedelta

today = datetime.today()


class Parametros:
    def __init__(self):

        # ruta donde se almacena los logs.
        self.log_file = 'C:/reportes/log/log.txt'

        # RUTA Y NOMBRE DEL REPORTE DE DAVIPLATA.
        self.nomflieDaviplata = 'C:/reportes//reportes/Transacciones Daviplata.xlsx'

        # RUTA Y NOMBRE DEL REPORTE DE CARROYA.
        self.nomflieCarroya = 'C:/reportes//reportes/Transacciones Carrroya.xlsx'

        # RUTA Y NOMBRE DEL REPORTE DE # EZYPASS.
        self.nomflieEzypass = 'C:/reportes//reportes/Transacciones EZYPASS.xlsx'

        # Calcular el primer día de la semana pasada
        start_of_last_week = today - timedelta(days=today.weekday() + 7)

        # Calcular el último día de la semana pasada
        end_of_last_week = start_of_last_week + timedelta(days=6)

        self.yearstar = start_of_last_week.strftime('%Y')
        self.monthstar = start_of_last_week.strftime('%m')
        self.daystar = start_of_last_week.strftime('%d')

        self.yearend = end_of_last_week.strftime('%Y')
        self.monthend = end_of_last_week.strftime('%m')
        self.dayend = end_of_last_week.strftime('%d')
