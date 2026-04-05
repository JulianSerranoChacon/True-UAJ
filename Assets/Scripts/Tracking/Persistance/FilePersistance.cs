using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

//Peristencia en disco
public class FilePersistance : IPersistance {

    CircularBuffer<Event> CBuffer;
    //Placeholder hasta que decidamos la frecuencia
    const int QUEUESIZE = 500;
    //Habria que implementar aqui la cola circular
    override public void Init()
    {
       CBuffer= new CircularBuffer<Event> (QUEUESIZE);
    }
   override public void Send(Event ev)
    {
        CBuffer.Add (ev);
        //Aqui habria que meter el evento en la cola circular y
        //definir la frecuencia con la que vamos a volcar los datos de dicha cola al disco...

    }

    override public void Flush()
    {
        Debug.Log("Se estan guardando los eventos en el disco");
        //Logica para guardar en disco los eventos...
        //Codigo de experimento de persistencia
        using (StreamWriter sw = new StreamWriter(Application.dataPath + "/NewTextFile.json", true))
        {
            sw.WriteLine("This is a new text file!");
        }
        AssetDatabase.Refresh();

    }
}
