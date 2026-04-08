using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JsonSerializer : ISerializer
{
     
    override public string SerializeEvent(Event ev)
    {
        return JsonUtility.ToJson(ev);
    }

    public override string SerializeTrackingQueue(CircularBuffer<TrackerEvent> evQ)
    {
        //Copiarlo a lo mejor para no vaciar la cola de eventos???
        string result = "{\n";

        while (evQ.Peek() != null)
        {
            result += evQ.Read().ToJson();
        }

        result += "}";

        return result;
    }
}
