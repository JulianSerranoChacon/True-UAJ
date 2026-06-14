public class SesionStart : TrackerEvent
{
    public SesionStart() { }

    public override string ToJson()
    {
        return "[\n{\n\"type\": \"sesStart\"\n" + this.parentToJson() + "\n}\n,";
    }
}
