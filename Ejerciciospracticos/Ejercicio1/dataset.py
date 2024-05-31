import pandas as pd

try:
    archivo = 'C:/xampp/htdocs/Python/Ejerciciospracticos/Ejercicio1/cotizacion.csv'

    df = pd.read_csv(archivo,sep=';',thousands='.',decimal=',')


    df = df[['Nombre','Minimo','Maximo']]

    df['Minimo'] = pd.to_numeric(df['Minimo'])
    df['Maximo'] = pd.to_numeric(df['Maximo'])

    
    print(df)


    summinmios=df['Minimo'].sum()
    mediaminmo=df['Minimo'].mean()
    print('la suma de minimos es ',summinmios)
    print('La media de los minmios es', mediaminmo)

    summmaximos=df['Maximo'].sum()
    mediamaximo=df['Maximo'].mean()
    print('la suma de maximos es ',summmaximos)
    print('La media de los minmios es', mediaminmo)



    dfresumen = [[summinmios,mediaminmo,summmaximos,mediamaximo]]
    
    dfresumen = pd.DataFrame(dfresumen, columns=['MInimo', 'Meida MInimo', 'Maximo','Media Maximo'])

    print(dfresumen)





except Exception as e:

    print('error',e)