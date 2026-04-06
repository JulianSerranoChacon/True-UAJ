public class PlayerEnd : TrackerEvent
{
    private int levelID;
    private float currentHealth;

    #region Bean
    public PlayerEnd() { }

    public int LevelID
    {
        get { return levelID; }
        set { levelID = value; }
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
        return "{\ntype: playerEnd\n" + this.parentToJson() + "Lo que sea que vaya despues\n}";
    }
}
