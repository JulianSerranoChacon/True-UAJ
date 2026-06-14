#Imports:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import os
import sys
import json

#Creacion de path a los jsons
path_to_json_files = '../../Datos Telemetria/'

#metodo que coge todos los archivos json en un directorio
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]
jsonList=[0]*len(json_file_names)

sys.path.insert(0, "./filespy") 

#Creacion de variables globales
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


def Metrica1():
    #Metrica 1
    mlabels = ['MuTut','MuN1','MuN2','MuN3']
    ar = [sum(singleDf['MuTut']), sum(singleDf['MuN1']), sum(singleDf['MuN2']), sum(singleDf['MuN3'])]
    if(sum(singleDf['MuTut']) + sum(singleDf['MuN1']) + sum(singleDf['MuN2']) + sum(singleDf['MuN3']) > 0): #Comprobar que al menos hay un valor en una de las categorias para evitar fallos con el pie chart
        mNames= ['Tutorial', 'Nivel 1', 'Nivel 2', 'Nivel 3'] #Nombres mas legibles
        plt.pie(ar, labels = mNames, startangle = 90)
        plt.title("Distribución de Muertes por Nivel")
        plt.savefig('./Metricas/Metrica1.png')

def Metrica2():
    #Metrica 2
    mlabels = ['MuSpike', 'MuE1', 'MuE2', 'MuE3', 'MuFi', 'MuIc']
    ar = [sum(singleDf['MuSpike']), sum(singleDf['MuE1']), sum(singleDf['MuE2']), sum(singleDf['MuE3']), sum(singleDf['MuFi']), sum(singleDf['MuIc'])]
    
    plt.clf()
    mNames= ['Pinchos','Terrestre', 'Distancia', 'Volador', 'Lanzallamas', 'Carámbanos'] #Nombres mas legibles
    plt.bar(mNames, ar, color=['#1565c0', '#ffb74d', "#19ea46","#e53935", "#d04cd7ff", "#000e6bff"]) #para que no se quede ese 0
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.25)
    #max = auxdf.plot(y=['TimTut', 'TimN1', 'TimN2', 'TimN3'], kind='bar')
    plt.title("Distribución de Causas de Muertes")
    plt.xlabel("Tipo obstáculo enemigo")
    plt.ylabel("Cantidad de muertes")
    plt.savefig('./Metricas/Metrica2.png')

def Metrica3():
    #Metrica 3
    mlabels = ['TimTut', 'TimN1', 'TimN2', 'TimN3']
    ar1=np.array([sum(singleDf['TimTut']),sum(singleDf['TimN1']),sum(singleDf['TimN2']),sum(singleDf['TimN3'])])    
    ar2 = np.array([len(singleDf[singleDf['TimTut'] != 0]),len(singleDf[singleDf['TimN1'] != 0]),len(singleDf[singleDf['TimN2'] != 0]),len(singleDf[singleDf['TimN3'] != 0])])
    ar2[ar2==0]=1
    ar= (ar1/ar2) / 60000 # pasamos a minutos para que sea mas legible
    
    auxdf = pd.DataFrame(columns = mlabels)
    auxdf.loc[0] = ar
    plt.clf()

    mNames= ['Tutorial', 'Nivel 1', 'Nivel 2', 'Nivel 3'] #Nombres mas legibles
    plt.bar(mNames, ar, color=['#1565c0', '#ffb74d', "#19ea46",'#e53935']) #para que no se quede ese 0

    #max = auxdf.plot(y=['TimTut', 'TimN1', 'TimN2', 'TimN3'], kind='bar')
    plt.title("Distribución de Tiempo tardado por Nivel")
    plt.xlabel("Niveles")
    plt.ylabel("Tiempo Medio (Minutos)")
    plt.savefig('./Metricas/Metrica3.png')

def Metrica4():
    #Metrica 4
    mlabels = ['AciertosDisparos', 'FallosDisparo']
    ar = [sum(singleDf['DisAc']), sum(singleDf['Dis']) - sum(singleDf['DisAc'])]
    
    if(sum(singleDf['Dis']) > 0):   #Comprobar que al menos se ha disparado una vez para evitar fallos con el pie chart
        plt.clf()
        plt.pie(ar, labels = mlabels, startangle = 90)
        plt.title("Tasa de Aciertos y fallos de los disparos del jugador")
        plt.savefig('./Metricas/Metrica4.png')

def Metrica5():
    #Metrica 6
    mlabels = ['AciertosMelee', 'FallosMelee']
    ar = [sum(singleDf['MelAc']), sum(singleDf['Mel']) - sum(singleDf['MelAc'])]
    
    if(sum(singleDf['Dis']) > 0):   #Comprobar que al menos se ha atacado con melee una vez para evitar fallos con el pie chart
        plt.clf()
        plt.pie(ar, labels = mlabels, startangle = 90)
        plt.title("Tasa de Aciertos y fallos de ataques a melee del jugador")
        plt.savefig('./Metricas/Metrica5.png')

def Metrica6():
    #Metrica 6
    mlabels = ['DamTut','DamN1','DamN2','DamN3']
    auxdf = pd.DataFrame(columns = mlabels)
    ar = [sum(singleDf['DamTut']), sum(singleDf['DamN1']), sum(singleDf['DamN2']), sum(singleDf['DamN3'])]
    
    auxdf.loc[0] = ar

    plt.clf()
    mNames= ['Tutorial', 'Nivel 1', 'Nivel 2', 'Nivel 3'] #Nombres mas legibles
    plt.bar(mNames, ar, color=['#1565c0', '#ffb74d', "#19ea46",'#e53935'])
    #max = auxdf.plot(y=['DamTut','DamN1','DamN2','DamN3'], kind='bar')

    plt.title("Distribución de Daño recibido por el jugador en cada nivel")
    plt.xlabel("Niveles")
    plt.ylabel("Cantidad de puntos de vida")
    plt.savefig('./Metricas/Metrica6.png')

def Metrica7():
    #Metrica 7
    mlabels = ['DamE1', 'DamE2', 'DamE3', 'DamFi', 'DamIc']
    ar = [sum(singleDf['DamE1']), sum(singleDf['DamE2']), sum(singleDf['DamE3']), sum(singleDf['DamFi']), sum(singleDf['DamIc'])]
    auxdf = pd.DataFrame(columns = mlabels)
    
    auxdf.loc[0] = ar
    
    plt.clf()
    mNames= ['Terrestre', 'Distancia', 'Volador', 'Lanzallamas', 'Carámbanos'] #Nombres mas legibles
    plt.bar(mNames, ar, color=['#1565c0', '#ffb74d', "#19ea46",'#e53935', "#d04cd7ff"], align='center')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.25)

    #max = auxdf.plot(y=['DamE1', 'DamE2', 'DamE3', 'DamFi', 'DamIc'], kind='bar')
    plt.title("Distribución de daño recibido por el jugador por causa")
    plt.xlabel("Tipos enemigos")
    plt.ylabel("Cantidad de puntos de vida")
    plt.savefig('./Metricas/Metrica7.png')

def Metrica8():
    #Metrica 8
    mlabels = ['FreqHeal']
    freq_heal_indv = singleDf['Heal'] / (singleDf['SesTime'] / 60000) #Curas por minuto (paso los milisegundos a minutos)

    #medias de las frecuencias de todos los jugadores
    media = freq_heal_indv.mean()

    auxdf = pd.DataFrame(columns = mlabels)
    auxdf.loc[0] = media
    max = auxdf.plot(y=['FreqHeal'], kind='bar')
    plt.title("Media de cuanto se cura cada jugador por minuto")
    plt.savefig('./Metricas/Metrica8.png')

def Metrica9():
    # Métrica 9: Proporción de curación malgastada
    mlabels = ['TotalWastedHeal','TotalNonWastedHeal','TotalHeal']
    auxdf = pd.DataFrame(columns = mlabels)

    ar=[sum(singleDf['OvHeal']),sum(singleDf['AmountHeal'])-sum(singleDf['OvHeal']),sum(singleDf['AmountHeal'])]
    auxdf.loc[0] = ar

    plt.clf()
    mNames= ['Curación malgastada', 'Curación útil', 'Curacion total'] #Nombres mas legibles
    plt.bar(mNames, ar, color=['#1565c0', '#ffb74d', "#19ea46"])
    plt.ylim(0,1000)
    #ax = auxdf.plot(y= ['TotalWastedHeal','TotalNonWastedHeal','TotalHeal'], kind='bar')
    #ax.set_ylim(0,1000) #Para ver el resultado como si fuera un porcentaje
    plt.title("Tasas de curación")
    plt.xlabel("Tipos de curación")
    plt.ylabel("Cantidad de puntos de vida")
    plt.savefig('./Metricas/Metrica9.png')

def CallAllMetrics():
    #Muertes por nivel
    Metrica1()
    #Causas de muertes
    Metrica3()
    #Tiempo tardado por nivel
    Metrica4()
    #Aciertos y fallos de disparos
    Metrica5()
    #Aciertos y fallos de ataques melee
    Metrica6()
    #Daño recibido por nivel
    Metrica7()
    #Causas de daño
    Metrica8()
    #Curaciones por minuto
    Metrica9()
    #Curación malgastada
    Metrica10()

def TratamientoDatos(i, jug):

    dataJug = {key: 0 for key in col_names}
    dataJug['ID']='name' + str(i)
    for event in event_names:
        currEvent=jug[i][jug[i]["type"]==event]
        if(len(currEvent)>0):
            TratamientoEventos(jug, currEvent, event, dataJug)
    return dataJug

def TratamientoEventos(jug, currEvent, event, dataJug):
    match event:
                case "playerDeath":
                    #se hace un for para recorrer las labels del numero de muertes de cada nivel (MuTut, MuN1, etc)
                    for j in range(4):
                        dataJug[col_names[1+j]]=len(currEvent[currEvent["levelID"]==j+2])
                    #se hace un for para recorrer las labels de las causas de muerte (MuE1, MuE2,etc)
                    for j in range(6):
                        dataJug[col_names[5+j]]=len(currEvent[currEvent["deathCause"]==j])      
                case "playShot":
                    dataJug['Dis']=len(currEvent)     
                case "enBulHit": 
                    dataJug['DisAc']=len(currEvent)
                case "playMel":
                    dataJug['Mel']=len(currEvent) 
                case "enMelHit":
                    dataJug['MelAc']=len(currEvent) 
                case "playerHit":
                    #se hace un for para recorrer las labels de la cantidad de daño que se recibe por Nivel(DamTut, DamN1, etc)
                    for j in range(4):
                         dataJug[col_names[15+j]]=sum(currEvent[currEvent["levelID"]==j+2]["hitDamage"].values.tolist())
                    #se hace un for para recorrer las labels de la cantidad de daño que se recibe por causa(DamE1,DamE2, etc)
                    for j in range(6):
                        dataJug[col_names[19+j]]=sum(currEvent[currEvent["hitCause"]==j]["hitDamage"].values.tolist())
                case "playerHeal":
                    dataJug['Heal'] =len(currEvent) 
                    prevHealth=sum(currEvent["previousHealth"].values.tolist()) 
                    healAmount=sum(currEvent["healingAmount"].values.tolist()) 
                    finalHealth=sum(currEvent["finalHealth"].values.tolist())
                    dataJug['OvHeal']=prevHealth+healAmount-finalHealth
                    dataJug['AmountHeal'] = healAmount
                case "sesStart":
                    dataJug['ISesTime']= currEvent["time"].values[0]
                case "sesEnd":
                    dataJug['SesTime']= currEvent["time"].values[0]
                case "playerEnd":
                    for j in range(4):
                        if(len (currEvent[currEvent["levelID"]==2+j]) > 0):
                            dataJug[col_names[28+j]]= currEvent[currEvent["levelID"]==2+j]["time"].values[0]-dataJug[col_names[27+j]]
             

def Main():
    for i in range(len(json_file_names)):
        jsonList[i]=pd.read_json(path_to_json_files+json_file_names[i])

    #En esta celda es donde haremos el for por cada jugador (sessionID) distinto.
    #Si lo hacemos bien podemos usar las librerias para ahorrarnos el trabajo.

    jug = jsonList
    for i in range(len(jug)):
       singleDf.loc[i] = TratamientoDatos(i, jug)
    

    CallAllMetrics()

Main()