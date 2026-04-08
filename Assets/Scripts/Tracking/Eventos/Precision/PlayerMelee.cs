public class PlayerMelee : TrackerEvent
{
    public PlayerMelee() { }

    public override string ToJson()
    {
        return "{\ntype\": \"playMel\"\n" + this.parentToJson() + "\n}";
    }
}
