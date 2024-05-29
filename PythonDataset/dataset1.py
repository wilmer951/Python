import pandas as pd

df = pd.read_csv('C:/xampp/htdocs/Python/PythonDataset/dataset1.csv',encoding='latin-1',sep=';')

print(df[df.Numer>300])


#este es un camio