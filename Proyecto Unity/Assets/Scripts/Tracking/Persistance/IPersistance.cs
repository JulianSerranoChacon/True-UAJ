using System;
using System.IO;
using UnityEngine;

//Interfaz del tipo de sistema de persistencia a implementar
public abstract class IPersistance
{
    protected ISerializer serializer;
    abstract public void Init(ISerializer Is, String fileName);
    abstract public void Close();
    //Metodo para el volacado de los datos de la cola para persistir los datos
    abstract public void Flush(CircularBuffer<TrackerEvent> evq);
}
