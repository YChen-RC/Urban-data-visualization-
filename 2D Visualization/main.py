import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import HeatMap,Line,Timeline,Tab,Grid
from pyecharts.faker import Faker,Collector

def heatmap_data(data):   #Processing the dataset data 
    n = len(data)       #in html file 【data = Monday -> Sunday】
    m = len(data.columns)
    heat_list = [] 
    for i in range(n):    #An 2D array going through the data
        for j in range(m):
            heat_list.append([j,i,data.iloc[i,j]])
    return heat_list


def heat_time(data_list)->Timeline:     #initalising heatmap
    t1  = Timeline()                      # create timeline objects
    for i in range(2015,2022):
        c = (                             #initialsing the heatmap setting
        HeatMap(init_opts=opts.InitOpts(width="1075px", height="1599px"))
        .add_xaxis(list(data_list[0].columns))
        .add_yaxis(                             ##Setting the timeline slider
        "",
        list(data_list[i-2015].index),
        heatmap_data(data_list[i-2015]),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        )
        .set_global_opts(                      ##Setting chart title and position
        title_opts=opts.TitleOpts(title="HeatMap-Label"),
        visualmap_opts=opts.VisualMapOpts(orient =  "vertical",max_=210,pos_right=10),
        )
        )
        t1.add(c,'{}'.format(i))   
    return t1


def grid_vertical(data_list) -> Grid:
    i = 2015
    c = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="5%"),

        )
    )
    i = 2016
    c1 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="18%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    i = 2017
    c2 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="31%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    i = 2018
    c3 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="44%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    i = 2019
    c4 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="57%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    i = 2020
    c5 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="70%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    i = 2021
    c6 = (
        Line()
        .add_xaxis(list(data_list[i - 2015].index))
        .add_yaxis(data_list[i - 2015].columns[0],
                   list(data_list[i - 2015].iloc[:, 0]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[1],
                   list(data_list[i - 2015].iloc[:, 1]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[2],
                   list(data_list[i - 2015].iloc[:, 2]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[3],
                   list(data_list[i - 2015].iloc[:, 3]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[4],
                   list(data_list[i - 2015].iloc[:, 4]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[5],
                   list(data_list[i - 2015].iloc[:, 5]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .add_yaxis(data_list[i - 2015].columns[6],
                   list(data_list[i - 2015].iloc[:, 6]),
                   linestyle_opts=opts.LineStyleOpts(width=4),  # 设置线
                   itemstyle_opts=opts.ItemStyleOpts(border_width=5), )  # 设置点
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{i}", pos_top="83%"),
            #             datazoom_opts=opts.DataZoomOpts(pos_top="40%",range_start =10,range_end = 100),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width="1075px", height="1599px"))
        .add(c, grid_opts=opts.GridOpts(height="10%", pos_top="5%"))
        .add(c1, grid_opts=opts.GridOpts(height="10%", pos_top="18%"))
        .add(c2, grid_opts=opts.GridOpts(height="10%", pos_top="31%"))
        .add(c3, grid_opts=opts.GridOpts(height="10%", pos_top="44%"))
        .add(c4, grid_opts=opts.GridOpts(height="10%", pos_top="57%"))
        .add(c5, grid_opts=opts.GridOpts(height="10%", pos_top="70%"))
        .add(c6, grid_opts=opts.GridOpts(height="10%", pos_top="83%"))
    )
    return grid

def g_line(Major_roads,Minor_roads)->Grid:
    timeData = [str(i) for i in range(2015,2022)] # Define the x-axis data as a list of strings
    l1 = (  # everything below is defining first chart
    Line()
    .add_xaxis(xaxis_data=timeData) 
    .add_yaxis(
        series_name="Major Road",
        y_axis=Major_roads,
        symbol_size=8, #Setting the point size
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=True), #Show the data point value or not
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    #Defining axies properties, name/range/type etc
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Major Road traffic flow", subtitle="", pos_left="center"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            name = "Year",
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        yaxis_opts=opts.AxisOpts(max_=30,min_=20, name="Traffic flow"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        
        #Toolbox for restoring 
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
                },
            ),
        #The zoom bar feature
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                is_realtime=True,
                
                xaxis_index=[0, 1],
            )
        ],
        )
    )

    l2 = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name="Minor road",
        y_axis=Minor_roads,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    .set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        #Defining axies properties, name/range/type etc
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            name = "Year",
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                xaxis_index=[0, 1],
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name="Traffic Flow"),
        legend_opts=opts.LegendOpts(pos_left="7%"),
        )
    )

    g = (
    Grid(init_opts=opts.InitOpts(width="1024px", height="768px"))
    .add(chart=l1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
    .add(
        chart=l2,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="55%", height="35%"),
        )
    )
    return g
if __name__ == '__main__':
    
    #reads the xlsx file and add them into list 
    data_list = []
    for i in range(2015, 2022):
        df = pd.read_excel('traffic_data_by_week.xlsx', sheet_name=f'TRA0307_({i})')
        #Reads the specific row and column in the dataset 
        data = pd.DataFrame(data=np.array(df.iloc[5:29, 1:]), columns=df.iloc[4, 1:], index=np.array(df.iloc[5:29, 0]))
        data_list.append(data)

    Major_roads = []
    Minor_roads = []
    for i in range(2015, 2022):
        df1 = pd.read_excel('tra0302.xlsx', sheet_name=f'TRA0302_({i})')
        Major_roads.append(float(df1.iloc[13, 4]))
        Minor_roads.append(float(df1.iloc[13, -3]))

    tab = Tab()
    tab.add(heat_time(data_list), "HeatMap")
    tab.add(grid_vertical(data_list), "Line")
    tab.add(g_line(Major_roads, Minor_roads), "Major_Minor")
    tab.render('./heat_line.html')
    
    
    
    