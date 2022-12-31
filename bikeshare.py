#!/usr/bin/env python
# coding: utf-8

# # Google Data Analytics Capstone Project
# ### By: Mohamed G. El-Naggar | Dated: 31-12-2022

# ## Breif Background on the project:
# As a junior data analyst working in the marketing analyst team at Cyclistic(a bike-share company in Chicago). The director of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore, your team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights, your team will design a new marketing strategy to convert casual riders into annual members.
# 
# ## Stakeholders:
# * Lily Moreno: The director of marketing. Moreno is responsible for the development of campaigns and initiatives to promote the bike-share program.
# * Cyclistic marketing analytics team: A team of data analysts who are responsible for collecting, analysing, and reporting data that helps guide Cyclistic marketing strategy.
# * Cyclistic executive team: The executive team will decide whether to approve the recommended marketing program.
# 
# ## Business Task:
# 1. Determine the patterns associated with service offered by Cyclistic.
# 2. Analyse the target audience and clients for our new campagin.
# 3. Enhance current offered services.
# 
# ## Datasource:
# The data used was offered under license of this link [link](https://ride.divvybikes.com/data-license-agreement). 
# We used the last 11 months data in order to create the patterns associated with our services.
# ### Data:
# The data is sorted under same order for each file and contains the same 12 columns:
# 1. ride_id (a specific id for each ride).
# 2. rideable_type (type of bike used).  
# 3. started_at (time/date of starting journey).        
# 4. ended_at (time/date of ending journey).             
# 5. start_station_name (start station name).
# 6. start_station_id (start station internal id).
# 7. end_station_name (end station name).     
# 8. end_station_id (end station internal id).      
# 9. start_lat (start location latitude).         
# 10. start_lng (start location longitude).             
# 11. end_lat (end location latitude).               
# 12. end_lng (end location longitude).               
# 13. member_casual (member type).
# 
# From having the primary insight on the data provided over spreadsheet program, it seems that data is reliable and will give an output that will be helpful for decision making. But, this will be reached after cleaning process into a sortable and understandable way in order to get the new inputs that will help in our analysis.

# ## Processing the data:

# We'll use Python to do our manipulation and analysis.
# 
# First of all, well import the libraries we'll need originally in our analysis.

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Importing the last 11 months in dataframes:

# In[7]:


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


# Merging the dataframes of the last 11 months in one dataframe to apply all the cleaning steps:

# In[8]:


merger=pd.concat([jan,feb,mar,apr,may,jun,jul,aug,sep,octb,nov])
merger.head()


# In[9]:


merger.info()


# Determining the unique values in our dataframe:

# In[10]:


merger.nunique()


# Create date and time for both start and end time data we already have in our dateframe:

# In[11]:


merger['startdate']=pd.to_datetime(merger['started_at']).dt.date
merger['starttime']=pd.to_datetime(merger['started_at']).dt.time
merger['enddate']=pd.to_datetime(merger['ended_at']).dt.date
merger['endtime']=pd.to_datetime(merger['ended_at']).dt.time
merger.head()


# In[12]:


merger.info()


# In[13]:


#Convert start and end dates to datetime class
merger['startdate']=pd.to_datetime(merger['startdate'])
merger['enddate']=pd.to_datetime(merger['enddate'])


# Importing another Python library which appears to be useful to extract data from given start and end dates:

# In[14]:


import calendar
from datetime import datetime


# In[15]:


#Create weekday correspondent to each start and end dates
merger['startday']=merger[['startdate']].apply(lambda x: datetime.strftime(x['startdate'], '%A'), axis=1)
merger['endday']=merger[['enddate']].apply(lambda x: datetime.strftime(x['enddate'], '%A'), axis=1)


# In[16]:


#Cleaning process to eliminate non-used columns
merger.drop(merger.columns[2:4],axis=1,inplace=True)
merger.head()


# In[17]:


from datetime import timedelta


# In[18]:


#Convert start and end times to string and timedelta to get duration of each ride
merger['starttime']= (merger['starttime'].astype('string').apply(pd.Timedelta))


# In[19]:


merger['endtime']= (merger['endtime'].astype('string').apply(pd.Timedelta))


# In[20]:


#Create a backup dataframe for any downfall in the code
merger2=merger


# Cleaning and elimination of non-used columns:

# In[21]:


#Create Duration column in minutes
merger['duration']=((merger['endtime']-merger['starttime']).dt.total_seconds())/60
#Eliminate trip which started and ended in other days - one trip as per dataset nunique output
merger.drop(merger.loc[merger['duration']<0].index,inplace=True)
merger.drop(merger.loc[merger['duration']==0].index,inplace=True)
merger.dropna()
merger.head()


# In[22]:


merger.dropna(axis=0,how='all')


# In[23]:


merger.nunique()


# In[24]:


merger.isnull().sum()


# In[25]:


merger.nunique()


# ## Analyzing the data after cleaning:

# ### Maximum trip duration and data

# In[26]:


#Get max. trip duration and its details
merger['duration'].max()


# In[27]:


max_trip=merger.loc[merger['duration']==merger['duration'].max()]
max_trip.head()


# In[28]:


max_trip.to_csv('max_trip.csv')


# ### Minimum trip duration and data

# In[29]:


#Get min. trip duration and its details
merger['duration'].min()


# In[30]:


min_trip=merger.loc[merger['duration']==merger['duration'].min()]
min_trip.head()


# ### Median and mean duration for trips:

# In[31]:


merger['duration'].median()


# In[32]:


merger['duration'].mean()


# In[33]:


mean=merger['duration'].mean()
above_mean=merger.loc[merger['duration']>mean].shape[0]
below_mean=merger.loc[merger['duration']<mean].shape[0]

print('No. of Trips Above Mean Duration are: ',above_mean)
print('No. of Trips Below Mean Duration are: ',below_mean)


# ### Identify preferable bike type for our customers:

# In[34]:


#Specify bike types in company
merger['rideable_type'].unique()


# In[35]:


#Most preferred bike type
merger['rideable_type'].value_counts().idxmax()


# In[36]:


#Ride numbers for each bike type
merger['rideable_type'].value_counts()


# In[52]:


sns.barplot(x=merger['rideable_type'].unique(),
           y=merger['rideable_type'].value_counts()/1000000
           );
plt.xlabel('Types of Bikes Available');
plt.ylabel('No of Rides for Each Type in millions');
plt.title('Fig.1 Relation between Bike Type and Number of Rides');
plt.tick_params(axis='y',labelsize=10);


# In[53]:


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


# ### Identify customers patterns:

# In[54]:


#Count total trips done by user types
merger['member_casual'].value_counts()


# In[55]:


plt.pie(merger['member_casual'].value_counts(),
        labels=merger['member_casual'].unique(),
        autopct=per(merger['member_casual'].value_counts()));
plt.title('Fig. 3 Percantage of Customers');


# ### Identify weekdays pattern:

# In[56]:


#Getting ride numbers in each day
merger['startday'].value_counts()


# In[60]:


(merger['startday'].value_counts()/1000).plot(kind='bar',color='blue');
plt.title('Fig. 4: No. of Rides per Weekday');
plt.xlabel('Weekdays');
plt.ylabel('Fig. 4: No of rides in thousands');


# ### Identify months pattern:

# In[ ]:


def day_mean(day):
    merger.loc[merger['startday']==day]


# In[73]:


merger['month']=merger['startdate'].dt.month
merger['month_name'] = merger['startdate'].dt.month_name().str[:3]
merger.head()


# In[74]:


merger['month_name'].value_counts()


# In[76]:


(merger['month_name'].value_counts()/1000).plot(kind='bar',color='blue');
plt.title('Fig. 5: No. of Rides per month');
plt.xlabel('Months');
plt.ylabel('No of rides in thousands');


# #### Function to manually have pattern for each month

# In[77]:


def month_mean(month):
    month_mean=merger.loc[merger['month']==month]
    month_mean_duration=month_mean['duration'].mean()
    rider_types=month_mean['member_casual'].value_counts()
    bike_type=month_mean['rideable_type'].value_counts()
    return month_mean_duration,rider_types,bike_type
month_entry=int(input('enter month'))
month_mean(month_entry)


# ### Relation between weekdays and member type for weekdays:

# In[84]:


plt.figure(figsize=(14,10))
sns.countplot(x='startday', hue='member_casual', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('WeekDays');
plt.ylabel('Number of Rides');
plt.title('Fig. 6: Customers pattern during weekdays');


# ### Relation between weekdays and member type for months:

# In[85]:


plt.figure(figsize=(14,10))
sns.countplot(x='month_name', hue='member_casual', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Months');
plt.ylabel('Number of Rides');
plt.title('Fig. 7: Customers pattern during months');


# ### Relation between weekdays and bike type for weekdays:

# In[87]:


plt.figure(figsize=(14,10))
sns.countplot(x='startday', hue='rideable_type', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Weekday');
plt.ylabel('Number of Rides');
plt.title('Fig. 8: Customers pattern during months');


# ### Relation between weekdays and bike type for months:

# In[88]:


plt.figure(figsize=(14,10))
sns.countplot(x='month_name', hue='rideable_type', data=merger, palette='Set1')
plt.tight_layout()
plt.xlabel('Months');
plt.ylabel('Number of Rides');
plt.title('Fig. 9: Customers pattern during months');


# ## Findings:

# From the analysis performed it shows some patterns that is obviously noticed:
# 1. Maximum duration time and data shows our service in bike sharing can be used all day not for a specific trip.
# 2. Minimum duration time and data shows that some customers tend to leave the bike once they have it.
# 3. Most preferred bike type is electric then usual bike. While docked type has only 3.1% of total market.
# 4. Casual members have more attribution than subscribed members.
# 5. Saturday is the most used day.
# 6. Summer is most preferable season in our business and for our customers as well.

# ## Conclusion:

# Our next campaign can look deeper and enchance based on the following ideas:
# 1. Take in consideration full day rental service supported by current global direction to minimize emissions.
# 2. Best campaign is set to launch in May as summer months are our top months.
# 3. Invest more in electric bikes as it seems that everyone loving it based on the data above.
# 4. Try to close the docked bikes branch as it doesn't have impact on total rides in both months and weekdays.
# 

# 

# 

# 
