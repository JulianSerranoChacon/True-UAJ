public class SesionStart : TrackerEvent
{
    public SesionStart() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"sesStart\"\n" + this.parentToJson() + "\n}";
    }
}
