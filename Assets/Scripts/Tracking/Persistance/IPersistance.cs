using System.IO;
using UnityEngine;

//Interfaz del tipo de sistema de persistencia a implementar
public abstract class IPersistance
{
    protected CircularBuffer<TrackerEvent> CBuffer;
    protected StreamWriter sw;
    protected ISerializer serializer;
    public void Init(ISerializer Is)
    {
        serializer = Is;
        sw = new StreamWriter(Application.dataPath + "/NewTextFile.json", true);
    }
   abstract public void Send(TrackerEvent ev);

    //Metodo para el volacado de los datos de la cola para persistir los datos
    abstract public void Flush(CircularBuffer<TrackerEvent> evq);
}
