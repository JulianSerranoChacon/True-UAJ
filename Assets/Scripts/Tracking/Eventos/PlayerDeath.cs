using System.Globalization;

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
        return "{\n\"type\": \"playerDeath\"\n" + this.parentToJson() + ",\n\"levelID\": " + levelID + ",\n\"coordX\": " + cordX.ToString(CultureInfo.CreateSpecificCulture("en-GB"))
            + ",\n\"coordY\": " + cordY.ToString(CultureInfo.CreateSpecificCulture("en-GB")) + ",\n\"deathCause\": " + (int)deathCause + "\n}\n,";
    }
}
