#!/usr/bin/env python
# coding: utf-8
#This code is used to generate the graphs comparing (1) gym level x frequency and (2) gym level x consistency of gym 
# In[32]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv("fre.csv")
df = pd.DataFrame(df)
df


# In[33]:


df2 = pd.read_csv("cons.csv")
df2 = pd.DataFrame(df2)
df2


# In[34]:


df3 = pd.read_csv("gym3.csv")
df3 = pd.DataFrame(df3)
df3


# In[8]:


df4 = pd.read_csv("fitness analysis.csv")
df4 = pd.DataFrame(df4)
df4


# In[4]:


#df.rename(columns={"How would you classify your familiarity with the gym and its equipment (or even facilities offered)?":"Level"})


# In[5]:


#fig = px.bar(df, x="Level", y="Consistency")
fig = sns.swarmplot(data=df, x="Level", y="Consistency")
fig.set(title="How long UCLA students have gymmed and how they classified their gym level")
fig


# In[25]:


f = sns.displot(data=df, x="Level", y="Frequency")
f.set(title="How UCLA students classified their gym level and how often they gym per week")
print(f)


# In[29]:


g = sns.displot(data=df2, x="Level", y="Consistency")
g.set(title="How UCLA students classified their gym level and how long they have gymmed")
g


# In[69]:


k = sns.displot(data=df3, x="Level", y="Muscle Group")
k.set(title="How UCLA students classified their gym level and what muscle group they like to target")
k


# In[ ]:




