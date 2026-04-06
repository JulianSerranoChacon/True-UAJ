public class PlayerCheckPoint : TrackerEvent
{
    private int levelID;
    private int checkpointID;

    #region Bean
    public PlayerCheckPoint() { }

    public int LevelID
    {
        get { return levelID; }
        set { levelID = value; }
    }
    
    public int CheckpointID
    {
        get { return checkpointID; }
        set { checkpointID = value; }
    }
    #endregion

    public override string ToJson()
    {
        //TODO
        return "{\ntype: playerCP\n" + this.parentToJson() + "Lo que sea que vaya despues\n}";
    }
}
