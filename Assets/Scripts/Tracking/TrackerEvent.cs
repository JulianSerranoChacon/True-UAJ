public class TrackerEvent 
{

    private long sessionID;
    private double timeStamp;

    #region Bean 
    //Constructor vacio, getters y setters publicos - Patron Bean/POYO
    public TrackerEvent() { }

    public long SessionID
    {
        get { return sessionID; }
        set { sessionID = value; }
    }

    public double TimeStamp
    {
        get { return timeStamp; }
        set { timeStamp = value; }  
    }
    #endregion

    #region Serializacion
    // Metodo padre del metodo de serializacion
    // Virtual para poder sobreescrinir
    virtual public string ToJson()
    {
        return "{\n\"type\": \"father\"\n" + this.parentToJson() + "\n}"; 
    }

    // Metodo para sacar los datos de la clase padre
    // y no tener que repetir texto
    protected string parentToJson()
    {
        return "\"time\": " + timeStamp + ",\n\"sesID\": " + sessionID; 
    }
    #endregion
}