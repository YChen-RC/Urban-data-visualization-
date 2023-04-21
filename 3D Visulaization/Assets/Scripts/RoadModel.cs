//Definning road model
//Two type minor road and major road
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RoadModel : MonoBehaviour
{
    public bool isMinorRoad = false;

    private void OnMouseEnter()
    {
        if (isMinorRoad)
            UIManager.Instance.OnMouseHoverMinorRoad();
        else
            UIManager.Instance.OnMouseHoverMajorRoad();
    }

    private void OnMouseExit()
    {
        UIManager.Instance.OnMouseExitRoad();
    }
}
