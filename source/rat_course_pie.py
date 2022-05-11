"""
a JustPy app containing a  pie chart that represents number of ratingsd per course. 

"""

import justpy as jp
import pandas as pd 
from datetime import datetime
from pytz import utc 
import matplotlib.pyplot as plt

data= pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
nb_rating=data.groupby("Course Name")["Rating"].count()

chart_def= """
{
    chart: {
        
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""
def app():
    wp=jp.QuasarPage()
    #heading 
    h1=jp.QDiv(a=wp, text="Analysis of Course reviews", classes= "text-h3 text-center q-pb-md" )
    p1=jp.QDiv(a=wp, text="This pie chart represent course review analysis", classes= "text-h5 text-center q-pb-md")
    # high charts: spline from documentation 
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc_data=[{"name":v1, "y":v2} for v1, v2 in zip(nb_rating.index, nb_rating)]
    hc.options.series[0].data=hc_data
    
    return wp  

jp.justpy(app)
