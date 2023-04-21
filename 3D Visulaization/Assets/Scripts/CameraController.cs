using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    [SerializeField] private float horizontalSensivity = 1;
    [SerializeField] private float verticalSensivity = 1;

    public static CameraController Instance;


    private void Awake()
    {
        Instance = this;
    }

    private void Update()
    {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        transform.Translate(h * transform.right * Time.deltaTime * horizontalSensivity * 10, Space.World);
        transform.Translate(v * transform.forward * Time.deltaTime * verticalSensivity * 10, Space.World);
        if (Input.GetMouseButton(0))
        {

        }
    }

    public void Rotate(Vector2 input)
    {
        transform.Rotate(-transform.right * input.y * Time.deltaTime * 10, Space.World);
        transform.Rotate(Vector3.up * Time.deltaTime * input.x * 10, Space.World);
    }
}
