public class PlayerShoot : TrackerEvent
{
    public PlayerShoot() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"playShot\"\n" + this.parentToJson() + "\n}\n,";
    }
}
