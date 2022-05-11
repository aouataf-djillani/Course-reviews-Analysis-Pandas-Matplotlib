import justpy as jp
import pandas as pd 
from datetime import datetime
from pytz import utc 
import matplotlib.pyplot as plt

data= pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"]=data["Timestamp"].dt.strftime("%y-%m")
average_month=data.groupby("Month").mean()


chart_def= """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating By Month'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}  {point.y} '
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

"""
def app():
    wp=jp.QuasarPage()
    #heading 
    h1=jp.QDiv(a=wp, text="Analysis of Course reviews", classes= "text-h3 text-center q-pb-md" )
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis", classes= "text-h5 text-center q-pb-md")
    # high charts: spline from documentation 
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories= list(average_month.index)
    hc.options.series[0].data= list(average_month["Rating"])
    return wp  

jp.justpy(app)
