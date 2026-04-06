public class SesionStart : TrackerEvent
{
    public SesionStart() { }

    public override string ToJson()
    {
        return "{\ntype: sesStart\n" + this.parentToJson() + "\n}";
    }
}
