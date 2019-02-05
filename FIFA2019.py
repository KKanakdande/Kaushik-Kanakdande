#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir("C:/Users/KAUSHIK/Documents/Python Scripts")


# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import itertools
import io
import re
import warnings
warnings.filterwarnings('ignore')
# !pip install plotly
import plotly
import plotly.offline as py # Visualization
py.init_notebook_mode(connected=True) # Visualization
import plotly.figure_factory as ff # Visualization
data = pd.read_csv("data.csv")


# In[9]:


# To display top 5 rows of the table
data.head()


# In[10]:


# To find the null value from the table. Which is in True and False. False for the not null value and True for null value.
missing_data = data.isnull()
missing_data.head(10)


# In[11]:


# To give the information about the table columns shows the datatype.
data.info()


# In[12]:


# It Shows Column Name Datatype Null Values
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[13]:


# To describe the count of the value. mean value, min value, max value.
data.describe()


# In[31]:


# .shape is used to count the rows and columns which is present in the dataset
data.shape


# In[15]:


data.nunique()


# In[16]:


# .isnull().any() is used to see the non-null value. False and True show the value of null or not null values.
# True is used when there is null value in the column.
data.isnull().any()


# In[17]:


# .columns is used to show the columns which is available in the dataset
data.columns


# In[18]:


# We are making heat-map for the given dataset.
plt.figure(figsize=(89,89))
sns.heatmap(data.corr(), annot=True)


# In[19]:


# This is used to make a bar graph on Age Distribution. 
# Which is used to see the maxmium Player comes under in 18 - 28 age group
plt.figure(figsize=(12,8))
sns.distplot(data.Age).set_title("Age Distribution")


# In[20]:


# List of Oldest Player in Dataset based on Age Distribution
oage = data.sort_values(by = 'Age', ascending = False)[['Name','Club','Overall','Age']].head(10)
table  = ff.create_table(np.round(oage,4))
py.iplot(table)


# In[21]:


# List of Yongest Player in Dataset based on Age Distribution
yage = data.sort_values(by = 'Age', ascending = True)[['Name','Club','Overall','Age']].head(10)
table  = ff.create_table(np.round(yage,4))
py.iplot(table)


# In[22]:


# Use of Foot. This will give us the Preferred Foot. In this dataset Maxmium Player use Right Foot to play Football
p = sns.countplot(x = 'Preferred Foot', data = data)


# In[6]:


# Top 5 left-footed players
data[data['Preferred Foot'] == 'Left'][['Name','Overall']].head()


# In[7]:


# Top 5 left-footed players
data[data['Preferred Foot'] == 'Right'][['Name','Overall']].head()


# In[23]:


# Work Rate is based on three levels which is High, Medium, Low.
p = sns.countplot(x = 'Work Rate', data = data)
_ = plt.setp(p.get_xticklabels(), rotation=90)


# In[24]:


# Count of Top 10 Best Players in the FIFA 2019
overall = data.sort_values(by = 'Overall', ascending = False)[['Name','Club','Overall','Age']].head(10)
table  = ff.create_table(np.round(overall,4))
py.iplot(table)


# In[25]:


# Positions of different players on the Field.
pos = sns.countplot(x = 'Position', data = data, palette = 'hls');
pos.set_title(label='Count of Players', fontsize=15);
_ = plt.setp(pos.get_xticklabels(), rotation=90)


# In[3]:


# The best player per position
from IPython.display import display, HTML
display(HTML(data.iloc[data.groupby(data['Position'])['Overall'].idxmax()][['Name', 'Position']].to_html(index=False)))


# In[5]:


player_features = (
    'Acceleration', 'Aggression', 'Agility', 
    'Balance', 'BallControl', 'Composure', 
    'Crossing', 'Dribbling', 'FKAccuracy', 
    'Finishing', 'GKDiving', 'GKHandling', 
    'GKKicking', 'GKPositioning', 'GKReflexes', 
    'HeadingAccuracy', 'Interceptions', 'Jumping', 
    'LongPassing', 'LongShots', 'Marking', 'Penalties'
)

# Top three features per position
for i, val in data.groupby(data['Position'])[player_features].mean().iterrows():
    print('Position {}: {}, {}, {}'.format(i, *tuple(val.nlargest(3).index)))


# In[10]:


from math import pi
idx = 1
plt.figure(figsize=(15,45))
for position_name, features in data.groupby(data['Position'])[player_features].mean().iterrows():
    top_features = dict(features.nlargest(5))
    
    # number of variable
    categories=top_features.keys()
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = list(top_features.values())
    values += values[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(9, 3, idx, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30,40,50,60,70,80], ["10","20","30","40","50","60","70","80","90"], color="grey", size=7)
    plt.ylim(0,100)
    
    plt.subplots_adjust(hspace = 0.5)
    
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    
    plt.title(position_name, size=11, y=1.1)
    
    idx += 1 


# In[27]:


pos = data.sort_values(by = 'Overall', ascending = False)[['Name', 'Overall', 'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl']].sort_values(by='Overall', ascending=False).head(10)
table  = ff.create_table(np.round(pos))
py.iplot(table)


# In[ ]:


# Explanation on Analysis:
# 1) We have different Analysis by different variables in dataset.
# 2) We made analysis on Age Distribution in which we get to know about that players age starts from 16 to 45 age limit 
# and maximum players comes under between 18 - 28 Age
# 3) After analysis on Prefered Foot we have 2 option on it which is Left and Right. Maximum players are Right Footed
# 4) We have top 10 best Players based on Overall, Acceleration,Aggression, Agility, Balance, BallControl..
# 5) In this we have shown the Best Players with there Best Field Positions.
# 6) We have Spider Map Which is based on different Position in the Field.

