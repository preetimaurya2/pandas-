#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_excel('Data_Train.xlsx')
df


# In[14]:


df['Arrival_time']=df['Arrival_Time'].apply(lambda i:i[:5])
df['Arrival_time']


# In[20]:


df.drop(columns=['Arrival_Time'])


# In[15]:


df.isnull().sum()


# In[7]:


df.info()


# In[8]:


df.describe(include='object')


# In[9]:


df.describe()


# In[16]:


df['Route'].mode()[0]


# In[17]:


df['Route'].fillna(df['Route'].mode()[0],inplace=True)


# In[18]:


df['Total_Stops'].fillna(df['Total_Stops'].mode()[0],inplace=True)


# In[19]:


df['Airline'].value_counts()


# In[14]:


import matplotlib.pyplot as plt
sns.catplot(x='Airline',data=df,kind='count',aspect=2)
plt.xticks(rotation=90);


# **Findings:**
# 
#     There were 12 airlines in which "Jet Airways Airlines"  had the maximum no. of flights and "Trujet Airlines" had the minimum no. of flight.

# In[15]:


df["Source"].value_counts()


# In[16]:


sns.catplot(x='Source',data=df,kind='count')


# **Findings:**
# 
#     1. The maximum no.of flights were take off from "Delhi" and the minimum were from "chennai". 

# In[78]:


df["Source"].value_counts()/df.shape[0]*100


# In[14]:


plt.pie([i for i in df['Source'].value_counts()],labels=["Delhi","Kolkata","Banglore",'Mumbai','chennai'],autopct='%1.2f%%',explode=[0.1,0.2,0.3,0.4,0.5],radius=1);


# In[15]:


df.groupby(['Airline'])['Source'].value_counts()/df.groupby(['Airline'])['Source'].size()*100


# In[19]:


import matplotlib.pyplot as plt
sns.catplot(x='Airline',data=df,kind='count',hue='Source',aspect=2)
plt.xticks(rotation=70);


# **findings:**
# 
#     1. "Air asia airline": the max% of total, take off flights were from Kolkata and the minimum% from Delhi.
#     2. "Air india airline" : the max% of total,take off flights were from Delhi and the minimum% from chennai.
#     3. "GoAir airline" :the max% of total,take off flights were from Banglore and the minimum% from kolkata.
#     4. "Indigo airline" :the max% of total,take off flights were from Kolkata and the minimum% from Delhi.
#     5. "Jet Airways ":the max% of total,take off flights were from Delhi and the minimum% from Mumbai.
#     6. "Jet Airways Business": the max% of total,take off flights were from Mumbai and the minimum% from delhi.
#     7. "Multiple carriers " and "Multiple carriers Premium economy": take off from Delhi only.   
#     8. "SpiceJet airlines": the max% of total,take off flights were from Kolkata and the minimum% from Delhi. 
#     9. "Trujet": take off from mumbai only
#     10. "Vistara": the max% of total, take off flights were from Banglore and the minimum% from Mumbai.
#     11. "Vistara Premium economy": the max% of total,take off flights were from Banglore and the minimum% from chennai.   

# In[17]:


import matplotlib.pyplot as plt
sns.catplot(x='Source',data=df,kind='count',col='Airline',col_wrap=3)
plt.xticks(rotation=90);


# In[67]:


df.groupby(['Airline'])['Destination'].value_counts()/df.groupby(['Airline'])['Destination'].size()*100


# Findings:
# 
#     1. "Air asia airline": the max% of total, landed flights were in Banglore and minimum% were in Delhi.    
#     2. "Air india airline" : the max% of total,landed flights were in cochin and minimum% were in kolkata.    
#     3. "GoAir airline" :the max% of total,landed flights were in cochin and minimum% were in delhi.    
#     4. "Indigo airline" :the max% of total,landed flights were in cochin and minimum% were in Delhi.
#     5. "Jet Airways ":the max% of total,landed flights were in cochin and minimum% were in hyderabad.
#     6. "Jet Airways Business": the max% of total,landed flights were in new delhi and minimum% were in cochin.
#     7. "Multiple carriers " and "Multiple carriers Premium economy": landed flights were in cochin only.   
#     8. "SpiceJet airlines": the max% of total,landed flights were in banglore and minimum% were in new Delhi. 
#     9. "Trujet": landed flights were in hyderabad only
#     10. "Vistara": the max% of total, landed flights were in Banglore and minimum% were in hyderabad.
#     11. "Vistara Premium economy":landed  flights were in delhi ,kolkata,new delhi.
#         
# 

# In[20]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Air Asia']


# Findings:
# 
#     "Air Asia Airlines":
#     
#     1. the earliest fights were at 4:55 morning from Banglore and the last fights were at 11:55 at night from banglore
#     2. max no. of take off flights were at 4:45 evening from "Delhi"
#     3. most of the flights were in morning 

# In[21]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Air India']


# Findings:
#     
#     "Air India Airlines"
#     
#     1. The earliest flights were at 12:30 am from "Banglore" and last flights at 11:00 pm from Delhi
#     2. The max no. of take off flights were at 9:25 morning from "Kolkata".
#     3. The frequency of flights is more in between 5:00 am to 6:00 am.    

# In[22]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['IndiGo']


# **Findings:**
# 
#     "Indigo Airlines"
#     
#     1. The earliest flights were at 12:25 am from "Banglore" and the last flights were at 11:30 pm from Delhi and banglore
#     2. The max no. of take off flights were at 7:35 morning from "Delhi".
#     3. The frequency of flights is more in between 6:00 am to 8:00 am.    

# In[26]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Jet Airways']


# **Findings:**
# 
#     "Jet Airways Airlines"
#     
#     1. The earliest flights were at 12:20 am from "Delhi" and the last flights were at 11:05 pm from "Delhi"
#     2. The max no. of take off flights were at 6:30 morning and 6:55 in evening from "Kolkata". 
#     3. The frequency of flights is more in between 8:00 am to 10:00 am , 17:00 to 18:00 and 19:00 to 20:00.   

# In[57]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['SpiceJet']


# **Findings:**
#     "SpicJet Airlines"
#     
#     1. The earliest flights were at 5:45 am from "Mumbai and Banglore" and the last flights were at 11:45 pm from "Mumbai"
#     2. The max no. of take off flights were at 6:55 in morning and 9:00 in morning from "Kolkata".   

# In[59]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['GoAir']


# **Findings:**
#     "GoAir Airlines"
#     
#     1. The earliest flight was at 5:45 am from "Delhi" andthe last flights were at 11:30 pm from "Kolkata"
#     2. The max no. of take off flights were at 7:45 in morning from "banglore".   

# In[61]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()["Vistara"]


# **Findings:**
# 
#     "Vistara Airlines"
#     
#     1. The earliest flights were at 6:00 am from "Delhi" and the last flights were at 11:55 pm from "Mumbai"
#     2. The max no. of take off flights were at 7:10 in morning from "Kolkata".
#     3. frequency of flights were more in morning    

# In[64]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()["Jet Airways Business"]


# **Findings:**
# 
#     "Jet Airways Business"
#     
#     1. The earliest flights were at 5:45am from "Banglore" and the last flights were at 8:05 pm from "Delhi"
#     2. The max no. of take off flights were at 5:45 in morning from "Banglore".

# In[65]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Trujet']


# Findings:
# 
#     "Trujet Airlines"
#     
#     1.There was only 1 flight and that was at 13:05 from "Mumbai"

# In[68]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Multiple carriers']


# **Findings:**
# 
#     'Multiple carriers'
#     
#     1. The earliest flights were at 12:20 am and the last flights were at 7:00 pm from "Delhi"
#     2. The max no. of take off flights were at 7:05 in morning from "Delhi".

# In[23]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Vistara Premium economy']


# *Findings:**
# 
#     'Vistara Premium economy'
#     
#     1. The earliest flight was at 7:05 am from "Chennai" and the last flight was at 4:00 pm from "Banglore"

# In[70]:


df.groupby(["Airline",'Dep_Time'])['Source'].value_counts()['Multiple carriers Premium economy']


# **Findings:**
# 
#     'Multiple carriers Premium economy'
#     
#     1. The earliest flights were at 6:00 am and the last flight was at 7:00 pm from "Delhi"
#     2. The max no. of take off flights were at 6:00 in morning from "Delhi".

# In[76]:


df['Destination'].value_counts()


# In[77]:


sns.catplot(x='Destination',data=df,kind='count')


# In[4]:


df['Destination'].value_counts()/df.shape[0]*100


# In[6]:


plt.pie([i for i in df['Destination'].value_counts()],labels=['Cochin',"Banglore","Delhi","New Delhi","Hyderabad","Kolkata"],autopct='%1.2f%%',explode=[0,0.1,0.2,0.3,0.4,0.5],shadow=True);


# FINDINGS:
# 
#     1. 42.47%(max) of the flights landed in "Banglore" and 3.57%(max) landed in "Kolkata."

# In[21]:


df.groupby(["Airline"])['Arrival_time'].value_counts()


# In[20]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Air Asia"]


# findings:
# "Air Asia Airlines"
# 1. The max no. of flights arrived at "1:20 pm" in "Banglore".

# In[42]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["IndiGo"][120:140]


# findings:
# "IndiGo Airlines"
# 1. The max no. of flights arrived at "9:00 pm" in "Cochin".

# In[51]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Air India"][60:80]


# findings:
# "IndiGo Airlines"
# 1. The most of flights arrived at "7:15 pm" in "Cochin".

# In[52]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["SpiceJet"]


# findings:
# "SpiceJet Airlines"
# 1. The max no. of flights arrived at "12:40 am" in "Banglore".

# In[61]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Jet Airways"][:20]


# findings:
# "Jet Airways Airlines"
# 1. The max no. of flights arrived at "4:25 am" in "Cochin".

# In[62]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Multiple carriers"]


# findings:
# "Multiple carriers Airlines"
# 1. The max no. of flights arrived at "9:00pm" in "Cochin".

# In[64]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["GoAir"]


# findings:
# "GoAir Airlines"
# 1. The max no. of flights arrived at "10:40 am and 7:35 pm" in "Delhi and Cochin" respectively.

# In[65]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Vistara"]


# findings:
# "Vistara Airlines"
# 1. The max no. of flights arrived at "8:20 pm" in "Banglore" .

# In[67]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Vistara Premium economy"]


# Findings:
# "VistaraPremium economy":
# 1. It had only 3 flights and the arrival time were: 1. "9:20am" in "Kolkata
#                                        2. "2:20 pm" in "Delhi"
#                                        3. "6:35 pm" in "New Delhi  an arrival frequency was "1"
#                                                     

# In[68]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Jet Airways Business"]


# findings:
# "Jet Airways Business Airlines"
# 1. The max no. of flights arrived at "4:25 am" in "Cochin" .

# In[69]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Multiple carriers Premium economy"]


# findings:
# " Multiple carriers Premium economy Airlines"
# 1. The max no. of flights arrived at "3:30 am and 9:00 pm"  in "Cochin" .

# In[70]:


df.groupby(["Airline",'Arrival_time'])['Destination'].value_counts()["Trujet"]


# findings:
# "Trujet Airlines"
# 
# 1. It had only one flight and it arrived at "4:20 pm"  in "Hyderabad".

# In[75]:


import matplotlib.pyplot as plt
sns.catplot(x='Destination',data=df,kind='count',col='Airline',col_wrap=3)
plt.xticks(rotation=90);


# In[80]:


df['Total_Stops'].value_counts()


# In[81]:


sns.catplot(x='Total_Stops',data=df,kind="count")


# In[51]:


df.groupby(['Airline'])['Total_Stops'].value_counts()


# **Findings:**
# 
#     1. "Air asia": most of the flights were non stop flights
#     2. "Air India": most of the flights were 2 stops flights.
#     3. "GoAir": most of the flights were 1 stop flights.
#     3. "IndiGo": most of the flights were non stop flights.
#     5. "Jet Airways": most of the flights were 1 stop flights.
#     6. "Jet Airway Business": most of the flights were 1 stops flights.
#     7. "Multiple carriers": most of the flights were 1 stop flights.
#     8. "Multiple carriers Premium economy": most of the flights were 1 stop flights.
#     9. "spiceJet": most of the flights were non stop flights.
#     10. "Trujet": had 1 stop flight
#     11. "Vistara": most of the flights were non stop flights.
#     12. "Vistara Premium economy": had only the non stop flights.

# In[88]:


sns.catplot(x='Total_Stops',data=df,kind='count',col='Airline',col_wrap=3)


# In[100]:


df[df['Total_Stops']=="4 stops"]


# Findings:
# 
#     1. Most of the flights were of 1 stop
#     2. "Air India" had the highest stoppage (4 stops) from "Banglore to New Delhi"

# In[37]:


df['Additional_Info'].value_counts()/df.shape[0]*100


# Findings:
# 
#     1. most of the flights did provide any additional informations.
#     2. 18.55% of total, flights did not include In flight meals
#     3. 2.99% of total,flights did not include check in baggage    

# In[59]:


df.groupby(['Airline'])['Additional_Info'].value_counts()/df.groupby(['Airline'])['Additional_Info'].size()*100


# Findings:
# 
#     1. one flight of "Air Asia " was red eye flight
#     2. 0.34% of the "Air India" flights were 1 long layover flights, 0.057% were 1 short layover flights, 0.057% were 2         long layover and 0.399% flights were change airports flights.
#     3. 48.99% of the "Jet Airways" flights did not include meal in flights,0.311% were 1 long layover flights and 0.025%       were Business Class flights.
#     4. 50% of the "Jet Airways Business" flights were Business Class
#     5. 8.02% of the "Multiple carriers" flights did not include meal in flights
#     6. 0.12% of the "SpiceJet" flights were 1 long layover flights and 39.11% flights did not include check in baggage .
#     7. "GoAir,Indigo,Multiple carriers Premium economy, Trujet,vistara and Vistara Premium economy" did not provide any          additional information

# In[44]:


df.groupby(['Airline'])['Price'].agg(['max','min','mean'])


# In[72]:


df[df['Price']==max(df['Price'])]


# In[73]:


df[df['Price']==min(df['Price'])]


# Findings:
# 
#     1. All airlines had different Price for different routes .
#     2. The airline that had the most expensive fare : "Jet Airways Business" ( "Banglore to New Delhi" with 1stop).
#     3. The airline that had the cheapest fare: "SpiceJet" ( "Mumbai to Hyderabad")
#     4. On average "Trujet Airline" had min fare but remember that it had only one flight.

# In[41]:


sns.catplot(x='Airline',y='Price',data=df,kind='bar',aspect=2)
plt.xticks(rotation=90);


# In[42]:


sns.relplot(x='Airline',y='max',data=a,kind='line',ci=False)
plt.xticks(rotation=90);
sns.relplot(x='Airline',y='min',data=a,kind='line',ci=False)
plt.xticks(rotation=90);


# In[13]:


a=df.groupby(["Airline",'Route'])['Price'].agg(['max','min'])
a


# In[47]:


a.loc['Air Asia']


# **findings:**
# 
#     1. "Air Asia ":The route that had highest fare headed from "Delhi to banglore to Cochin"
#         and " Banglore to delhi " had lowest fare.

# In[103]:


a.loc['IndiGo']


# **findings:**
# 
#     1. "IndiGo ":The route that highest fare headed from "Banglore to Mumbai to Delhi" 
#         and " Mumbai to hyderabad " had the lowest fare.

# In[63]:


a.loc["Air India"]


# In[67]:


a.loc['Air India']['min'].idxmin()


# **findings:**
# 
#     1. "Air India":The route that had highest fare headed from "Kolkata to Banglore" and "Mumbai to hyderabad" had the lowest fare.

# In[68]:


a.loc['Jet Airways']


# In[69]:


a.loc['Jet Airways']['max'].idxmax()


# In[71]:


a.loc['Jet Airways']['min'].idxmin()


# **findings:**
# 
#     1."Jet Airways":Therouted that had highest fare headed from "Banglore to Mumbai to delhi" 
#         and "Mumbai to hyderabad" had the lowest fare.

# In[73]:


a.loc['SpiceJet']


# In[74]:


a.loc['SpiceJet']['max'].idxmax()


# In[75]:


a.loc['SpiceJet']['min'].idxmin()


# **findings:**
# 
#     1."SpiceJet":The route that had highest fare headed from "Banglore to Pune to delhi" 
#         and "Mumbai to hyderabad" had the lowest fare.

# In[81]:


a.loc['Multiple carriers']


# **findings:**
# 
#     1."Multiple carriers": The route that had highest fare headed from "delhi to Mumbai to cochin" 
#         and "delhi to Mumbai to cochin" also had the lowest fare .

# In[82]:


a.loc['GoAir']


# **findings:**
# 
#     1."GoAir":The route that had highest fare headed from "delhi to Mumbai to cochin" 
#         and "Banglore to delhi" had the lowest fare .

# In[83]:


a.loc['Vistara']


# **findings:**
# 
#     1."Vistara":The route that had highest fare headed from "Banglore to delhi" 
#         and "Banglore to delhi" also had the lowest fare .
#  

# In[84]:


a.loc['Vistara Premium economy']


# **findings:**
# 
#     1."Vistara":The route that had highest fare headed from "Banglore to delhi" 
#         and "Banglore to delhi" also had the lowest fare .

# In[85]:


a.loc['Jet Airways Business']


# **findings:**
# 
#     1."Jet Airways Business":The route that had highest fare headed from "Banglore to Mumbai to delhi" 
#         and "delhi to ATQ to Mumbai to cochin"  had the lowest fare .

# In[86]:


a.loc['Multiple carriers Premium economy']


# **findings:**
# 
#     1."Multiple carriers Premium economy":had only one route " Delhi to Mumbai to Cochin" 

# In[87]:


a.loc['Trujet']


# **findings:**
# 
#     1."Trujet":had only one route " Mumbai to NDC to hyderabad" 

# In[100]:


df.groupby(['Airline'])['Route'].value_counts()


# In[105]:


df.groupby(['Airline'])['Duration'].value_counts()


# In[112]:


df.loc[(df['Airline']=="Air Asia")]['Duration'].value_counts()


# In[113]:


df.loc[(df['Airline']=="Air Asia") &(df['Duration']=='15h 55m')]


# **findings:**
# "Air Asia"
# 1. Most of the flights duration were 2h 30m 
# 3. The longest duration of flights was 15h 55m
# 2. The flights that had the highest duration headed from the "Kolkata to Delhi to Banglore".

# In[125]:


df.groupby(['Airline'])['Duration'].value_counts()["IndiGo"][20:41]


# In[131]:


df.loc[(df['Duration']=='16h 15m') & (df["Airline"]=='IndiGo')]


# **findings:**
# "Indigo"
# 1. Most of the flights duration were 2h 50m 
# 3. The longest duration of flights was 16h 15m
# 2. The flights that had the highest duration headed from the " Delhi to Mumbai to Banglore".

# In[153]:


df.groupby(['Airline'])['Duration'].value_counts()["Air India"][200:]


# In[154]:


df.loc[(df['Duration']=='41h 20m') & (df["Airline"]=='Air India')]


# **findings:**
# "Air India"
# 1. Most of the flights duration were 2h 45m 
# 3. The longest duration of flight was 41h 20m
# 2. The flight that had the longest duration headed from the " Kolkata to Banglore" with 2 stops.

# In[58]:


df.groupby(['Airline'])['Duration'].value_counts()["Jet Airways"][240:]


# In[59]:


df[(df["Airline"]=="Jet Airways") &(df['Duration']=="47h 40m")]


# **findings:**
# "Jet Airways"
# 
# 1. Most of the flights duration were 3h 
# 3. The longest duration of flight was 47h 45m.
# 2. The flight that had the longest duration headed from the " Delhi to Cochin" with 2 stops.

# In[60]:


df.groupby(['Airline'])['Duration'].value_counts()["SpiceJet"]


# In[63]:


df[(df["Airline"]=="SpiceJet") &(df['Duration']=="8h 40m")]


# **findings:**
# "SpiceJet"
# 
# 1. Most of the flights duration were 2h 20m
# 3. The longest duration of flights was 8h 40m.
# 2. The flights that had the longest duration headed from the " Kolkata to Banglore" with 1 stop.

# In[69]:


df.groupby(['Airline'])['Duration'].value_counts()["Multiple carriers"][60:]


# In[70]:


df[(df["Airline"]=="Multiple carriers") &(df['Duration']=="15h 35m")]


# **findings:**
# "Multiple carriers"
# 
# 1. Most of the flights duration were 8h
# 3. The longest duration of flights was 15h 35m.
# 2. The flights that had the longest duration headed from the " Delhi to Cochin" with 1 stop.

# In[72]:


df.groupby(['Airline'])['Duration'].value_counts()["GoAir"]


# In[73]:


df[(df["Airline"]=="GoAir") &(df['Duration']=="9h 15m")]


# **findings:**
# "Multiple carriers"
# 
# 1. Most of the flights duration were 2h 55m.
# 3. The longest duration flight was 9h 15m.
# 2. The flight that had the longest duration headed from the " Kolkata to Banglore" with 1 stop.

# In[78]:


df.groupby(['Airline'])['Duration'].value_counts()["Vistara"][40:]


# In[79]:


df[(df["Airline"]=="Vistara") &(df['Duration']=="29h 10m")]


# **findings:**
# "Vistara"
# 
# 1. Most of the flights duration were 2h 50m.
# 3. The longest duration flight was 29h 10m.
# 2. The flight that had the longest duration headed from the " Kolkata to Banglore" with 1 stop.

# In[80]:


df.groupby(['Airline'])['Duration'].value_counts()["Vistara Premium economy"]


# In[81]:


df[(df["Airline"]=="Vistara Premium economy") &(df['Duration']=="2h 50m")]


# **findings:**
# "Vistara Premium economy"
# 
# 1. The longest duration flight was 2h 50m.
# 2. The flight that had the longest duration headed from the " Banglore to Delhi" with no stop.

# In[82]:


df.groupby(['Airline'])['Duration'].value_counts()["Jet Airways Business"]


# In[83]:


df[(df["Airline"]=="Jet Airways Business") &(df['Duration']=="6h 40m")]


# **findings:**
# "Jet Airways Business"
# 
# 1. The longest duration flights was 6h 40m.
# 2. The flight that had the longest duration headed from the "Banglore to New Delhi" wit 1stop.

# In[84]:


df.groupby(['Airline'])['Duration'].value_counts()["Multiple carriers Premium economy"]


# In[85]:


df[(df["Airline"]=="Multiple carriers Premium economy") &(df['Duration']=="13h 30m")]


# **findings:**
# "Multiple carriers Premium economy"
# 
# 1. Most of the flights duration were 6h 35m.
# 3. The longest duration flights was 13h 30m.
# 2. The flight that had the longest duration headed from the "Delhi to cochin" with 1 stop.

# In[86]:


df.groupby(['Airline'])['Duration'].value_counts()["Trujet"]


# In[87]:


df[(df["Airline"]=="Trujet") &(df['Duration']=="3h 15m")]


# **findings:**
# "Trujet"
# 
# 1. Trujet had only one flight and the duration of flight was "3h 15m" that  headed from "Mumbai to Hyderabad" with 1stop.
