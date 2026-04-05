public class TrackerEvent 
{

    private int sessionID;
    private float timeStamp;

    public TrackerEvent() { }

    public int SessionID
    {
        get { return sessionID; }
        set { sessionID = value; }
    }

    public float TimeStamp
    {
        get { return timeStamp; }
        set { timeStamp = value; }  
    }
}
