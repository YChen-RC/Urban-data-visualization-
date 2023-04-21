//This script is responsible for the visualization of traffic data
using HighlightPlus;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

/// 
public class MapRoadVisualManager : MonoBehaviour
{
    [SerializeField] private HighlightEffect majorRoadsHighlight; //
    [SerializeField] private HighlightEffect minorRoadsHighlight; // 
    [SerializeField] private float timeSpeed = 1; //

    
    [Header("Color")]
    [SerializeField] private Gradient majorRoadsGradient; // color gradient 
    [SerializeField] private Gradient minorRoadsGradient; // color gradient
    [Space]
    // The current data in the map
    [Header("Realtime")]
    [SerializeField] private float currentHour; //The current hour in the map
    [SerializeField] private float majorRoadsCurrentValue; //Current major road traffic flow in the map
    [SerializeField] private float minorRoadsCurrentValue; //Current minor road traffic flow in the map
    [SerializeField] private Color32 majorRoadsCurrentColor;
    [SerializeField] private Color32 minorRoadsCurrentColor;
    [SerializeField] private bool playing = false;
    [SerializeField] private int year = 2021; //initalising the year 
    [SerializeField] private int weekDay = 0;
    //[SerializeField] private float minorToMajorRate = 23.8f / 2.6f; // Initialising the rate 
    [SerializeField] private float maxValue;

    [SerializeField] private List<float> dayData = new List<float>();

    [SerializeField] private VisualMode visualMode;

    public static MapRoadVisualManager Instance;


    private YearData yearData;
    private float weekDayDataValueAve = 0; 

    private MeshRenderer[] majorRoadsRenderers; //Array of render for major roads
    private MeshRenderer[] minorRoadsRenderers; //Array of render for minor roads

    // Two type of visualizing the data 
    public enum VisualMode 
    {
        Year, //By year
        Day, //By year of which day in the week
    }

    public bool IsPlaying { get { return playing; } set { playing = value; } }


    
    ///Getter 
    public float CurrentHour { get { return currentHour; } }
    public VisualMode VMode { get { return visualMode; } }
    public int WeekDay { get { return weekDay; } }
    public float MajorRoadsCurrentValue { get { return majorRoadsCurrentValue; } }
    public float MinorRoadsCurrentValue { get { return minorRoadsCurrentValue; } }
    public Gradient MajorGradient { get { return majorRoadsGradient; } }
    public Gradient MinorGradient { get { return minorRoadsGradient; } }
    public float MaxValue { get { return maxValue; } }


    // Render the road 
    private void Awake()
    {
        Instance = this;
        majorRoadsRenderers = majorRoadsHighlight.GetComponentsInChildren<MeshRenderer>();
        minorRoadsRenderers = minorRoadsHighlight.GetComponentsInChildren<MeshRenderer>();
    }

    private void Start()
    {
        Getdata();
    }

    private void Update()
    {
        if (!playing) return;

        UpdateVisual();
    }


    public void StartVisual()
    {
        playing = true;
        Array.ForEach(minorRoadsRenderers, r => r.enabled = true);
        Array.ForEach(minorRoadsRenderers, r => r.enabled = true);
        majorRoadsHighlight.enabled = true;
        minorRoadsHighlight.enabled = true;
        Getdata();
    }

    public void PauseVisual()
    {
        playing = false;
    }

    public void StopVisual()
    {
        playing = false;
        Array.ForEach(minorRoadsRenderers, r => r.enabled = false);
        Array.ForEach(minorRoadsRenderers, r => r.enabled = false);
        majorRoadsHighlight.enabled = false;
        minorRoadsHighlight.enabled = false;
    }

    //Get data for new day
    private void Getdata()
    {
        yearData = DataManager.Instance.GetYearData(year);
        maxValue = DataManager.Instance.MaxValue * yearData.MinorToMajorRate;
        //doing the search based on weekDay 
        dayData = yearData.weekDayPerHourDatas.Find(w => (int)w.weekDay == weekDay).perHourValues;
        weekDayDataValueAve = dayData.Average();
        currentHour = 0;
    }

    //Update the visualization
    private void UpdateVisual()
    {
        currentHour += Time.deltaTime * 0.01f * timeSpeed;
        if (currentHour >= 24)  // checking is current hour exceeded 24
        {
            currentHour = currentHour - 24; //yes - new day start
            // when the visualmode is in year mode, increase the count for day, and if is over 7, reset it
            if (visualMode == VisualMode.Year)
            {
                weekDay++; 
                if (weekDay >= 7) 
                {
                    weekDay = 0;
                }
                Getdata(); // calls function to get data for the new day
            }
        }
        int hourInt = (int)currentHour; //convert to int
        int nextHourInt = hourInt + 1; //convert to int

        if (nextHourInt >= 24) nextHourInt = 0;

        float minorRoadsCurHourValue = dayData[hourInt];
        float minorRaodsNextHourValue = dayData[nextHourInt];
        // interpolate between current hour and the next hour to get the current values
        // lerp( the start value, the end value, and the interpolation value)
        minorRoadsCurrentValue = Mathf.Lerp(minorRoadsCurHourValue, minorRaodsNextHourValue, ((int)(currentHour * 100)) % 100 * 1.0f / 100);

        float majorRoadsCurHourValue = dayData[hourInt] * yearData.MinorToMajorRate;
        float majorRoadsNextHourValue = dayData[nextHourInt] * yearData.MinorToMajorRate;
        // interpolate between current hour and the next hour to get the current values
        // lerp( the start value, the end value, and the interpolation value)
        majorRoadsCurrentValue = Mathf.Lerp(majorRoadsCurHourValue, majorRoadsNextHourValue, ((int)(currentHour * 100)) % 100 * 1.0f / 100);

        UpdateMinorColor();
        UpdateMajorColor();
    }

    //Update Minor road color
    private void UpdateMinorColor()
    {
        //Calculate the color at give time
        Color32 showingColor =  minorRoadsGradient.Evaluate(minorRoadsCurrentValue / DataManager.Instance.MaxValue);
        //setting the inner glow color effect to minor road model
        minorRoadsHighlight.innerGlowColor = showingColor;
        //Apply a color to each object in the render array
        Array.ForEach(minorRoadsRenderers, r => r.material.color = showingColor);
        minorRoadsCurrentColor = showingColor;
    }

    //Update Major road color
    private void UpdateMajorColor()
    {
        //Calculate the color at give time
        Color32 showingColor =  majorRoadsGradient.Evaluate(majorRoadsCurrentValue / DataManager.Instance.MaxValue);
        //setting the inner glow color effect to minor road model
        majorRoadsHighlight.innerGlowColor = showingColor;
        //Apply a color to each object in the render array
        Array.ForEach(majorRoadsRenderers, r => r.material.color = showingColor);
        majorRoadsCurrentColor = showingColor;
    }

    
    
    public void ChangeVisualMode(VisualMode visualMode)
    {
        this.visualMode = visualMode;
        Getdata();
    }

    public void SetYear(int year)
    {
        this.year = year;
        Getdata();
    }


    public void SetWeekDay(int week)
    {
        this.weekDay = week;
        Getdata();
    }

    public void SetSpeed(float speed)
    {
        this.timeSpeed = speed;
    }


}
