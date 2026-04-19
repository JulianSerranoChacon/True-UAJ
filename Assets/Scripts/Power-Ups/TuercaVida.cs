using UnityEngine;

public class TuercaVida : MonoBehaviour
{
    #region References
    //Referencia al componente de la vida de Mighty.
    MightyLifeComponent _myMightyLifeComponent;

    //La vida que le sube a Mighty.
    [SerializeField] private float _healthbonus = 15f;
    #endregion

    //El Awake se llama antes que el Start.
    private void Awake()
    {
        _myMightyLifeComponent= GetComponent<MightyLifeComponent>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        //Si es MIGHTY el que toca...
        if(collision.gameObject == GameManager.instance._player)
        {
                //Hacer que se le sume a la vida actual el "healthbonus". La vida sumada hacerlo en negativo porque es "Hacer daño" pero invertido.
                _myMightyLifeComponent.TakeDamage(-_healthbonus);

                //Quita el objeto de curación de la escena.
                Destroy(gameObject);
        }
    }
}
