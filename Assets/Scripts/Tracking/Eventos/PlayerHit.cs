public class PlayerHit : TrackerEvent
{
    private int levelID;
    private float cordX;
    private float cordY;
    private cause hitCause;
    private float hitDamage;
    private float currentHealth;

    #region Bean
    public PlayerHit() { }

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

    public cause HitCause
    {
        get { return hitCause; }
        set { hitCause = value; }
    }

    public float HitDamage
    {
        get { return hitDamage; }
        set { hitDamage = value; }
    }

    public float CurrentHealth
    {
        get { return currentHealth; }
        set { currentHealth = value; }
    }
    #endregion

    public override string ToJson()
    {        
        return "{\n\"type\": \"playerHit\"\n" + this.parentToJson() + ",\n\"levelID\": " + levelID + ",\n\"cordX\": " + cordX + ",\n\"cordY\": " + cordY 
            + ",\n\"hitCause\": " + hitCause.ToString() + ",\n\"hitDamage\": " + hitDamage + ",\n\"currentHealth\": " + currentHealth + "\n}";
    }
}
