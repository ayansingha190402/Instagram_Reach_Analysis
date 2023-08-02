import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("Instagram.csv", encoding = 'latin1')
print(data.head())
#Before starting everything, let’s have a look at whether this dataset contains any null values or not:

data.isnull().sum()

#So it has a null value in every column. Let’s drop all these null values and move further:


data = data.dropna()
#Let’s have a look at the insights of the columns to understand the data type of all the columns:


data.info()

#Analyzing Instagram Reach
#Now let’s start with analyzing the reach of my Instagram posts. I will first have a look at the distribution of impressions I have received from home:


plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.distplot(data['From Home'])
plt.show()

#Now let’s have a look at the distribution of the impressions I received from hashtags:


plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()

#Now let’s have a look at the percentage of impressions I get from various sources on Instagram:


home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()
labels = ['From Home','From Hashtags','From Explore','Other']
values = [home, hashtags, explore, other]
fig = px.pie(data, values=values, names=labels, 
title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()
