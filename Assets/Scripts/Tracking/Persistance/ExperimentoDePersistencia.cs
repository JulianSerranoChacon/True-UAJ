using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

public class ExperimentoDePersistencia : MonoBehaviour
{
    [MenuItem("Assets/Create/MISC/New Text File", priority = 100)]
public static void CreateNewTextFile()
    {
        using (StreamWriter sw = new StreamWriter(Application.dataPath + "/NewTextFile.txt", true))
        {
            sw.WriteLine("This is a new text file!");
        }
        AssetDatabase.Refresh();
    }
}
