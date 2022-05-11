# Data analysis and visualization with python     
This repository contains some scripts that help exploring a course review dataset and getting some insights such as: 
- Top rated courses: Average ratings per course
- Time series analysis: rating by period
- Positive and negative reviews
- What day of the week are people the happiest...etc 

### Why Python? 
- Libraries to access and analyse data like pandas
- Creating interactive charts in a web app using justpy      
- Creating simple visualization plots using matplotlib 


### Dataset
- The course review dataset from udemy 
![alt text](http://url/to/img.png)


|Course | Name |	Timestamp	| Rating |	Comment |
|--|--|--|--|--|
|The Python Mega Course: Build 10 Real World Ap...	| 2021-04-02 06:25:52+00:00	4.0|	NaN |
 | The Python Mega Course: Build 10 Real World Ap... |	2021-04-02 05:12:34+00:00	4.0	| NaN |
| The Python Mega Course: Build 10 Real World Ap...	| 2021-04-02 05:11:03+00:00	4.0	| NaN |
| The Python Mega Course: Build 10 Real World Ap...	| 2021-04-02 03:33:24+00:00	5.0	| NaN |
| The Python Mega Course: Build 10 Real World Ap...	| 2021-04-02 03:31:49+00:00	4.5	| NaN |

# 1. Overview of the dataframe 


```python
import pandas as pd 
from datetime import datetime
from pytz import utc 
import matplotlib.pyplot as plt
data= pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data.head


```




    <bound method NDFrame.head of                                              Course Name  \
    0      The Python Mega Course: Build 10 Real World Ap...   
    1      The Python Mega Course: Build 10 Real World Ap...   
    2      The Python Mega Course: Build 10 Real World Ap...   
    3      The Python Mega Course: Build 10 Real World Ap...   
    4      The Python Mega Course: Build 10 Real World Ap...   
    ...                                                  ...   
    44995                 Python for Beginners with Examples   
    44996  The Python Mega Course: Build 10 Real World Ap...   
    44997  The Python Mega Course: Build 10 Real World Ap...   
    44998                 Python for Beginners with Examples   
    44999  The Python Mega Course: Build 10 Real World Ap...   
    
                          Timestamp  Rating Comment  
    0     2021-04-02 06:25:52+00:00     4.0     NaN  
    1     2021-04-02 05:12:34+00:00     4.0     NaN  
    2     2021-04-02 05:11:03+00:00     4.0     NaN  
    3     2021-04-02 03:33:24+00:00     5.0     NaN  
    4     2021-04-02 03:31:49+00:00     4.5     NaN  
    ...                         ...     ...     ...  
    44995 2018-01-01 01:11:26+00:00     4.0     NaN  
    44996 2018-01-01 01:09:56+00:00     5.0     NaN  
    44997 2018-01-01 01:08:11+00:00     5.0     NaN  
    44998 2018-01-01 01:05:26+00:00     5.0     NaN  
    44999 2018-01-01 01:01:16+00:00     5.0     NaN  
    
    [45000 rows x 4 columns]>



## 2. Average rating of courses per day


```python
# add a day column 
data["Day"]= data["Timestamp"].dt.date
day_average=data.groupby(["Day"]).mean()

```


```python
list(day_average.index)
plt.plot(day_average.index, day_average['Rating'])

```



![output_4_1](https://user-images.githubusercontent.com/54501663/167885516-a13ac433-cfa3-4d92-bed5-483808314f10.png)


    



```python
# Add figure object to resize the graph 
plt.figure(figsize=(25, 3))
plt.plot(day_average.index, day_average['Rating'])
```


![output_5_1](https://user-images.githubusercontent.com/54501663/167885636-fe08740e-253b-41ee-8dec-14a64c798830.png)

    


# 3. Average rating of courses per week


```python
data["Week"]=data["Timestamp"].dt.strftime("%Y-%U") # week with its year  
data.head()
average_week=data.groupby( ["Week"]).mean()
average_week
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rating</th>
    </tr>
    <tr>
      <th>Week</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-00</th>
      <td>4.434564</td>
    </tr>
    <tr>
      <th>2018-01</th>
      <td>4.424933</td>
    </tr>
    <tr>
      <th>2018-02</th>
      <td>4.417702</td>
    </tr>
    <tr>
      <th>2018-03</th>
      <td>4.401024</td>
    </tr>
  
  </tbody>
</table>
<p>173 rows × 1 columns</p>
</div>


```python
plt.figure(figsize=(30, 6))
plt.plot(average_week.index, average_week["Rating"])
```



![output_8_1](https://user-images.githubusercontent.com/54501663/167885975-7a1b88d8-aa35-487f-bda2-b54bf1443adf.png)

    


# 4. Average rating per month 


```python
data["Month"]=data["Timestamp"].dt.strftime("%y-%m")
average_month=data.groupby("Month").mean()
average_month
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rating</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18-01</th>
      <td>4.429645</td>
    </tr>
    <tr>
      <th>18-02</th>
      <td>4.436248</td>
    </tr>
    <tr>
      <th>18-03</th>
      <td>4.421671</td>
    </tr>
    <tr>
      <th>18-04</th>
      <td>4.468211</td>
    </tr>
    <tr>
      <th>18-05</th>
      <td>4.396420</td>
    </tr>
    <tr>
      <th>18-06</th>
      <td>4.375379</td>
    </tr>
    <tr>
      <th>18-07</th>
      <td>4.393184</td>
    </tr>
    <tr>
      <th>18-08</th>
      <td>4.344753</td>
    </tr>
    <tr>
      <th>18-09</th>
      <td>4.347247</td>
    </tr>
    <tr>
      <th>18-10</th>
      <td>4.374429</td>
    </tr>
    <tr>
      <th>18-11</th>
      <td>4.386817</td>
    </tr>
    <tr>
      <th>18-12</th>
      <td>4.342105</td>
    </tr>
    <tr>
      <th>19-01</th>
      <td>4.401920</td>
    </tr>
    <tr>
      <th>19-02</th>
      <td>4.346964</td>
    </tr>
    <tr>
      <th>19-03</th>
      <td>4.333145</td>
    </tr>
    <tr>
      <th>19-04</th>
      <td>4.420049</td>
    </tr>
    <tr>
      <th>19-05</th>
      <td>4.405569</td>
    </tr>
    <tr>
      <th>19-06</th>
      <td>4.398559</td>
    </tr>
    <tr>
      <th>19-07</th>
      <td>4.382353</td>
    </tr>
    <tr>
      <th>19-08</th>
      <td>4.417059</td>
    </tr>
    <tr>
      <th>19-09</th>
      <td>4.451135</td>
    </tr>
    <tr>
      <th>19-10</th>
      <td>4.483871</td>
    </tr>
    <tr>
      <th>19-11</th>
      <td>4.493260</td>
    </tr>
    <tr>
      <th>19-12</th>
      <td>4.471046</td>
    </tr>
    <tr>
      <th>20-01</th>
      <td>4.439615</td>
    </tr>
    <tr>
      <th>20-02</th>
      <td>4.428642</td>
    </tr>
    <tr>
      <th>20-03</th>
      <td>4.480690</td>
    </tr>
    <tr>
      <th>20-04</th>
      <td>4.475220</td>
    </tr>
    <tr>
      <th>20-05</th>
      <td>4.448082</td>
    </tr>
    <tr>
      <th>20-06</th>
      <td>4.482812</td>
    </tr>
    <tr>
      <th>20-07</th>
      <td>4.517508</td>
    </tr>
    <tr>
      <th>20-08</th>
      <td>4.470987</td>
    </tr>
    <tr>
      <th>20-09</th>
      <td>4.485862</td>
    </tr>
    <tr>
      <th>20-10</th>
      <td>4.515201</td>
    </tr>
    <tr>
      <th>20-11</th>
      <td>4.479306</td>
    </tr>
    <tr>
      <th>20-12</th>
      <td>4.528358</td>
    </tr>
    <tr>
      <th>21-01</th>
      <td>4.551325</td>
    </tr>
    <tr>
      <th>21-02</th>
      <td>4.567901</td>
    </tr>
    <tr>
      <th>21-03</th>
      <td>4.589207</td>
    </tr>
    <tr>
      <th>21-04</th>
      <td>4.544118</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(30,6))
plt.plot(average_month.index, average_month['Rating'])

```


![output_11_1](https://user-images.githubusercontent.com/54501663/167886394-b06fc970-654f-47bc-839b-1f9b58b2a1d4.png)

# 5. Average rating by course per month 


```python
data["Month"]=data["Timestamp"].dt.strftime("%y-%m")
average_month_course=data.groupby(["Month","Course Name"]).mean()
average_month_course[:20] 
# dataframe with 2 indexes 
```




    (262, 1)




```python
average_month_course=data.groupby(["Month","Course Name"]).mean().unstack()
average_month_course[:20] 
average_month_course.columns

```



```python

average_month_course.plot(figsize=(20,6))
```


![output_15_1](https://user-images.githubusercontent.com/54501663/167886534-78489dbb-3636-447b-a1b6-74fc1b93481a.png)
    


# 6. Day where people are happiest


```python
data.head

```




    <bound method NDFrame.head of                                              Course Name  \
    0      The Python Mega Course: Build 10 Real World Ap...   
    1      The Python Mega Course: Build 10 Real World Ap...   
    2      The Python Mega Course: Build 10 Real World Ap...   
    3      The Python Mega Course: Build 10 Real World Ap...   
    4      The Python Mega Course: Build 10 Real World Ap...   
    ...                                                  ...   
    44995                 Python for Beginners with Examples   
    44996  The Python Mega Course: Build 10 Real World Ap...   
    44997  The Python Mega Course: Build 10 Real World Ap...   
    44998                 Python for Beginners with Examples   
    44999  The Python Mega Course: Build 10 Real World Ap...   
    
                          Timestamp  Rating Comment         Day     Week  Month  
    0     2021-04-02 06:25:52+00:00     4.0     NaN  2021-04-02  2021-13  21-04  
    1     2021-04-02 05:12:34+00:00     4.0     NaN  2021-04-02  2021-13  21-04  
    2     2021-04-02 05:11:03+00:00     4.0     NaN  2021-04-02  2021-13  21-04  
    3     2021-04-02 03:33:24+00:00     5.0     NaN  2021-04-02  2021-13  21-04  
    4     2021-04-02 03:31:49+00:00     4.5     NaN  2021-04-02  2021-13  21-04  
    ...                         ...     ...     ...         ...      ...    ...  
    44995 2018-01-01 01:11:26+00:00     4.0     NaN  2018-01-01  2018-00  18-01  
    44996 2018-01-01 01:09:56+00:00     5.0     NaN  2018-01-01  2018-00  18-01  
    44997 2018-01-01 01:08:11+00:00     5.0     NaN  2018-01-01  2018-00  18-01  
    44998 2018-01-01 01:05:26+00:00     5.0     NaN  2018-01-01  2018-00  18-01  
    44999 2018-01-01 01:01:16+00:00     5.0     NaN  2018-01-01  2018-00  18-01  
    
    [45000 rows x 7 columns]>




```python
data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["daynumber"]=data["Timestamp"].dt.strftime("%w")
data
average_weekday=data.groupby(["Weekday", "daynumber"]).mean()
average_weekday=average_weekday.sort_values("daynumber")
average_weekday
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Rating</th>
    </tr>
    <tr>
      <th>Weekday</th>
      <th>daynumber</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sunday</th>
      <th>0</th>
      <td>4.439097</td>
    </tr>
    <tr>
      <th>Monday</th>
      <th>1</th>
      <td>4.449335</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <th>2</th>
      <td>4.446240</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <th>3</th>
      <td>4.427452</td>
    </tr>
    <tr>
      <th>Thursday</th>
      <th>4</th>
      <td>4.437880</td>
    </tr>
    <tr>
      <th>Friday</th>
      <th>5</th>
      <td>4.455207</td>
    </tr>
    <tr>
      <th>Saturday</th>
      <th>6</th>
      <td>4.440274</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(15,6))

plt.plot(average_weekday.index.get_level_values(0), average_weekday["Rating"])
```

![output_19_1](https://user-images.githubusercontent.com/54501663/167886646-f81e520c-7eaa-4374-8150-df43e324a92f.png)   
 # Number of comments per course


```python
nb_comment=data.groupby("Course Name")["Comment"].count()
list(nb_comment)
nb_comment.index

```


```python
plt.pie(nb_comment, labels=nb_comment.index)
```


![output_22_1](https://user-images.githubusercontent.com/54501663/167886838-3b93cfad-baaa-406a-9f6f-f6682193f70e.png)

    


### Requirements


#### Pandas
```bash
sudo apt install python3-pandas
```

#### Matplotlib
```bash 
pip install matplotlib
```
#### Justpy
```bash 
pip install justpy

```
### Highchart documentation

https://www.highcharts.com/docs/chart-and-series-types/pie-chart 
