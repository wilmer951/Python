import pandas as pd
import numpy as np


data = 'C:/xampp/htdocs/Python/data/estadistica.xlsx'


df = pd.read_excel(data)


df['clasificacion'] = np.where(
    df['TIME_PERIOD_CODE'] > 2015, 'actual', 'pasado')

print(df)
