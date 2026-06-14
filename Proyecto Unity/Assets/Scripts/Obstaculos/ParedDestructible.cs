using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ParedDestructible : MonoBehaviour
{
    #region parameters && references
    private Animator _animator;

    [SerializeField] private int _maxHealth = 100;     //Vida m?xima de la pared.
    public int _currentHealth { get; private set; }

    [SerializeField] private float _coolDownDeathAnim;

    [SerializeField] private float _cooldownDamagedColor;

    private float _initialCooldownDamagedColor;

    [SerializeField] private AudioClip _hurt;
    [SerializeField] private AudioClip _dead;

    public bool _death { get; private set; }
    private bool _damagedC; //Variable que gestiona cuando se puede activar el color de dañado en el EnemyStateManager

    [SerializeField]
    private Color[] _colores;   //Array de colores de la pared

    [SerializeField]
    private Renderer _renderC; //Renderiza el color de la pared

    #endregion

    #region methods
    public void TakeDamage(int damage)
    //M?todo para que el enemigo reciba da?o.
    //Cuando la vida quede a 0 o menos, el enemigo muere.
    {
        _currentHealth -= damage;
        _damagedC = true;

        //GetComponent<AudioSource>().PlayOneShot(_hurt);
        //Animaci?n de recibir da?o.

        if (_currentHealth <= 0)
        {
            Die();
        }
    }

    private void Die()
    //M?todo para que se "destrulla" la pared
    {
        _death = true;
        GetComponent<Collider2D>().isTrigger = true;
        GetComponent<AudioSource>().PlayOneShot(_dead);

    }
    #endregion

    #region collisions methods

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.GetComponent<BulletCollisionComponent>() != null && collision.gameObject.GetComponent<BulletCollisionComponent>()._normalBulletValue != 0)
        {
            TakeDamage(collision.gameObject.GetComponent<BulletCollisionComponent>()._normalBulletValue);
            GetComponent<AudioSource>().PlayOneShot(_hurt);
        }
    }
    #endregion

    private void Start()
    {
        //Al comienzo, el enemigo comienza con m?xima vida.
        _currentHealth = _maxHealth;
        _death = false;
        _damagedC = false;
        _animator = GetComponent<Animator>();
        _initialCooldownDamagedColor = _cooldownDamagedColor;
    }

    private void Update()
    {
        //Debug.Log(_currentHealth);
        _animator.SetBool("_death", _death);

        if (_damagedC)
        {
            _renderC.material.color = _colores[1]; //Color de cuando la pared es golpeada (feedback visual)
            _cooldownDamagedColor -= Time.deltaTime;
            if (_cooldownDamagedColor <= 0)
            {
                _damagedC = false;
            }
        }
        else
        {
            _renderC.material.color = _colores[0]; //color original
            _cooldownDamagedColor = _initialCooldownDamagedColor;
        }

        if (_death)
        {
            _coolDownDeathAnim -= Time.deltaTime;

            if (_coolDownDeathAnim <= 0)
            {
                Destroy(gameObject);
            }
        }
    }
}
