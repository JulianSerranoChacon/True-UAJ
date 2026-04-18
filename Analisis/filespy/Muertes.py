#TODO ESTO SON PRUEBAS DE AURORA PARA ENSEÑAR COMO APENDEAR
#BORRAR UNA VEZ NOS PONGAMOS CON LOS DATOS DE VERDAD 

#Importacion para evento random
from numpy.random import randint
#Ejemplo qye encontré de una manera de añadir al dataframe
for i in range(5):
     singleDf.loc[i] = ['name' + str(i)] + list(randint(10, size=4))

#Probablemente tengamos que hacerlo así: 
#Usamos una lista/array para guardar toda la informacion
#Y luego volcamos al dataframe
prubaData = ['name7', 0, 0, 0, 0]
singleDf.loc[6] = prubaData;

singleDf
