using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

//Peristencia en disco
public class FilePersistance : IPersistance {


    override public void Flush(CircularBuffer<TrackerEvent>evq)
    {
        if (!fileNull)
        {
            Debug.Log("Se estan guardando los eventos en el disco");
            //Logica para guardar en disco los eventos...
            //Codigo de experimento de persistencia
            string eventos = serializer.SerializeTrackingQueue(evq);
            sw.WriteLine(eventos);

            //AssetDatabase.Refresh();
        }

    }
}
