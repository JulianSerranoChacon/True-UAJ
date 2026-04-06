public class PlayerShoot : TrackerEvent
{
    public PlayerShoot() { }

    public override string ToJson()
    {
        return "{\ntype: playShot\n" + this.parentToJson() + "\n}";
    }
}
