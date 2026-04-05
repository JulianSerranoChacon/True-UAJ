using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JsonSerializer : ISerializer
{
     
    override public string SerializeEvent(Event ev)
    {
        return JsonUtility.ToJson(ev);
    }
}
