//This script is for implementing the free camera feature
//When the program is running, user can use mouse to drag to explore the City model and data visualization

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class DragArea : MonoBehaviour, IBeginDragHandler, IDragHandler, IEndDragHandler
{

    // This function is called while the drag is ongoing
    public void OnBeginDrag(PointerEventData eventData)
    {
        
    }

    // This function is called while the drag is ongoing
    public void OnDrag(PointerEventData eventData)
    {
        // Rotate the camera based on the change in pointer position
        CameraController.Instance.Rotate(eventData.delta);
    }

    // This function is called when the drag event ends
    public void OnEndDrag(PointerEventData eventData)
    {
       
    }
}
