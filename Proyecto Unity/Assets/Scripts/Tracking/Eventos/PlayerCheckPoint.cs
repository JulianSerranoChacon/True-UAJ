public class PlayerCheckPoint : TrackerEvent
{
    private int levelID;

    #region Bean
    public PlayerCheckPoint() { }
    
    public int CheckpointID
    {
        get { return checkpointID; }
        set { checkpointID = value; }
    }
    #endregion

    public override string ToJson()
    {        
        return "{\n\"type\": \"playerCP\"\n" + this.parentToJson() + ",\n\"levelID\": " + levelID + ",\n}\n,";
    }
}
