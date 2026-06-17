public class PlayerCheckPoint : TrackerEvent
{
    private int levelID;

    #region Bean
    public PlayerCheckPoint() { }
    public int LevelID
    {
        get { return levelID; }
        set { levelID = value; }
    }

    #endregion

    public override string ToJson()
    {        
        return "{\n\"type\": \"playerCP\"\n" + this.parentToJson() + ",\n\"levelID\": " + levelID + "\n}\n,";
    }
}
