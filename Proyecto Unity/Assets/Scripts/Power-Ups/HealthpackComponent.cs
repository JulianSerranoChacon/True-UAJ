using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HealthpackComponent : MonoBehaviour
{
    #region references
    private MightyLifeComponent _myMightyLifeComponent;
    #endregion

    #region parameters
    [SerializeField] private float _sanation;
    #endregion

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject == GameManager.instance._player)
        {
            // referencias en la colision
            _myMightyLifeComponent =collision.gameObject.GetComponent<MightyLifeComponent>();

                _myMightyLifeComponent.TakeDamage(-_sanation);
 
            Destroy(gameObject);
        }
    }
}
