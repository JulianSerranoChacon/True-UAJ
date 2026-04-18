using System;
using System.IO;
using UnityEngine;

//Interfaz del tipo de sistema de persistencia a implementar
public abstract class IPersistance
{
    protected StreamWriter sw;
    protected ISerializer serializer;
    protected bool fileNull = false;
    public void Init(ISerializer Is, String fileName)
    {
        serializer = Is;
        try
        {
            sw = new StreamWriter(Application.dataPath + "/Sessions/"+fileName+".json", true);
        }
        catch (ArgumentNullException e)
        {
            Debug.LogError(e.Message);
            fileNull = true;
        }
    }
    public void Close()
    {
        if (!fileNull)
        {
            sw.Close();
        }
    }
    //Metodo para el volacado de los datos de la cola para persistir los datos
    abstract public void Flush(CircularBuffer<TrackerEvent> evq);
}
