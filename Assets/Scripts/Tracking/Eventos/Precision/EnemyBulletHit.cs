public class EnemyBulletHit : TrackerEvent
{
    public EnemyBulletHit() { }

    public override string ToJson()
    {
        return "{\ntype: enBulHit\n" + this.parentToJson() + "\n}";
    }
}
