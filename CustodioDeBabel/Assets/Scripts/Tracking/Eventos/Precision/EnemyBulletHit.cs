public class EnemyBulletHit : TrackerEvent
{
    public EnemyBulletHit() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"enBulHit\"\n" + this.parentToJson() + "\n}";
    }
}
