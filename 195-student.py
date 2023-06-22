#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("In the following notebook we will how to clean and manipulate the data, and lastly come to a consulsion.")
print("Using the above skills set we will cleaned and manipulated the Austin weather data, to plot a point scatter graph for the average high and low temperature as per months")
print("Also we have plotted a point scatter graph for average temperature and humidity as per months ")



# ## Activity - 1 Find the average high and low temperature and plot a point grahp as per months

# In[2]:


#Activity 1
import pandas as pd
import matplotlib.pyplot as plt 

#read the csv
df = pd.read_csv('austin_weather.csv')
df



# In[3]:


#Fetech the months from Data column and add a new column
df['month'] = pd.DatetimeIndex(df['Date']).month
df

#Group by month column and find the average high and low temperature and make a new dataframe out of it
group_by_month = df.groupby('month')[['TempHighF','TempLowF']].mean().reset_index()
group_by_month



# In[4]:


#Plot a point scatter graph for the average high and low temperature as per months 
month = group_by_month['month']
TempHighF = group_by_month['TempHighF']

plt.scatter(month, TempHighF, label = "High temp")

TempLowF = group_by_month['TempLowF']

plt.scatter(month, TempLowF , label = "Low temp")
plt.legend()



# Conclusion - By logic the low temperature is always lesser then high temperature hence we have plot the grahp correctly

# # Activity - 2 Plot a point graph for showing the correlation between humidity and temperature as per month
# 

# In[5]:


#Activity 2
import pandas as pd
import matplotlib.pyplot as plt

#Read the dataframe
dataframe= pd.read_csv('austin_weather.csv')
dataframe

#Fetech the months from Data column and add a new column
dataframe['month'] = pd.DatetimeIndex(dataframe['Date']).month
dataframe


# In[6]:


#cleaning the data
dataframe.replace("-", float("NaN"), inplace=True)
df = dataframe.dropna()
df

#Converting datatype of HumidityHighPercent column from object to int
df['HumidityHighPercent'] = df['HumidityHighPercent'].astype(int)
df


# In[7]:


#Group by month column and out the find the average temperature and humidity 


# In[8]:


#Plot a point scatter graph for the average temperature and humidity as per months 
month = group_by_month['month']
TempHighF = group_by_month['TempHighF']
plt.scatter(month, TempHighF, label = "Average temperature")

HumidityHighPercent=group_by_month['HumidityHighPercent']

plt.scatter(month, HumidityHighPercent, label = "Average humidity")

plt.legend()


# Conclusion - 

# In[ ]:


#Print the Events column(which has weather information) and cross check the observation
df.groupby('month')['Events'].max().reset_index()


# Conclusion -  

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




