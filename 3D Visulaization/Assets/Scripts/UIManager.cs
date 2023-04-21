//This script is responsible for mananging the interface 

using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    [SerializeField] private TMP_Dropdown yearDropdown; // A dropdown UI element for selecting the year
    [SerializeField] private TMP_Dropdown weekDropdown; // A dropdown UI element for selecting the week
    [SerializeField] private TMP_InputField hourInput; // An input field for setting the hour
    [SerializeField] private TMP_Dropdown dataModeDropdown; // A dropdown UI element for selecting the data mode (Year or Day)
    [SerializeField] private GameObject speedUI;
    [SerializeField] private TMP_InputField speedInput; // An input field for setting the playback speed

    [SerializeField] private Button playButton; // A button UI element for playing the visualization
    [SerializeField] private Button pauseButton; // A button UI element for pausing the visualization

    [SerializeField] private TextMeshProUGUI number1Text; // A text UI element for displaying a data value
    [SerializeField] private TextMeshProUGUI number2Text; // A text UI element for displaying a data value

    [SerializeField] private RectTransform dataValueLabel; // A UI element for displaying a data value on hover
    [SerializeField] private TextMeshProUGUI dataValueText; // A text UI element for displaying a data value on hover

    [SerializeField] private UIImageGradient minorGradientImage; // A UI element for displaying a color gradient for minor roads
    [SerializeField] private UIImageGradient majorGradientImage; // A UI element for displaying a color gradient for major roads

    [SerializeField] private TextMeshProUGUI maxText; // A text UI element for displaying the maximum data value

    private bool hoverMinorRoad = false; // A boolean for tracking whether the user is hovering over a minor road

    public static UIManager Instance;

    private void Awake()
    {
        Instance = this;
        dataModeDropdown.onValueChanged.AddListener(OnDataModeValueChanged); // Add a listener for changes to the data mode dropdown
        yearDropdown.onValueChanged.AddListener(OnYearValueChanged); // Add a listener for changes to the year dropdown
        weekDropdown.onValueChanged.AddListener(OnWeekValueChanged); // Add a listener for changes to the week dropdown
        dataModeDropdown.value = 0; // Set the initial value of the data mode dropdown
        speedInput.onEndEdit.AddListener(OnChangeSpeed); // Add a listener for changes to the speed input field
        playButton.onClick.AddListener(OnPlayBtnClick); // Add a listener for clicks on the play button
        pauseButton.onClick.AddListener(OnPauseBtnClick); // Add a listener for clicks on the pause button

        playButton.gameObject.SetActive(true); // Set the play button to be initially active
        pauseButton.gameObject.SetActive(false); // Set the pause button to be initially inactive

        weekDropdown.interactable = false; // Disable the week dropdown by default

        dataValueLabel.gameObject.SetActive(false); // Hide the data value label by default
    }

    // Set the gradient colors for the major and minor roads at the start of the scene
    private void Start()
    {
        minorGradientImage.gradientColor = MapRoadVisualManager.Instance.MinorGradient;
        majorGradientImage.gradientColor = MapRoadVisualManager.Instance.MajorGradient;
    }

    // Update the UI elements every frame
    private void Update()
    {
        float hourFloat = MapRoadVisualManager.Instance.CurrentHour;
        int hourInt = (int)hourFloat;
        int minutesInt = (int)((hourFloat - hourInt) * 60);
        hourInput.text = hourInt.ToString("00") + ":" + minutesInt.ToString("00");
        if (MapRoadVisualManager.Instance.VMode == MapRoadVisualManager.VisualMode.Year)
        {
            weekDropdown.interactable = false; //Lock the option for changing week variable
            weekDropdown.value = MapRoadVisualManager.Instance.WeekDay; //持续更新周时间
        }
        number1Text.text = MapRoadVisualManager.Instance.MajorRoadsCurrentValue.ToString();
        number2Text.text = MapRoadVisualManager.Instance.MinorRoadsCurrentValue.ToString();
        maxText.text = MapRoadVisualManager.Instance.MaxValue.ToString("f2");
        if (dataValueLabel.gameObject.activeSelf)
        {
            dataValueLabel.position = Input.mousePosition;
            if (hoverMinorRoad)
                dataValueText.text = MapRoadVisualManager.Instance.MinorRoadsCurrentValue.ToString();
            else
                dataValueText.text = MapRoadVisualManager.Instance.MajorRoadsCurrentValue.ToString();
        }
    }

    //Hovering feature for minor road
    public void OnMouseHoverMinorRoad()
    {
        dataValueLabel.gameObject.SetActive(true);

        hoverMinorRoad = true;
    }
    //Hovering feature for major road
    public void OnMouseHoverMajorRoad()
    {
        dataValueLabel.gameObject.SetActive(true);
        hoverMinorRoad = false;
    }

    // This method is called when the mouse cursor exits the road area
    public void OnMouseExitRoad()
    {
        dataValueLabel.gameObject.SetActive(false);
    }

    // This method is called when the data mode dropdown value changes
    private void OnDataModeValueChanged(int dataMode)
    {
        if (dataMode == 0) //Year
        {
            MapRoadVisualManager.Instance.ChangeVisualMode(MapRoadVisualManager.VisualMode.Year);
            weekDropdown.interactable = false;
        }
        else if (dataMode == 1) //Day
        {
            MapRoadVisualManager.Instance.ChangeVisualMode(MapRoadVisualManager.VisualMode.Day); // Change visual mode to Day
            weekDropdown.value = 0;
            weekDropdown.interactable = true; // Enable weekDropdown to allow changing the week
        }
    }

    // This method is called when the week dropdown value changes
    private void OnWeekValueChanged(int week)
    {
        MapRoadVisualManager.Instance.SetWeekDay(week);
    }

    // This method is called when the year dropdown value changes
    private void OnYearValueChanged(int value)
    {
        MapRoadVisualManager.Instance.SetYear(2021 - value);
    }

    // This method is called when the speed input field value changes
    private void OnChangeSpeed(string speedString)
    {
        float speed;
        float.TryParse(speedString, out speed);
        MapRoadVisualManager.Instance.SetSpeed(speed);
    }

    // This method is called when the play button is clicked
    private void OnPlayBtnClick()
    {
        pauseButton.gameObject.SetActive(true);
        playButton.gameObject.SetActive(false);
        MapRoadVisualManager.Instance.IsPlaying = true;
    }


    // This method is called when the pause button is clicked
    private void OnPauseBtnClick()
    {
        playButton.gameObject.SetActive(true);
        pauseButton.gameObject.SetActive(false);
        MapRoadVisualManager.Instance.IsPlaying = false;
    }

}
