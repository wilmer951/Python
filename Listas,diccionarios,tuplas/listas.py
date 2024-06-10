

# recorrido de una lista


import pandas as pd
frutas = ['manzana', 'pera', 'limon']


for a in frutas:
    print(a)


# ELIMINAR DATOS DUPLICADOS DE UNA LISTA

lista = [10, 20, 30, 50, 10, 10, 10, 10, 20, 30]

lista = set(lista)

print(lista)


# combaritr dos listas a un diccionario.

frutas = ['Manzana', 'Pera', 'Lulo', 'Mango']
precio = ['100', '200', '300', '100']


diccionario = dict(zip(frutas, precio))
print(diccionario)


# DOS LISTAS AUN DATAFRAME.


frutas = ['Manzana', 'Pera', 'Lulo', 'Mango']
precio = ['100', '200', '300', '100']


df = pd.DataFrame({'Frutas': frutas, 'Precio': precio})


print(df)
