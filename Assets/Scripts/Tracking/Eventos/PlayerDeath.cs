public enum cause { Spikes, Enem1, Enem2, Enem3, Ice, Fire};

public class PlayerDeath : TrackerEvent
{
    private int levelID;
    private float cordX;
    private float cordY;
    private cause deathCause;

    #region Bean
    public PlayerDeath() { }

    public int LevelID
    {
        get { return levelID; }
        set { levelID = value; }
    }

    public float CordX
    {
        get { return cordX; }
        set { cordX = value; }
    }

    public float CordY
    {
        get { return cordY; }
        set { cordY = value; }
    }

    public cause DeathCause
    {
        get { return deathCause; }
        set { deathCause = value; }
    }
    #endregion

    public override string ToJson()
    {
        //TODO
        return "{\ntype: playerDeath\n" + this.parentToJson() + "Lo que sea que vaya despues\n}";
    }
}
