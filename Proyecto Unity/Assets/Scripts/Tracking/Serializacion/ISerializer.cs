using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class ISerializer
{
    abstract public string SerializeEvent(TrackerEvent ev);

    abstract public string SerializeTrackingQueue(CircularBuffer<TrackerEvent> evQ);
}
