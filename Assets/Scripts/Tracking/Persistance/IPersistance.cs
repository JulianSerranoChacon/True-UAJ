using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//Interfaz del tipo de sistema de persistencia a implementar
public interface IPersistance
{
    void Send();

    //Metodo para el volacado de los datos de la cola para persistir los datos
    void Flush();
}
