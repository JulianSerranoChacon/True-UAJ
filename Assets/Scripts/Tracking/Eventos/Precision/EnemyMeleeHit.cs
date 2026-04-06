public class EnemyMeleeHit : TrackerEvent
{
    public EnemyMeleeHit() { }

    public override string ToJson()
    {
        return "{\ntype: enMelHit\n" + this.parentToJson() + "\n}";
    }
}
