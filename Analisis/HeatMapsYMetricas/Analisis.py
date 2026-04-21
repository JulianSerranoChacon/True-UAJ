#Imports:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import os
import json


path_to_json_files = '../../Assets/Sessions/'  

#metodo que coge todos los archivos json en un directorio
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]
jsonList=[0]*len(json_file_names)

for i in range(len(json_file_names)):
    jsonList[i]=pd.read_json(path_to_json_files+json_file_names[i])


# Creacion de las columnas que vamos a usar
col_names =  ['ID','MuTut', 'MuN1', 'MuN2', 'MuN3',  
              'MuSpike', 'MuE1', 'MuE2', 'MuE3', 'MuFi', 'MuIc',
              'Dis', 'DisAc', 'Mel', 'MelAc',
              'DamTut', 'DamN1', 'DamN2', 'DamN3',
              'DamSpike', 'DamE1', 'DamE2', 'DamE3', 'DamFi', 'DamIc',
              'Heal', 'OvHeal', 
              'ISesTime', 'TimTut', 'TimN1', 'TimN2', 'TimN3','SesTime','AmountHeal']
event_names =["sesStart","sesEnd","playerDeath","playerCP","playerEnd",
              "playerHeal","playerHit","enBulHit","enMelHit","playMel","playShot"]

# create an empty dataframe
# with columns
singleDf  = pd.DataFrame(columns = col_names)

import sys
sys.path.insert(0, "./filespy") 

#En esta celda es donde haremos el for por cada jugador (sessionID) distinto.
#Si lo hacemos bien podemos usar las librerias para ahorrarnos el trabajo.

#jug = [[1, 2, 3], [4, 2], [3]]; #Valor de jugadores arbitrario
jug = jsonList
for i in range(len(jug)):
    dataJug = ['name' + str(i), 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 
               0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0, 0, 0,
               0, 0, 
               0, 0, 0, 0, 0, 0,0]
    
    dataJug[27]=currEvent =jug[i][jug[i]["type"]=="sesStart"]["time"].values[0]
    dataJug[28]=currEvent =jug[i][jug[i]["type"]=="sesEnd"]["time"].values[0]
    

    for event in event_names:
        currEvent=jug[i][jug[i]["type"]==event]
        if(len(currEvent)>0):
            match event:
                case "playerDeath":
                    for j in range(4):
                        dataJug[1+j]=len(currEvent[currEvent["levelID"]==j+2])
                    for j in range(6):
                        dataJug[5+j]=len(currEvent[currEvent["deathCause"]==j])      
                case "playShot":
                    dataJug[11]=len(currEvent)     
                case "enBulHit": 
                    dataJug[12]=len(currEvent)
                case "playMel":
                    dataJug[13]=len(currEvent) 
                case "enMelHit":
                    dataJug[14]=len(currEvent) 
                case "playerHit":
                    for j in range(4):
                         dataJug[15+j]=sum(currEvent[currEvent["levelID"]==j+2]["hitDamage"].values.tolist())
                    for j in range(6):
                        dataJug[19+j]=sum(currEvent[currEvent["hitCause"]==j]["hitDamage"].values.tolist())
                case "playerHeal":
                    dataJug[25] =len(currEvent) 
                    prevHealth=sum(currEvent["previousHealth"].values.tolist()) 
                    healAmount=sum(currEvent["healingAmount"].values.tolist()) 
                    finalHealth=sum(currEvent["finalHealth"].values.tolist())
                    dataJug[26]=prevHealth+healAmount-finalHealth
                    dataJug[33] = healAmount
                case "sesStart":
                    dataJug[27]= currEvent["time"].values[0]
                case "playerEnd":
                    for j in range(4):
                        if(len (currEvent[currEvent["levelID"]==2+j]) > 0):
                            dataJug[28+j]= currEvent[currEvent["levelID"]==2+j]["time"].values[0]-dataJug[27+j]
                case "sesEnd":
                    dataJug[32]= currEvent["time"].values[0]
               
                
    singleDf.loc[i] = dataJug
#Metrica 1
mlabels = ['MuTut','MuN1','MuN2','MuN3']
#auxdf = pd.DataFrame(columns = mlabels)
ar = [sum(singleDf['MuTut']), sum(singleDf['MuN1']), sum(singleDf['MuN2']), sum(singleDf['MuN3'])]
#auxdf.loc[0] = ar
#auxdf
#max = auxdf.plot(y=['MuTut','MuN1','MuN2','MuN3'], kind='bar')

plt.pie(ar, labels = mlabels, startangle = 90)
plt.title("Distribución de Muertes por Nivel")
plt.savefig('./Metricas/Metrica1.png')

#Metrica 3
mlabels = ['MuSpike', 'MuE1', 'MuE2', 'MuE3', 'MuFi', 'MuIc']
ar = [sum(singleDf['MuSpike']), sum(singleDf['MuE1']), sum(singleDf['MuE2']), sum(singleDf['MuE3']), sum(singleDf['MuFi']), sum(singleDf['MuIc'])]
plt.clf()
plt.pie(ar, labels = mlabels, startangle = 90)
plt.title("Distribución de Muertes por Causas")
plt.savefig('./Metricas/Metrica3.png')

#Metrica 4
mlabels = ['TimTut', 'TimN1', 'TimN2', 'TimN3']
ar1=np.array([sum(singleDf['TimTut']),sum(singleDf['TimN1']),sum(singleDf['TimN2']),sum(singleDf['TimN3'])])
ar2 = np.array([len(singleDf[singleDf['TimTut'] != 0]),len(singleDf[singleDf['TimN1'] != 0]),len(singleDf[singleDf['TimN2'] != 0]),len(singleDf[singleDf['TimN3'] != 0])])
ar2[ar2==0]=1
ar=ar1/ar2
auxdf = pd.DataFrame(columns = mlabels)
auxdf.loc[0] = ar
plt.clf()
max = auxdf.plot(y=['TimTut', 'TimN1', 'TimN2', 'TimN3'], kind='bar')
plt.title("Distribución de Tiempo tardado por Nivel")
plt.savefig('./Metricas/Metrica4.png')

#Metrica 5 y 6
mlabels = ['AciertosDisparos', 'FallosDisparo', 'AciertosMelee', 'FallosMelee']
ar = [sum(singleDf['DisAc']), sum(singleDf['Dis']) - sum(singleDf['DisAc']), 
      sum(singleDf['MelAc']), sum(singleDf['Mel']) - sum(singleDf['MelAc'])]
plt.clf()
plt.pie(ar, labels = mlabels, startangle = 90)
plt.title("Tasa de Aciertos y fallos de los distintos ataques del jugador")
plt.savefig('./Metricas/Metrica5y6.png')

#Metrica 7
mlabels = ['DamTut','DamN1','DamN2','DamN3']
auxdf = pd.DataFrame(columns = mlabels)
ar = [sum(singleDf['DamTut']), sum(singleDf['DamN1']), sum(singleDf['DamN2']), sum(singleDf['DamN3'])]
auxdf.loc[0] = ar
max = auxdf.plot(y=['DamTut','DamN1','DamN2','DamN3'], kind='bar')
plt.title("Distribución de Daño recibido por el jugador en cada nivel")
plt.savefig('./Metricas/Metrica7.png')
#Metrica 8
mlabels = ['DamE1', 'DamE2', 'DamE3', 'DamFi', 'DamIc']
ar = [sum(singleDf['DamE1']), sum(singleDf['DamE2']), sum(singleDf['DamE3']), sum(singleDf['DamFi']), sum(singleDf['DamIc'])]
auxdf = pd.DataFrame(columns = mlabels)
auxdf.loc[0] = ar
max = auxdf.plot(y=['DamE1', 'DamE2', 'DamE3', 'DamFi', 'DamIc'], kind='bar')
plt.title("Distribución de daño recibido por el jugador por causa")
plt.savefig('./Metricas/Metrica8.png')
#Metrica 9
mlabels = ['FreqHeal']
freq_heal_indv = singleDf['Heal'] / (singleDf['SesTime'] / 60000) #Curas por minuto (paso los milisegundos a minutos)

#medias de las frecuencias de todos los jugadores
media = freq_heal_indv.mean()


auxdf = pd.DataFrame(columns = mlabels)
auxdf.loc[0] = media
max = auxdf.plot(y=['FreqHeal'], kind='bar')
plt.title("Media de cuanto se cura cada jugador por minuto")
plt.savefig('./Metricas/Metrica9.png')

# Métrica 10: Proporción de curación malgastada
mlabels = ['TotalWastedHeal','TotalNonWatedHeal','TotalHeal']
auxdf = pd.DataFrame(columns = mlabels)


ar=[sum(singleDf['OvHeal']),sum(singleDf['AmountHeal'])-sum(singleDf['OvHeal']),sum(singleDf['AmountHeal'])]
auxdf.loc[0] = ar
ax = auxdf.plot(y= ['TotalWastedHeal','TotalNonWastedHeal','TotalHeal'], kind='bar')
ax.set_ylim(0,1000) #Para ver el resultado como si fuera un porcentaje
plt.title("Tasa de Curación malgastada")
plt.savefig('./Metricas/Metrica10.png')

