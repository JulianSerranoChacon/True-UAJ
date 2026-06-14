public class SesionEnd : TrackerEvent
{
    public SesionEnd() { }

    public override string ToJson()
    {
        return "{\n\"type\": \"sesEnd\"\n" + this.parentToJson() + "\n} \n] ";
    }
}
