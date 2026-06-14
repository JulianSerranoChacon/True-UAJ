using System.Globalization;

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
        return "{\n\"type\": \"playerEnd\"\n" + this.parentToJson() + ",\n\"levelID\": " + levelID + ",\n\"currentHealth\": " + 
            currentHealth.ToString(CultureInfo.CreateSpecificCulture("en-GB")) + "\n}\n,";
    }
}
