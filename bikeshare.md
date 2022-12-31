# Google Data Analytics Capstone Project
### By: Mohamed G. El-Naggar | Dated: 31-12-2022

## Breif Background on the project:
As a junior data analyst working in the marketing analyst team at Cyclistic(a bike-share company in Chicago). The director of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore, your team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights, your team will design a new marketing strategy to convert casual riders into annual members.

## Stakeholders:
* Lily Moreno: The director of marketing. Moreno is responsible for the development of campaigns and initiatives to promote the bike-share program.
* Cyclistic marketing analytics team: A team of data analysts who are responsible for collecting, analysing, and reporting data that helps guide Cyclistic marketing strategy.
* Cyclistic executive team: The executive team will decide whether to approve the recommended marketing program.

## Business Task:
1. Determine the patterns associated with service offered by Cyclistic.
2. Analyse the target audience and clients for our new campagin.
3. Enhance current offered services.

## Datasource:
The data used was offered under license of this link [link](https://ride.divvybikes.com/data-license-agreement). 
We used the last 11 months data in order to create the patterns associated with our services.
### Data:
The data is sorted under same order for each file and contains the same 12 columns:
1. ride_id (a specific id for each ride).
2. rideable_type (type of bike used).  
3. started_at (time/date of starting journey).        
4. ended_at (time/date of ending journey).             
5. start_station_name (start station name).
6. start_station_id (start station internal id).
7. end_station_name (end station name).     
8. end_station_id (end station internal id).      
9. start_lat (start location latitude).         
10. start_lng (start location longitude).             
11. end_lat (end location latitude).               
12. end_lng (end location longitude).               
13. member_casual (member type).

From having the primary insight on the data provided over spreadsheet program, it seems that data is reliable and will give an output that will be helpful for decision making. But, this will be reached after cleaning process into a sortable and understandable way in order to get the new inputs that will help in our analysis.

## Processing the data:

We'll use Python to do our manipulation and analysis.

First of all, well import the libraries we'll need originally in our analysis.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
```

Importing the last 11 months in dataframes:


```python
nov=pd.read_csv('202211-divvy-tripdata.csv')
octb=pd.read_csv('202210-divvy-tripdata.csv')
sep=pd.read_csv('202209-divvy-tripdata.csv')
aug=pd.read_csv('202208-divvy-tripdata.csv')
jul=pd.read_csv('202207-divvy-tripdata.csv')
jun=pd.read_csv('202206-divvy-tripdata.csv')
may=pd.read_csv('202205-divvy-tripdata.csv')
apr=pd.read_csv('202204-divvy-tripdata.csv')
mar=pd.read_csv('202203-divvy-tripdata.csv')
feb=pd.read_csv('202202-divvy-tripdata.csv')
jan=pd.read_csv('202201-divvy-tripdata.csv')
```

Merging the dataframes of the last 11 months in one dataframe to apply all the cleaning steps:


```python
merger=pd.concat([jan,feb,mar,apr,may,jun,jul,aug,sep,octb,nov])
merger.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>2022-01-13 11:59:47</td>
      <td>2022-01-13 12:02:44</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>2022-01-10 08:41:56</td>
      <td>2022-01-10 08:46:17</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>2022-01-25 04:53:40</td>
      <td>2022-01-25 04:58:01</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>2022-01-04 00:18:04</td>
      <td>2022-01-04 00:33:00</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>2022-01-20 01:31:10</td>
      <td>2022-01-20 01:37:12</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>member</td>
    </tr>
  </tbody>
</table>
</div>




```python
merger.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 5485911 entries, 0 to 337734
    Data columns (total 13 columns):
     #   Column              Dtype  
    ---  ------              -----  
     0   ride_id             object 
     1   rideable_type       object 
     2   started_at          object 
     3   ended_at            object 
     4   start_station_name  object 
     5   start_station_id    object 
     6   end_station_name    object 
     7   end_station_id      object 
     8   start_lat           float64
     9   start_lng           float64
     10  end_lat             float64
     11  end_lng             float64
     12  member_casual       object 
    dtypes: float64(4), object(9)
    memory usage: 586.0+ MB


Determining the unique values in our dataframe:


```python
merger.nunique()
```




    ride_id               5485911
    rideable_type               3
    started_at            4575538
    ended_at              4588116
    start_station_name       1661
    start_station_id         1311
    end_station_name         1680
    end_station_id           1316
    start_lat              648758
    start_lng              613005
    end_lat                  1588
    end_lng                  1572
    member_casual               2
    dtype: int64



Create date and time for both start and end time data we already have in our dateframe:


```python
merger['startdate']=pd.to_datetime(merger['started_at']).dt.date
merger['starttime']=pd.to_datetime(merger['started_at']).dt.time
merger['enddate']=pd.to_datetime(merger['ended_at']).dt.date
merger['endtime']=pd.to_datetime(merger['ended_at']).dt.time
merger.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>2022-01-13 11:59:47</td>
      <td>2022-01-13 12:02:44</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-13</td>
      <td>11:59:47</td>
      <td>2022-01-13</td>
      <td>12:02:44</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>2022-01-10 08:41:56</td>
      <td>2022-01-10 08:46:17</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-10</td>
      <td>08:41:56</td>
      <td>2022-01-10</td>
      <td>08:46:17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>2022-01-25 04:53:40</td>
      <td>2022-01-25 04:58:01</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>member</td>
      <td>2022-01-25</td>
      <td>04:53:40</td>
      <td>2022-01-25</td>
      <td>04:58:01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>2022-01-04 00:18:04</td>
      <td>2022-01-04 00:33:00</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>casual</td>
      <td>2022-01-04</td>
      <td>00:18:04</td>
      <td>2022-01-04</td>
      <td>00:33:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>2022-01-20 01:31:10</td>
      <td>2022-01-20 01:37:12</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>member</td>
      <td>2022-01-20</td>
      <td>01:31:10</td>
      <td>2022-01-20</td>
      <td>01:37:12</td>
    </tr>
  </tbody>
</table>
</div>




```python
merger.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 5485911 entries, 0 to 337734
    Data columns (total 17 columns):
     #   Column              Dtype  
    ---  ------              -----  
     0   ride_id             object 
     1   rideable_type       object 
     2   started_at          object 
     3   ended_at            object 
     4   start_station_name  object 
     5   start_station_id    object 
     6   end_station_name    object 
     7   end_station_id      object 
     8   start_lat           float64
     9   start_lng           float64
     10  end_lat             float64
     11  end_lng             float64
     12  member_casual       object 
     13  startdate           object 
     14  starttime           object 
     15  enddate             object 
     16  endtime             object 
    dtypes: float64(4), object(13)
    memory usage: 753.4+ MB



```python
#Convert start and end dates to datetime class
merger['startdate']=pd.to_datetime(merger['startdate'])
merger['enddate']=pd.to_datetime(merger['enddate'])
```

Importing another Python library which appears to be useful to extract data from given start and end dates:


```python
import calendar
from datetime import datetime
```


```python
#Create weekday correspondent to each start and end dates
merger['startday']=merger[['startdate']].apply(lambda x: datetime.strftime(x['startdate'], '%A'), axis=1)
merger['endday']=merger[['enddate']].apply(lambda x: datetime.strftime(x['enddate'], '%A'), axis=1)
```


```python
#Cleaning process to eliminate non-used columns
merger.drop(merger.columns[2:4],axis=1,inplace=True)
merger.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-13</td>
      <td>11:59:47</td>
      <td>2022-01-13</td>
      <td>12:02:44</td>
      <td>Thursday</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-10</td>
      <td>08:41:56</td>
      <td>2022-01-10</td>
      <td>08:46:17</td>
      <td>Monday</td>
      <td>Monday</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>member</td>
      <td>2022-01-25</td>
      <td>04:53:40</td>
      <td>2022-01-25</td>
      <td>04:58:01</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>casual</td>
      <td>2022-01-04</td>
      <td>00:18:04</td>
      <td>2022-01-04</td>
      <td>00:33:00</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>member</td>
      <td>2022-01-20</td>
      <td>01:31:10</td>
      <td>2022-01-20</td>
      <td>01:37:12</td>
      <td>Thursday</td>
      <td>Thursday</td>
    </tr>
  </tbody>
</table>
</div>




```python
from datetime import timedelta
```


```python
#Convert start and end times to string and timedelta to get duration of each ride
merger['starttime']= (merger['starttime'].astype('string').apply(pd.Timedelta))
```


```python
merger['endtime']= (merger['endtime'].astype('string').apply(pd.Timedelta))
```


```python
#Create a backup dataframe for any downfall in the code
merger2=merger
```

Cleaning and elimination of non-used columns:


```python
#Create Duration column in minutes
merger['duration']=((merger['endtime']-merger['starttime']).dt.total_seconds())/60
#Eliminate trip which started and ended in other days - one trip as per dataset nunique output
merger.drop(merger.loc[merger['duration']<0].index,inplace=True)
merger.drop(merger.loc[merger['duration']==0].index,inplace=True)
merger.dropna()
merger.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-13</td>
      <td>0 days 11:59:47</td>
      <td>2022-01-13</td>
      <td>0 days 12:02:44</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>2.950000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-10</td>
      <td>0 days 08:41:56</td>
      <td>2022-01-10</td>
      <td>0 days 08:46:17</td>
      <td>Monday</td>
      <td>Monday</td>
      <td>4.350000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>member</td>
      <td>2022-01-25</td>
      <td>0 days 04:53:40</td>
      <td>2022-01-25</td>
      <td>0 days 04:58:01</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>4.350000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>casual</td>
      <td>2022-01-04</td>
      <td>0 days 00:18:04</td>
      <td>2022-01-04</td>
      <td>0 days 00:33:00</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>14.933333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>member</td>
      <td>2022-01-20</td>
      <td>0 days 01:31:10</td>
      <td>2022-01-20</td>
      <td>0 days 01:37:12</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>6.033333</td>
    </tr>
  </tbody>
</table>
</div>




```python
merger.dropna(axis=0,how='all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-13</td>
      <td>0 days 11:59:47</td>
      <td>2022-01-13</td>
      <td>0 days 12:02:44</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>2.950000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>casual</td>
      <td>2022-01-10</td>
      <td>0 days 08:41:56</td>
      <td>2022-01-10</td>
      <td>0 days 08:46:17</td>
      <td>Monday</td>
      <td>Monday</td>
      <td>4.350000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>member</td>
      <td>2022-01-25</td>
      <td>0 days 04:53:40</td>
      <td>2022-01-25</td>
      <td>0 days 04:58:01</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>4.350000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>casual</td>
      <td>2022-01-04</td>
      <td>0 days 00:18:04</td>
      <td>2022-01-04</td>
      <td>0 days 00:33:00</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>14.933333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>member</td>
      <td>2022-01-20</td>
      <td>0 days 01:31:10</td>
      <td>2022-01-20</td>
      <td>0 days 01:37:12</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>6.033333</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>337730</th>
      <td>C349E243A9BAA6F7</td>
      <td>electric_bike</td>
      <td>Wabash Ave &amp; Grand Ave</td>
      <td>TA1307000117</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.891836</td>
      <td>-87.626806</td>
      <td>41.890000</td>
      <td>-87.620000</td>
      <td>member</td>
      <td>2022-11-25</td>
      <td>0 days 11:19:52</td>
      <td>2022-11-25</td>
      <td>0 days 11:31:50</td>
      <td>Friday</td>
      <td>Friday</td>
      <td>11.966667</td>
    </tr>
    <tr>
      <th>337731</th>
      <td>B0B4E85DA43A9194</td>
      <td>classic_bike</td>
      <td>Franklin St &amp; Jackson Blvd</td>
      <td>TA1305000025</td>
      <td>Sheffield Ave &amp; Wrightwood Ave</td>
      <td>TA1309000023</td>
      <td>41.877708</td>
      <td>-87.635321</td>
      <td>41.928712</td>
      <td>-87.653833</td>
      <td>casual</td>
      <td>2022-11-22</td>
      <td>0 days 16:57:53</td>
      <td>2022-11-22</td>
      <td>0 days 17:31:29</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>33.600000</td>
    </tr>
    <tr>
      <th>337732</th>
      <td>8D148DD47B59530B</td>
      <td>classic_bike</td>
      <td>Michigan Ave &amp; Ida B Wells Dr</td>
      <td>TA1305000010</td>
      <td>Shedd Aquarium</td>
      <td>15544</td>
      <td>41.876243</td>
      <td>-87.624426</td>
      <td>41.867226</td>
      <td>-87.615355</td>
      <td>casual</td>
      <td>2022-11-06</td>
      <td>0 days 13:04:05</td>
      <td>2022-11-06</td>
      <td>0 days 13:13:33</td>
      <td>Sunday</td>
      <td>Sunday</td>
      <td>9.466667</td>
    </tr>
    <tr>
      <th>337733</th>
      <td>0D1170BA18FD33D1</td>
      <td>classic_bike</td>
      <td>Halsted St &amp; 18th St</td>
      <td>13099</td>
      <td>Shedd Aquarium</td>
      <td>15544</td>
      <td>41.857506</td>
      <td>-87.645991</td>
      <td>41.867226</td>
      <td>-87.615355</td>
      <td>casual</td>
      <td>2022-11-06</td>
      <td>0 days 09:41:29</td>
      <td>2022-11-06</td>
      <td>0 days 15:17:17</td>
      <td>Sunday</td>
      <td>Sunday</td>
      <td>335.800000</td>
    </tr>
    <tr>
      <th>337734</th>
      <td>09B20DC75B5EA1E0</td>
      <td>electric_bike</td>
      <td>Michigan Ave &amp; Ida B Wells Dr</td>
      <td>TA1305000010</td>
      <td>Shedd Aquarium</td>
      <td>15544</td>
      <td>41.876272</td>
      <td>-87.624576</td>
      <td>41.867226</td>
      <td>-87.615355</td>
      <td>casual</td>
      <td>2022-11-26</td>
      <td>0 days 11:59:28</td>
      <td>2022-11-26</td>
      <td>0 days 12:31:04</td>
      <td>Saturday</td>
      <td>Saturday</td>
      <td>31.600000</td>
    </tr>
  </tbody>
</table>
<p>5266021 rows × 18 columns</p>
</div>




```python
merger.nunique()
```




    ride_id               5266021
    rideable_type               3
    start_station_name       1656
    start_station_id         1308
    end_station_name         1673
    end_station_id           1315
    start_lat              637179
    start_lng              602361
    end_lat                  1573
    end_lng                  1556
    member_casual               2
    startdate                 334
    starttime               86238
    enddate                   335
    endtime                 86238
    startday                    7
    endday                      7
    duration                17568
    dtype: int64




```python
merger.isnull().sum()
```




    ride_id                    0
    rideable_type              0
    start_station_name    773839
    start_station_id      773839
    end_station_name      828606
    end_station_id        828606
    start_lat                  0
    start_lng                  0
    end_lat                 4306
    end_lng                 4306
    member_casual              0
    startdate                  0
    starttime                  0
    enddate                    0
    endtime                    0
    startday                   0
    endday                     0
    duration                   0
    dtype: int64




```python
merger.nunique()
```




    ride_id               5266021
    rideable_type               3
    start_station_name       1656
    start_station_id         1308
    end_station_name         1673
    end_station_id           1315
    start_lat              637179
    start_lng              602361
    end_lat                  1573
    end_lng                  1556
    member_casual               2
    startdate                 334
    starttime               86238
    enddate                   335
    endtime                 86238
    startday                    7
    endday                      7
    duration                17568
    dtype: int64



## Analyzing the data after cleaning:

### Maximum trip duration and data


```python
#Get max. trip duration and its details
merger['duration'].max()
```




    1408.4833333333333




```python
max_trip=merger.loc[merger['duration']==merger['duration'].max()]
max_trip.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17502</th>
      <td>21F5D1C2E789B5A6</td>
      <td>classic_bike</td>
      <td>Desplaines St &amp; Kinzie St</td>
      <td>TA1306000003</td>
      <td>Sedgwick St &amp; North Ave</td>
      <td>TA1307000038</td>
      <td>41.888716</td>
      <td>-87.644448</td>
      <td>41.911386</td>
      <td>-87.638677</td>
      <td>casual</td>
      <td>2022-07-31</td>
      <td>0 days 00:21:49</td>
      <td>2022-07-31</td>
      <td>0 days 23:50:18</td>
      <td>Sunday</td>
      <td>Sunday</td>
      <td>1408.483333</td>
    </tr>
  </tbody>
</table>
</div>




```python
max_trip.to_csv('max_trip.csv')
```

### Minimum trip duration and data


```python
#Get min. trip duration and its details
merger['duration'].min()
```




    0.016666666666666666




```python
min_trip=merger.loc[merger['duration']==merger['duration'].min()]
min_trip.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>203</th>
      <td>B0F160012485900B</td>
      <td>classic_bike</td>
      <td>Financial Pl &amp; Ida B Wells Dr</td>
      <td>SL-010</td>
      <td>Financial Pl &amp; Ida B Wells Dr</td>
      <td>SL-010</td>
      <td>41.875024</td>
      <td>-87.633094</td>
      <td>41.875024</td>
      <td>-87.633094</td>
      <td>member</td>
      <td>2022-01-10</td>
      <td>0 days 07:28:27</td>
      <td>2022-01-10</td>
      <td>0 days 07:28:28</td>
      <td>Monday</td>
      <td>Monday</td>
      <td>0.016667</td>
    </tr>
    <tr>
      <th>15877</th>
      <td>B1BBF65BC2C3806E</td>
      <td>classic_bike</td>
      <td>Halsted St &amp; Archer Ave</td>
      <td>TA1308000013</td>
      <td>Halsted St &amp; Archer Ave</td>
      <td>TA1308000013</td>
      <td>41.847203</td>
      <td>-87.646795</td>
      <td>41.847203</td>
      <td>-87.646795</td>
      <td>member</td>
      <td>2022-01-23</td>
      <td>0 days 13:21:06</td>
      <td>2022-01-23</td>
      <td>0 days 13:21:07</td>
      <td>Sunday</td>
      <td>Sunday</td>
      <td>0.016667</td>
    </tr>
    <tr>
      <th>17966</th>
      <td>93C86A208BF0568E</td>
      <td>electric_bike</td>
      <td>Clinton St &amp; Madison St</td>
      <td>TA1305000032</td>
      <td>Clinton St &amp; Madison St</td>
      <td>TA1305000032</td>
      <td>41.881840</td>
      <td>-87.640791</td>
      <td>41.882242</td>
      <td>-87.641066</td>
      <td>member</td>
      <td>2022-01-27</td>
      <td>0 days 08:46:23</td>
      <td>2022-01-27</td>
      <td>0 days 08:46:24</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>0.016667</td>
    </tr>
    <tr>
      <th>43488</th>
      <td>B78E6B3F8273FB01</td>
      <td>electric_bike</td>
      <td>Clark St &amp; Columbia Ave</td>
      <td>RP-008</td>
      <td>Clark St &amp; Columbia Ave</td>
      <td>RP-008</td>
      <td>42.004472</td>
      <td>-87.672348</td>
      <td>42.004451</td>
      <td>-87.672402</td>
      <td>member</td>
      <td>2022-01-30</td>
      <td>0 days 11:51:46</td>
      <td>2022-01-30</td>
      <td>0 days 11:51:47</td>
      <td>Sunday</td>
      <td>Sunday</td>
      <td>0.016667</td>
    </tr>
    <tr>
      <th>46093</th>
      <td>C32D5D5D32BAAAD8</td>
      <td>electric_bike</td>
      <td>Damen Ave &amp; Pierce Ave</td>
      <td>TA1305000041</td>
      <td>Damen Ave &amp; Pierce Ave</td>
      <td>TA1305000041</td>
      <td>41.909408</td>
      <td>-87.677687</td>
      <td>41.909396</td>
      <td>-87.677692</td>
      <td>member</td>
      <td>2022-01-11</td>
      <td>0 days 13:22:43</td>
      <td>2022-01-11</td>
      <td>0 days 13:22:44</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>0.016667</td>
    </tr>
  </tbody>
</table>
</div>



### Median and mean duration for trips:


```python
merger['duration'].median()
```




    10.366666666666667




```python
merger['duration'].mean()
```




    15.968780786605647




```python
mean=merger['duration'].mean()
above_mean=merger.loc[merger['duration']>mean].shape[0]
below_mean=merger.loc[merger['duration']<mean].shape[0]

print('No. of Trips Above Mean Duration are: ',above_mean)
print('No. of Trips Below Mean Duration are: ',below_mean)
```

    No. of Trips Above Mean Duration are:  1618203
    No. of Trips Below Mean Duration are:  3647818


### Identify preferable bike type for our customers:


```python
#Specify bike types in company
merger['rideable_type'].unique()
```




    array(['electric_bike', 'classic_bike', 'docked_bike'], dtype=object)




```python
#Most preferred bike type
merger['rideable_type'].value_counts().idxmax()
```




    'electric_bike'




```python
#Ride numbers for each bike type
merger['rideable_type'].value_counts()
```




    electric_bike    2675078
    classic_bike     2425589
    docked_bike       165354
    Name: rideable_type, dtype: int64




```python
sns.barplot(x=merger['rideable_type'].unique(),
           y=merger['rideable_type'].value_counts()/1000000
           );
plt.xlabel('Types of Bikes Available');
plt.ylabel('No of Rides for Each Type in millions');
plt.title('Fig.1 Relation between Bike Type and Number of Rides');
plt.tick_params(axis='y',labelsize=10);
```


    
![png](output_46_0.png)
    



```python
y=merger['rideable_type'].value_counts()
mlabels=merger['rideable_type'].unique()
def per(values):
    def form(pcntg):
        total=sum(values)
        val=int(round(pcntg*total/100.0))
        return '{:.1f}%\n'.format(pcntg,v=val)
    return form
plt.pie(y,labels=mlabels,autopct=per(y));
plt.title('Fig. 2Percantage for Bike Types used by Customers');
```


    
![png](output_47_0.png)
    


### Identify customers patterns:


```python
#Count total trips done by user types
merger['member_casual'].value_counts()
```




    member    3084894
    casual    2181127
    Name: member_casual, dtype: int64




```python
plt.pie(merger['member_casual'].value_counts(),
        labels=merger['member_casual'].unique(),
        autopct=per(merger['member_casual'].value_counts()));
plt.title('Fig. 3 Percantage of Customers');
```


    
![png](output_50_0.png)
    


### Identify weekdays pattern:


```python
#Getting ride numbers in each day
merger['startday'].value_counts()
```




    Saturday     853076
    Thursday     774422
    Wednesday    742662
    Friday       742216
    Sunday       729128
    Tuesday      725234
    Monday       699283
    Name: startday, dtype: int64




```python
(merger['startday'].value_counts()/1000).plot(kind='bar',color='blue');
plt.title('Fig. 4: No. of Rides per Weekday');
plt.xlabel('Weekdays');
plt.ylabel('Fig. 4: No of rides in thousands');
```


    
![png](output_53_0.png)
    


### Identify months pattern:


```python
def day_mean(day):
    merger.loc[merger['startday']==day]
```


```python
merger['month']=merger['startdate'].dt.month
merger['month_name'] = merger['startdate'].dt.month_name().str[:3]
merger.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>...</th>
      <th>startdate</th>
      <th>starttime</th>
      <th>enddate</th>
      <th>endtime</th>
      <th>startday</th>
      <th>endday</th>
      <th>duration</th>
      <th>month</th>
      <th>month_full</th>
      <th>month_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C2F7DD78E82EC875</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012800</td>
      <td>-87.665906</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>...</td>
      <td>2022-01-13</td>
      <td>0 days 11:59:47</td>
      <td>2022-01-13</td>
      <td>0 days 12:02:44</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>2.950000</td>
      <td>1</td>
      <td>January</td>
      <td>Jan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A6CF8980A652D272</td>
      <td>electric_bike</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Clark St &amp; Touhy Ave</td>
      <td>RP-007</td>
      <td>42.012763</td>
      <td>-87.665967</td>
      <td>42.012560</td>
      <td>-87.674367</td>
      <td>...</td>
      <td>2022-01-10</td>
      <td>0 days 08:41:56</td>
      <td>2022-01-10</td>
      <td>0 days 08:46:17</td>
      <td>Monday</td>
      <td>Monday</td>
      <td>4.350000</td>
      <td>1</td>
      <td>January</td>
      <td>Jan</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BD0F91DFF741C66D</td>
      <td>classic_bike</td>
      <td>Sheffield Ave &amp; Fullerton Ave</td>
      <td>TA1306000016</td>
      <td>Greenview Ave &amp; Fullerton Ave</td>
      <td>TA1307000001</td>
      <td>41.925602</td>
      <td>-87.653708</td>
      <td>41.925330</td>
      <td>-87.665800</td>
      <td>...</td>
      <td>2022-01-25</td>
      <td>0 days 04:53:40</td>
      <td>2022-01-25</td>
      <td>0 days 04:58:01</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>4.350000</td>
      <td>1</td>
      <td>January</td>
      <td>Jan</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CBB80ED419105406</td>
      <td>classic_bike</td>
      <td>Clark St &amp; Bryn Mawr Ave</td>
      <td>KA1504000151</td>
      <td>Paulina St &amp; Montrose Ave</td>
      <td>TA1309000021</td>
      <td>41.983593</td>
      <td>-87.669154</td>
      <td>41.961507</td>
      <td>-87.671387</td>
      <td>...</td>
      <td>2022-01-04</td>
      <td>0 days 00:18:04</td>
      <td>2022-01-04</td>
      <td>0 days 00:33:00</td>
      <td>Tuesday</td>
      <td>Tuesday</td>
      <td>14.933333</td>
      <td>1</td>
      <td>January</td>
      <td>Jan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DDC963BFDDA51EEA</td>
      <td>classic_bike</td>
      <td>Michigan Ave &amp; Jackson Blvd</td>
      <td>TA1309000002</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.877850</td>
      <td>-87.624080</td>
      <td>41.884621</td>
      <td>-87.627834</td>
      <td>...</td>
      <td>2022-01-20</td>
      <td>0 days 01:31:10</td>
      <td>2022-01-20</td>
      <td>0 days 01:37:12</td>
      <td>Thursday</td>
      <td>Thursday</td>
      <td>6.033333</td>
      <td>1</td>
      <td>January</td>
      <td>Jan</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
merger['month_name'].value_counts()
```




    Jul    794349
    Aug    757025
    Jun    740529
    Sep    673877
    May    609064
    Oct    535427
    Apr    354490
    Nov    322280
    Mar    270665
    Feb    109798
    Jan     98517
    Name: month_name, dtype: int64




```python
(merger['month_name'].value_counts()/1000).plot(kind='bar',color='blue');
plt.title('Fig. 5: No. of Rides per month');
plt.xlabel('Months');
plt.ylabel('No of rides in thousands');
```


    
![png](output_58_0.png)
    


#### Function to manually have pattern for each month


```python
def month_mean(month):
    month_mean=merger.loc[merger['month']==month]
    month_mean_duration=month_mean['duration'].mean()
    rider_types=month_mean['member_casual'].value_counts()
    bike_type=month_mean['rideable_type'].value_counts()
    return month_mean_duration,rider_types,bike_type
month_entry=int(input('enter month'))
month_mean(month_entry)
```

    enter month4





    (14.861931366188093,
     member    234332
     casual    120158
     Name: member_casual, dtype: int64,
     electric_bike    183987
     classic_bike     159166
     docked_bike       11337
     Name: rideable_type, dtype: int64)



### Relation between weekdays and member type for weekdays:


```python
plt.figure(figsize=(14,10))
sns.countplot(x='startday', hue='member_casual', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('WeekDays');
plt.ylabel('Number of Rides');
plt.title('Fig. 6: Customers pattern during weekdays');
```


    
![png](output_62_0.png)
    


### Relation between weekdays and member type for months:


```python
plt.figure(figsize=(14,10))
sns.countplot(x='month_name', hue='member_casual', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Months');
plt.ylabel('Number of Rides');
plt.title('Fig. 7: Customers pattern during months');
```


    
![png](output_64_0.png)
    


### Relation between weekdays and bike type for weekdays:


```python
plt.figure(figsize=(14,10))
sns.countplot(x='startday', hue='rideable_type', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Weekday');
plt.ylabel('Number of Rides');
plt.title('Fig. 8: Customers pattern during months');
```


    
![png](output_66_0.png)
    


### Relation between weekdays and bike type for months:


```python
plt.figure(figsize=(14,10))
sns.countplot(x='month_name', hue='rideable_type', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Months');
plt.ylabel('Number of Rides');
plt.title('Fig. 9: Customers pattern during months');
```


    
![png](output_68_0.png)
    


## Findings:

From the analysis performed it shows some patterns that is obviously noticed:
1. Maximum duration time and data shows our service in bike sharing can be used all day not for a specific trip.
2. Minimum duration time and data shows that some customers tend to leave the bike once they have it.
3. Most preferred bike type is electric then usual bike. While docked type has only 3.1% of total market.
4. Casual members have more attribution than subscribed members.
5. Saturday is the most used day.
6. Summer is most preferable season in our business and for our customers as well.

## Conclusion:

Our next campaign can look deeper and enchance based on the following ideas:
1. Take in consideration full day rental service supported by current global direction to minimize emissions.
2. Best campaign is set to launch in May as summer months are our top months.
3. Invest more in electric bikes as it seems that everyone loving it based on the data above.
4. Try to close the docked bikes branch as it doesn't have impact on total rides in both months and weekdays.







