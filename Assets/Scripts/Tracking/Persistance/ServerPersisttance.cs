using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ServerPersisttance : IPersistance
{
    public override void Init()
    {
        
    }
    override public void Send(Event ev)
    {

    }

    override public void Flush()
    {
        Debug.Log("Se estan guardando los eventos en el servidor...");
        //Logica para guardar en servidor los eventos...
    }
}
