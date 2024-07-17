import os
import glob

from conexion import Conexion
from paramtec import Parametros
from datetime import datetime
from envioemail import Envioemail


import pandas as pd


class Aplication:

    def borradoreports(self):

        # Definir la ruta de la carpeta que quieres limpiar
        carpeta_a_limpiar = 'C:/reportes/reportes'

        # Obtener una lista de todos los archivos en la carpeta
        archivos_en_carpeta = glob.glob(os.path.join(carpeta_a_limpiar, '*'))

        # Iterar sobre la lista de archivos y borrar cada uno
        for archivo in archivos_en_carpeta:
            try:
                # Verificar que sea un archivo (no directorio)
                if os.path.isfile(archivo):
                    os.remove(archivo)
                    self.log_error(mensje="Borrado exitoso")
            except Exception as e:
                self.log_error(f"No se pudo borrar {archivo}: {e}")

    # obtner reporte de daviplata

    def reportDaviplata(self):

        # instanaciar objeto conexion
        conn = Conexion()
        con = conn.conectar()

        # instanciar parametros
        params = Parametros()


# en caso de ser conexion exitosa.
        if con:

            # conexion establecida.
            self.log_error(mensje='conexion exitosa')

            # obtener las fechas para los reportes

            fecha_reportstar = (f'fecha inicial reporte {params.yearstar}  {
                                params.monthstar}  {params.daystar} ')
            fecha_reporend = (f'fecha final de reporte {params.yearend}  {
                params.monthend}  {params.dayend} ')

            self.log_error(mensje=fecha_reportstar)
            self.log_error(mensje=fecha_reporend)

            try:

                sql_query = f"""
                    SELECT [CLIENTE]
                        ,[MEDIOPAGO]
                        ,[FECHA]
                        ,[CODIGOTRANSACCION]
                        ,[CONCEPTO]
                        ,CAST(VALORPAGADO AS int) as VALORPAGADO
                    FROM [ESP_TransactionPay].[dbo].[ESPV_TransaccionesClientes]
                    WHERE YEAR(FECHA) = {params.yearstar}
                    AND MONTH(FECHA) BETWEEN {params.monthstar} AND {params.monthend}
                    AND DAY(FECHA) BETWEEN {params.daystar} AND {params.dayend}
                    AND Estado = 'APROBADO'AND MEDIOPAGO = 'DAVIPLATA'
                """

                df = pd.read_sql(sql_query, con)

                cant_result = df.shape[0]

                self.log_error(
                    mensje=(f'Cantiad de resultados Daviplata {df.shape[0]} '))

                if cant_result > 0:

                    # Guarda el DataFrame en el archivo Excel
                    df.to_excel(params.nomflieDaviplata, index=False)

                    # ajsutar ancho de columnas a la hoja

                    # ENVIO DE EMAIL

                    # controlar cuando el reporte sea de dos meses diferentes se utliza la variable me en el asunto del correo.

                    if params.monthstar == params.monthend:
                        asunto = f"Transacciones electrónicas Daviplata {
                            params.daystar} a {params.dayend} del mes {params.monthstar}"
                    else:
                        asunto = f"Transacciones electrónicas Daviplata {params.daystar} del mes {
                            params.monthstar} al  {params.dayend} del mes {params.monthend}"

                    destinatario = "wpulido@eglobalt.com"
                    cuerpoemail = "Cordial saludo \n \n Adjunto, transacciones electrónicas (Medio de pago Daviplata)"
                    adjunto = params.nomflieDaviplata

                    sendemail = Envioemail()
                    sendemail.send_email(
                        destinatario, asunto, cuerpoemail, adjunto)

            except Exception as e:
                self.log_error(mensje=e)

            # cerra conexion.
            con = conn.cerrar()
            self.log_error(mensje='conexion cerrada')

        else:

            # en caso de ser conexion falida.
            self.log_error(mensje='conexion fallida')


# obtner reporte de carroya


    def reportCarroya(self):

        # instanaciar objeto conexion
        conn = Conexion()
        con = conn.conectar()

        # instanciar parametros
        params = Parametros()


# en caso de ser conexion exitosa.
        if con:

            # conexion establecida.
            self.log_error(mensje='conexion exitosa')

            # obtener las fechas para los reportes

            fecha_reportstar = (f'fecha inicial reporte {params.yearstar}  {
                                params.monthstar}  {params.daystar} ')
            fecha_reporend = (f'fecha final de reporte {params.yearend}  {
                params.monthend}  {params.dayend} ')

            self.log_error(mensje=fecha_reportstar)
            self.log_error(mensje=fecha_reporend)

            try:

                sql_query = f"""
                    SELECT [CLIENTE]
                        ,[MEDIOPAGO]
                        ,[FECHA]
                        ,[CODIGOTRANSACCION]
                        ,[CONCEPTO]
                        ,CAST(VALORPAGADO AS int) as VALORPAGADO
                    FROM [ESP_TransactionPay].[dbo].[ESPV_TransaccionesClientes]
                    WHERE YEAR(FECHA) = {params.yearstar}
                    AND MONTH(FECHA) BETWEEN {params.monthstar} AND {params.monthend}
                    AND DAY(FECHA) BETWEEN {params.daystar} AND {params.dayend}
                    and Estado !='FAILED' and Estado != 'REJECTED' and MEDIOPAGO = 'CARROYA'
                """

                df = pd.read_sql(sql_query, con)

                cant_result = df.shape[0]

                self.log_error(
                    mensje=(f'Cantiad de resultados Carroya {df.shape[0]} '))

                if cant_result > 0:

                    # Guarda el DataFrame en el archivo Excel
                    df.to_excel(params.nomflieCarroya, index=False)

                    # ajsutar ancho de columnas a la hoja

        # ENVIO DE EMAIL

                    # controlar cuando el reporte sea de dos meses diferentes se utliza la variable me en el asunto del correo.

                    if params.monthstar == params.monthend:
                        asunto = f"Transacciones electrónicas Carroya {
                            params.daystar} a {params.dayend} del mes {params.monthstar}"
                    else:
                        asunto = f"Transacciones electrónicas Carroya {params.daystar} del mes {
                            params.monthstar} al  {params.dayend} del mes {params.monthend}"

                    destinatario = "wpulido@eglobalt.com"
                    cuerpoemail = "Cordial saludo \n \n Adjunto, transacciones electrónicas (Medio de pago Carroya)"

                    adjunto = params.nomflieCarroya

                    sendemail = Envioemail()
                    sendemail.send_email(
                        destinatario, asunto, cuerpoemail, adjunto)

            except Exception as e:
                self.log_error(mensje=e)

            # cerra conexion.
            con = conn.cerrar()
            self.log_error(mensje='conexion cerrada')

        else:

            # en caso de ser conexion falida.
            self.log_error(mensje='conexion fallida')


# obtner reporte de EZYPASS


    def reportEzypass(self):

        # instanaciar objeto conexion
        conn = Conexion()
        con = conn.conectar()

        # instanciar parametros
        params = Parametros()


# en caso de ser conexion exitosa.
        if con:

            # conexion establecida.
            self.log_error(mensje='conexion exitosa')

            # obtener las fechas para los reportes

            fecha_reportstar = (f'fecha inicial reporte {params.yearstar}  {
                                params.monthstar}  {params.daystar} ')
            fecha_reporend = (f'fecha final de reporte {params.yearend}  {
                params.monthend}  {params.dayend} ')

            self.log_error(mensje=fecha_reportstar)
            self.log_error(mensje=fecha_reporend)

            try:

                sql_query = f"""
                    SELECT [CLIENTE]
                        ,[MEDIOPAGO]
                        ,[FECHA]
                        ,[CODIGOTRANSACCION]
                        ,[CONCEPTO]
                        ,CAST(VALORPAGADO AS int) as VALORPAGADO
                    FROM [ESP_TransactionPay].[dbo].[ESPV_TransaccionesClientes]
                    WHERE YEAR(FECHA) = {params.yearstar}
                    AND MONTH(FECHA) BETWEEN {params.monthstar} AND {params.monthend}
                    AND DAY(FECHA) BETWEEN {params.daystar} AND {params.dayend}
                    and Estado !='FAILED' and Estado != 'REJECTED' AND cajero = 'EZYPASS'
                """

                df = pd.read_sql(sql_query, con)

                cant_result = df.shape[0]

                self.log_error(
                    mensje=(f'Cantiad de resultados EZYPASS {df.shape[0]} '))

                if cant_result > 0:

                    # Guarda el DataFrame en el archivo Excel
                    df.to_excel(params.nomflieEzypass, index=False)

                    # ajsutar ancho de columnas a la hoja

        # ENVIO DE EMAIL

                    # controlar cuando el reporte sea de dos meses diferentes se utliza la variable me en el asunto del correo.

                    if params.monthstar == params.monthend:
                        asunto = f"Transacciones electrónicas EZYPASS {
                            params.daystar} a {params.dayend} del mes {params.monthstar}"
                    else:
                        asunto = f"Transacciones electrónicas EZYPASS {params.daystar} del mes {
                            params.monthstar} al  {params.dayend} del mes {params.monthend}"

                    destinatario = "wpulido@eglobalt.com"
                    cuerpoemail = "Cordial saludo \n \n Adjunto, transacciones electrónicas (Medio de pago EZYPASS)"

                    adjunto = params.nomflieEzypass

                    sendemail = Envioemail()
                    sendemail.send_email(
                        destinatario, asunto, cuerpoemail, adjunto)

            except Exception as e:
                self.log_error(mensje=e)

            # cerra conexion.
            con = conn.cerrar()
            self.log_error(mensje='conexion cerrada')

        else:

            # en caso de ser conexion falida.
            self.log_error(mensje='conexion fallida')


# Generacon de logs.


    def log_error(self, mensje):

        # instanciar parametros
        params = Parametros()
        self.msm = mensje

        file_path = params.log_file

        with open(file_path, 'a') as file:
            file.write(f'{datetime.now()}  {self.msm} \n')


app = Aplication()
eje = app.borradoreports()
aje = app.reportDaviplata()
aje = app.reportCarroya()
aje = app.reportEzypass()
