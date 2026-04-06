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
        //TODO
        return "{\ntype: playerHit\n" + this.parentToJson() + "Lo que sea que vaya despues\n}";
    }
}
