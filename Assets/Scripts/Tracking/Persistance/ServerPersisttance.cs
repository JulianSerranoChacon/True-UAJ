using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ServerPersisttance : IPersistance
{
    override public void Flush(CircularBuffer<TrackerEvent> evq)
    {
        Debug.Log("Se estan guardando los eventos en el servidor...");
        //Logica para guardar en servidor los eventos...
    }
}
