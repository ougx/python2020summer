# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:53:21 2020

@author: lthompson8
"""

#%%
#1. Use Pandas to repeat the Exercise 5.7.
#Hint 1: Use pd.read_csv(url, ...) to read the USGS online gauge data.

import pandas as pd
import os

url = "https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no=06803495&site_no=06803486&referred_module=sw&period=&begin_date=2000-10-01&end_date=2019-09-30"
#df = pd.read_csv(url, skiprows=range(0,28), sep='\n')
df = pd.read_csv(url, skiprows=29, delimiter='\t', header=0, names=['org','gage','date','flow','estimate'])
print(df)
dirPath = r'C:\Users\lthompson8\python2020summer\LauraThompson\Exercise7'
fileName = 'USGS_Streamflow_Data.csv'
fullPath = os.path.join(dirPath, fileName)
print(fullPath)

df.to_csv(fullPath, index=False)
#Hint 2: Use df.set_index() to set the datetime column and df.resample() to calculate the monthly and annual statistics

df['date']= pd.to_datetime(df['date'], errors='coerce')
print(df)
df.info()
df = df.set_index(['date'])

#change flow to numeric type
df['flow'] = pd.to_numeric(df['flow'], errors='coerce')
df.info()

#create empty dataframe for monthly stats to go into
MonthlyStats = pd.DataFrame(columns=['Min','Max','Mean'])
print(MonthlyStats)
#put data in! "M" resamples by Month
#use following code if you want to go across both gages.
#MonthlyStats.Min = df.flow.resample('M').min()
#MonthlyStats.Max = df.flow.resample('M').max()
#MonthlyStats.Mean = df.flow.resample('M').mean()

#can also do this by gage if desired using code below, but instructions seem like we should average across gages.
df['gage'] = pd.to_numeric(df['gage'], errors='coerce')
MonthlyStats.Min = df.flow.groupby(df['gage']).resample('M').min()
MonthlyStats.Max = df.flow.groupby(df['gage']).resample('M').max()
MonthlyStats.Mean = df.flow.groupby(df['gage']).resample('M').mean()


fileName = 'MonthlyStreamflowStats.csv'
fullPath = os.path.join(dirPath, fileName)
print(fullPath)
MonthlyStats.to_csv(fullPath, float_format='%.2f')
#4) calculate the average annual runoff of each gage (expressed in acre-feet)
#Hint 7: for the average annual runoff, you need to calculate the total runoff for each year and then calculate average of these annual runoff.
#create empty dataframe for yearly total
YearlyTotal = pd.DataFrame(columns=['AcreFeet'])
#convert to acre-feet
df['AcreFeetPerDay'] = df['flow']*1.98347
#resample by year with "Y" and include groupby to create separate for each gage.

df['gage'] = pd.to_numeric(df['gage'], errors='coerce')
df.info()
YearlyTotal.AcreFeet = df.AcreFeetPerDay.groupby(df['gage']).resample('Y').sum()
YearlyTotal
              
fileName = 'AnnualAcreFeet.csv'
fullPath = os.path.join(dirPath, fileName)
print(fullPath)
YearlyTotal.to_csv(fullPath, float_format='%.2f')


#%%
#2. Use Pandas to:
#2.1 Read data in data/users.zip (using Pandas' the on-the-fly decompression cabability)
import pandas as pd
import os
userdata = pd.read_csv('C:/Users/lthompson8/python2020summer/LauraThompson/users.zip', sep='|')
userdata = userdata.set_index('user_id')
userdata.info()
print(userdata)
#2.2 Identify all the occupations and compare the user numbers between STEM-related occupations and non-STEM occupations.
#first idenfity the occupations that are considered STEM.
#view all occupations with pivot table
userdata.pivot_table(index='occupation', aggfunc=['min','max','mean','std'])

#for total number of stem careers:
stem_careers = ('engineer', "programmer", "scientist", "technician", "doctor")
print(stem_careers)
    # create empty stem total list
stem_careers_total = 0
for item in stem_careers:
    num = len(userdata[userdata["occupation"] == item])
    print(f'{item} = {num}')
    stem_careers_total += num

#for total number of non-stem careers:
non_stem_careers = ('administrator', 'artist', 'educator', 'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer', 'librarian', 'marketing', 'none', 'other', 'retired', 'salesman', 'student', 'writer')
non_stem_careers_total = 0
for item in non_stem_careers:
    num = len(userdata[userdata["occupation"] == item])
    print(f'{item} = {num}')
    non_stem_careers_total += num

#to get total remaining careers (across career), will sum the total number of users, then subtract the non stem
totalall = len(userdata.index)

print('Total users is = ', totalall)
print('Total STEM users is = ', stem_careers_total)
print('Total non-STEM users is = ', non_stem_careers_total)

#2.3 Identify the locations of the users that are programmers and above 35. 
userdata.info()
programmers = userdata.query('occupation == "programmer"')
programmersunder35 = programmers.query('age < 35')
programmersunder35location = (programmersunder35.zip_code)
print(f"zip code locations of programmers under 35 = {programmersunder35location}")
youngprogrammerslocation = userdata.query('occupation == "programmer" & age < 35').groupby(['zip_code'])['zip_code'].count()
print(youngprogrammerslocation)

#2.4 How many male and female programmers, respectively? 
programmergender = programmers.query('occupation == "programmer"').groupby(programmers['gender']).count()
print(programmergender)
maleprogrammers = programmergender['gender']['M']
femaleprogrammers = programmergender['gender']['F']
print(f"The number of male programmers is {maleprogrammers} and number of female programmers is {femaleprogrammers}")

#2.5 Is this ratio the same for the age under 35?
#split previous by under 35 and greater or equal to 35.
print(programmers)
programmers.info()
youngprogrammers = programmers.query('occupation == "programmer" & age < 35').groupby(programmers['gender']).count()
youngmaleprogrammers = youngprogrammers['gender']['M']
youngfemaleprogrammers = youngprogrammers['gender']['F']
print(f"The number of male programmers under 35 is {youngmaleprogrammers} and the number of female programmers under 35 is {youngfemaleprogrammers}.")
ratioyoungprogrammers = f'{youngmaleprogrammers/youngfemaleprogrammers:.2f}'
print(f"The ratio of male to female programmers in the under 35 group is {ratioyoungprogrammers}.")

olderprogrammersgender = programmers.query('age >= 35').groupby(programmers['gender']).count()
oldermaleprogrammers = olderprogrammersgender['gender']['M']
olderfemaleprogrammers = olderprogrammersgender['gender']['F']
print(f"The number of male programmers over 35 is {oldermaleprogrammers} and the number of female programmers over 35 is {olderfemaleprogrammers}.")
ratioolderprogrammers = f'{oldermaleprogrammers/olderfemaleprogrammers:.2f}'
print(f"The ratio of male to female programmers in the 35 and over group is {ratioolderprogrammers}.")

#2.6 Compare the numbers of male and female for each occupations
occupationstatsbygender = userdata.groupby(['occupation', 'gender'])['gender'].count()
print(occupationstatsbygender)

#2.7 Find the occupations with the youngest and oldest mean ages, respectively

#find mean ages first
meanages = userdata.groupby(['occupation'])['age'].mean()
#sort
print(meanages.sort_values().round(decimals=2))
#find youngest
youngestoccupation = meanages.idxmin()
print(f'{youngestoccupation} is the occupation with the youngest mean age with a mean age of {meanages.min():.1f} years')
#find oldest
oldestoccupation = meanages.idxmax()
print(f'{oldestoccupation} is the occupation with the youngest mean age with a mean age of {meanages.max():.1f} years')

#2.8 Based on the first two digits of the zip codes, find the area with the largest number of users
#shorten zipcode 
userdata['shortzip'] = userdata['zip_code'].str[:2]
userdata.info()
usersbyregion = userdata.groupby(['shortzip'])['occupation'].count()
maxuserszip = usersbyregion.idxmax()
print(f"The largest number of users is in the zip code prefix {maxuserszip}.")



#userdata.pivot_table(values='age', index='occupation', columns='gender', aggfunc=['min','max','mean','std'])
