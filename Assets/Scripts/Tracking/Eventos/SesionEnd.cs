public class SesionEnd : TrackerEvent
{
    public SesionEnd() { }

    public override string ToJson()
    {
        return "{\ntype: sesEnd\n" + this.parentToJson() + "\n}";
    }
}
