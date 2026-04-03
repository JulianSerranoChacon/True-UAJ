using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class ISerializer
{
    abstract public string SerializeEvent(Event ev);
}
