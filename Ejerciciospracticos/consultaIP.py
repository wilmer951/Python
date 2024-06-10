import pandas as pd
import os


try:

    # opción 1 ***************************************************************************

    archivo = 'C:/xampp/htdocs/Python/data/ip.xlsx'
    df = pd.read_excel(archivo)

    with open('resultados_ping.txt', 'w') as archivo_resultados:
        for columna in df.columns:
            for valor in df[columna]:
                ip = valor
                # Agregamos '-n 1' para enviar solo un paquete de ping
                resultado = os.system(f'ping -n 1 {ip}')
                if resultado == 0:
                    linea = f"La IP {ip} : OK\n"
                else:
                    linea = f"La IP {ip} : KO\n"
                archivo_resultados.write(linea)

    # opción 2 ***************************************************************************
    archivo = 'C:/xampp/htdocs/Python/data/ip.xlsx'

    df = pd.read_excel(archivo)
    with open('resultados_ping.txt', 'w') as archivo_resultados:
        for index, row in df.iterrows():
            ip = row[0]
            resultado = os.system(f'ping -n 1 {ip}')
            if resultado == 0:
                linea = f"La IP {ip} : OK\n"
            else:
                linea = f"La IP {ip} : KO\n"
            archivo_resultados.write(linea)


except Exception as e:
    print("Error:", type(e).__name__, "-", e)
