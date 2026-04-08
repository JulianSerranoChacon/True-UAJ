public class EnemyMeleeHit : TrackerEvent
{
    public EnemyMeleeHit() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"enMelHit\"\n" + this.parentToJson() + "\n}";
    }
}
