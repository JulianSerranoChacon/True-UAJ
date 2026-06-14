using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ServerPersistance : IPersistance
{
    //Como no usamos Server Persistance tenemos estos metodos vacios
    //Si expandiesemos la practica para usarlo, llenariamos estos metodos
    override public void Init(ISerializer Is, String fileName)
    {
    }

    override public void Close()
    {
    }
    override public void Flush(CircularBuffer<TrackerEvent> evq)
    {
        Debug.Log("Se estan guardando los eventos en el servidor...");
        //Logica para guardar en servidor los eventos...
    }
}
