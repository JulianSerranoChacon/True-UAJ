public class PlayerMelee : TrackerEvent
{
    public PlayerMelee() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"playMel\"\n" + this.parentToJson() + "\n}\n,";
    }
}
