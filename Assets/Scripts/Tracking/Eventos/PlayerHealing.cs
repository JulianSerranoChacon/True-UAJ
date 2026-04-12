public class PlayerHealing : TrackerEvent
{
    private float previousHealth;
    private float healingAmount;
    private float finalHealth;

    #region Bean
    public PlayerHealing() { }

    public float PreviousHealth
    {
        get { return previousHealth; }
        set { previousHealth = value; }
    }

    public float HealingAmount
    {
        get { return healingAmount; }
        set { healingAmount = value; }
    }

    public float FinalHealth
    {
        get { return finalHealth; }
        set { finalHealth = value; }
    }
    #endregion

    public override string ToJson()
    {        
        return "{\ntype\": \"playerHeal\"\n" + this.parentToJson() + "\n\"previousHealth\": " + previousHealth + "\n\"healingAmount\": " + healingAmount + "\n\"finalHealth\": " + finalHealth + "\n}";
    }
}
