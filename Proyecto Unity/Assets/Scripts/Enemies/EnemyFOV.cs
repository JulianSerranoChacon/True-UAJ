//Parte del c�digo fue obtenido del siguiente video https://www.youtube.com/watch?v=lV47ED8h61k

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyFOV : MonoBehaviour
{
    #region parameters 
    [SerializeField][Range(0f, 360f)] private float _visionAngle = 45f; //El �ngulo de visi�n del enemigo.
    [SerializeField] private float _visionDistance = 10f;               //La m�xima distancia de nuestro cono de visi�n.

    [SerializeField] private float _coolDownChase;
    float _initialCoolDownChase;
    private bool _detected;                        //Booleano que determina si el enemigo ha detectado al jugador
    private bool _detectedSFX;                        //Booleano que determina si el enemigo ha detectado al jugador (SONIDO)
    private bool _attackSFX;
    private bool _stillChase;
    #endregion

    #region references
    private GameObject _player;
    private Animator _animator;

    [SerializeField] private AudioClip _detectSFX;
    #endregion

    #region getter && setters
    public bool GetDetected()
    {
        return _detected;
    }

    public void SetDetected(bool detected)
    {
        _detected = detected;
    }
    public bool GetAttackSFX()
    {
        return _attackSFX;
    }
    #endregion

    #region methods
    Vector3 PointforAngles(float angles, float distance)
    //Devuelve los puntos que forman los vectoers directrores del �ngulo.
    {
        return transform.TransformDirection(new Vector2(Mathf.Cos(angles * Mathf.Deg2Rad), Mathf.Sin(angles * Mathf.Deg2Rad)) * distance);
    }

    private void OnDrawGizmos()
    //M�todo para ver el cono de visi�n, dibujando el �ngulo
    //no se hace nada si el �ngulo es menor que cero
    {
        if (_visionAngle <= 0f) return;
        float halfVisionAngle = _visionAngle * 0.5f;
        Vector2 p1, p2;
        p1 = PointforAngles(halfVisionAngle, _visionDistance);
        p2 = PointforAngles(-halfVisionAngle, _visionDistance);

        Gizmos.color = Color.red;

        Gizmos.DrawLine(transform.position, (Vector2)transform.position + p1);
        Gizmos.DrawLine(transform.position, (Vector2)transform.position + p2);
        Gizmos.DrawRay(transform.position, transform.right * 4f);
    }
    #endregion

    void Start()
    {
        _animator = GetComponent<Animator>();
        _player = GameManager.instance._player;
        _detected = false;
        _detectedSFX = true;
        _attackSFX = false;
        _stillChase = false;
        _initialCoolDownChase = _coolDownChase;
    }

    void Update()
    {
        if (_detectedSFX && _detected)
        {
            GetComponent<AudioSource>().PlayOneShot(_detectSFX);
            _detectedSFX = false;
        }
        else if (!_detected)
        {
            _detectedSFX = true;
        }

        if (_stillChase)
        {
            _coolDownChase -= Time.deltaTime;
            if (_coolDownChase <= 0)
            {
                _stillChase = false;
                _detected = false;
                _attackSFX = false;
                _coolDownChase = _initialCoolDownChase;
            }
        }

        _animator.SetBool("_run", _detected); //no lo encuentra. Si lo encuentra, no lo toques 
        //Debug.Log(_detected);
        if (_player != null)
        {
            // El vector que indica la distancia del jugador al enemigo.
            Vector2 playerVector = _player.transform.position - transform.position;

            float angle = Vector3.Angle(playerVector.normalized, transform.right);
            float halfAngle = _visionAngle * 0.5f;
            float distance = playerVector.magnitude;

            if (angle < halfAngle && distance < _visionDistance)
            {
                _stillChase = false;
                _detected = true;
                _attackSFX = true;
                _coolDownChase = _initialCoolDownChase;
            }
            else
            {
                _stillChase = true;
                //_detected = false;
                //_attackSFX = false;
            }
        }
    }
}