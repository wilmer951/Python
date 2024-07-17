import win32com.client
from datetime import datetime
from paramtec import Parametros


class Envioemail:
    def __init__(self):
        try:
            self.outlook = win32com.client.Dispatch("Outlook.Application")
            self.mensaje = self.outlook.CreateItem(0)  # Create a new mail item
        except Exception as e:

            self.log_erroremail(mensaje=f'Error al iniciar outlook.{e}')

    def send_email(self, destinatario, asunto, cuerpo, adjunto):
        try:
            self.mensaje.To = destinatario
            self.mensaje.Subject = asunto
            self.mensaje.Body = cuerpo
            self.mensaje.Attachments.Add(adjunto)
            self.mensaje.Send()
            self.log_erroremail(mensaje='El email fue enviado exitosamente.')

        except Exception as e:

            self.log_erroremail(
                mensaje=f'Error al enviar correo.{e}')

    def log_erroremail(self, mensaje):

        params = Parametros()
        self.msm = mensaje
        try:
            file_path = params.log_file
            with open(file_path, 'a') as file:
                file.write(f'{datetime.now()}  {self.msm}\n')
        except Exception as e:
            print("Error writing to log file:", e)
