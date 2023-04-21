//This script is responsible for dealing with dataset
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataManager : MonoBehaviour
{

    public static DataManager Instance;

    [SerializeField]
    private List<YearData> road1YearDatas; //List to store all the data in tra0307

    [SerializeField]
    private float maxValue; // Maximum value for the data set


    public float MaxValue { get { return maxValue; } }

    // This method is for finding the max value in the dataset
    // and result will be use in the calculating the color gradient process
    private void Awake()
    {
        Instance = this;
        // Store maximum value in the data list
        maxValue = road1YearDatas[0].weekDayPerHourDatas[0].perHourValues[0];

        //Looping through the data to find the maximum value
        for (int i = 0; i < road1YearDatas.Count; i++) 
        {
            for (int j = 0; j < road1YearDatas[i].weekDayPerHourDatas.Count; j++) 
            {
                for (int m = 0; m < road1YearDatas[i].weekDayPerHourDatas[j].perHourValues.Count; m++)
                {
                    //Checking is maxvalue or not
                    if (road1YearDatas[i].weekDayPerHourDatas[j].perHourValues[m] > maxValue) 
                    {
                        maxValue = road1YearDatas[i].weekDayPerHourDatas[j].perHourValues[m];
                    }
                }
            }
        }
    }

    // Method to get year data
    public YearData GetYearData(int year)
    {
        return road1YearDatas.Find(d => d.Year == year);
    }

    // Method to get weekday data
    public WeekDayPerHourData GetWeekDayData(int year, int week)
    {
        WeekDayPerHourData weekDayData = road1YearDatas.Find(i => i.Year == year).weekDayPerHourDatas.Find(w => (int)w.weekDay == week);
        return weekDayData;
    }
}

[System.Serializable]
public class YearData
{
    public int Year; 
    public float MinorToMajorRate = 23.8f / 2.6f; //Setting the initial Ratio 
    public List<WeekDayPerHourData> weekDayPerHourDatas; 
}


[System.Serializable]
public class WeekDayPerHourData
{
    public WeekDay weekDay; 
    public List<float> perHourValues; 
}

//setting the days of week
public enum WeekDay
{
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
}