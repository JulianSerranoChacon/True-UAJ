using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

//Peristencia en disco
public class FilePersistance : IPersistance {

    private StreamWriter sw;
    private bool fileNull = false;
    override  public void Init(ISerializer Is, String fileName)
    {
        serializer = Is;
        try
        {
            string dirPath = Path.Combine(Application.dataPath, "../../Datos Telemetria");

            if (!Directory.Exists(dirPath))
                Directory.CreateDirectory(dirPath);

            string fullPath = Path.Combine(dirPath, fileName);

            sw = new StreamWriter(fullPath + ".json", true);
        }
        catch (ArgumentNullException e)
        {
            Debug.LogError(e.Message);
            fileNull = true;
        }
    }
    override public void Close()
    {
        if (!fileNull && sw != null)
        {
            sw.Close();
            sw = null;
        }
    }
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
