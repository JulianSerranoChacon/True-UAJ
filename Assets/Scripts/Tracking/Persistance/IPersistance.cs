using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//Interfaz del tipo de sistema de persistencia a implementar
public abstract class IPersistance
{
    protected CircularBuffer<Event> CBuffer;
    protected const int QueueSize = 500;
    public void Init()
    {
        CBuffer=new CircularBuffer<Event>(QueueSize);
    }
   abstract public void Send(Event ev);

    //Metodo para el volacado de los datos de la cola para persistir los datos
    abstract public void Flush();
}
