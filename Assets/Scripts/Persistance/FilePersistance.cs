using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

//Peristencia en disco
public class FilePersistance : IPersistance { 
    public void Send()
    {
        
    }

    public void Flush()
    {

        Debug.Log("Se estan guardando los eventos en el disco");
        //Logica para guardar en disco los eventos...


    }
}
