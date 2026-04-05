using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

//Peristencia en disco
public class FilePersistance : IPersistance { 

    //Habria que implementar aqui la cola circular

   override public void Send(Event ev)
    {
        //Aqui habria que meter el evento en la cola circular y
        //definir la frecuencia con la que vamos a volcar los datos de dicha cola al disco...

    }

    override public void Flush()
    {
        Debug.Log("Se estan guardando los eventos en el disco");
        //Logica para guardar en disco los eventos...
        //Codigo de experimento de persistencia
        using (StreamWriter sw = new StreamWriter(Application.dataPath + "/NewTextFile.txt", true))
        {
            sw.WriteLine("This is a new text file!");
        }
        AssetDatabase.Refresh();

    }
}
