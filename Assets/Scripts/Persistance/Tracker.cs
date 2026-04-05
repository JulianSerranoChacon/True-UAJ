using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//Clase que representa el Tracker de eventos
public class Tracker
{
    //Instancia unica del tracker (patron Singleton)
    private static Tracker _instance;

    //Lista con referencias a las estrategias de persistencia actual (en disco o red)
    List<IPersistance> _persistenceObjects;

    //Lista de "escuchadores" de eventos especializados (no se muy bien para que se usa aun...)
    List<int> _activeTrackers;


    //Acceso a la instancia unica del tracker
    public static Tracker Instance
    {
        get
        {
            if(_instance == null)
            {
                _instance = new Tracker();
                _instance.Init();
            }

            return _instance;
        }
    }

    //Inicializacion del tracker
    public void Init()
    {
        //Seteamos el tipo de estrategia de persistencia que vayamos a usar
        //De momento solo persistencia en disco, si da tiempo, en red
        _persistenceObjects.Add(new FilePersistance());

        //añadimos los listeners de eventos
        //ejemplo : _activeTrackers.Add(new PrgressionTracker())
    }

    //Metodo que se encarga de cerrar el tracker
    public void End()
    {
        //Antes debemos asegurarnos de que no queden elementos en la cola.. hacemos el volcado de los datos que falten
        foreach(var stratergy in _persistenceObjects)
        {
            stratergy.Flush();
        }
    }

    //Metodo para enviar el evento a la cola de envios
    public void TrackEvent(Event ev)
    {
        //El tracker recorre todas las estrategias de persistencia
        foreach (var stratergy in _persistenceObjects)
        {
            stratergy.Send(ev);
        }
    }


}
