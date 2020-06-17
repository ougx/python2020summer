# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:48:56 2020

@author: lthompson8
"""
#%% Exercise 1.1
#1. Write a format string (using str.format() and f'string') that will take the following four element tuple:
#( 2, 123.4567, 10000, 12345.67)
#and produce:
#'file_002 :   123.46, 1.00e+04, 1.23e+04'

#First using str.format()
"file_{:0>3} :    {:.2f}, {:.2e}, {:.2e}" .format( 2, 123.4567, 10000, 12345.67)

#%% Exercise 1.2
#now with f'string'
val1=  2
val2=123.4567
val3=10000
val4=12345.67
print(f"file_{val1:0>3}  :    {val2:.2f}, {val3:.2e}, {val4:.2e}")
#%% Excercise 2
#2. Write a python function that output the following formatted string based on the input iterable:
#'The n numbers are: i1, i2, i3, ...'
#where n is the number in the iterable and i1, i2 ... are the items inside the iterable.
#for example:
#func([1, 2, 3]) will return 'The 3 numbers are: 1, 2, 3'
#func((6, 7, 8, 9)) will return 'The 4 numbers are: 6, 7, 8, 9'

func=([6, 7, 8, 9])
func2= ', '.join([str(i) for i in func])
print(f"The {len(func)} numbers are: {func2}")

#%% Excercise 3
#3. Write a similar function as the last one but it inputs variable-length arguments instead
#func(1, 2, 3) will return 'The 3 numbers are: 1, 2, 3'
#func(6, 7, 8, 9) will return 'The 4 numbers are: 6, 7, 8, 9'

func=([6, 7, 8, 11000])
func2= ', '.join([str(i) for i in func])
print(f"The {len(func)} numbers are: {func2}")

#already seems to work fine for variable length arguments
#%% Excercise 4
#4. Write a format string (f'string') that will take the following tuple and return the formatted string below:
#Tuple: (4, 30, 2017, 2, 27)
#Return: '02 27 2017 04 30'

Tuple=(4, 30, 2017, 2, 27)
print(f"{Tuple[3]:0>2} {Tuple[4]} {Tuple[2]} {Tuple[0]:0>2} {Tuple[1]}")
#%% Exercise 5
#5. Write a format string (f'string') that will take the following input and return the formatted string below:
#Input: ['oranges', 1.3, 'lemons', 1.1]
#Return: 'The weight of an orange is 1.3 and the weight of a lemon is 1.1 and the total weight is 2.4'

Input=['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {Input[0]:.6} is {Input[1]} and the weight of a {Input[2]:.5} is {Input[3]} and the total weight is 2.4")

#This works, but is there a way to sum 1.3 and 1.1 using Input[0] and Input[3] within the f'string'????

#%% Exercise 6
#6. Write a function that will format each item in an input iterable object into a customized width
#syntax: func(iterable, width)
#for example:
#func([1, 2, 3, 4, 5], 3) return '  1  2  3  4  5'
#func([1, 2, 3, 4, 5], 2) return ' 1 2 3 4 5'

def func(iterable, width):
    string = ''
    for i in range(len(iterable)):
        number = iterable[i]
        string += (f"{number:{width}}")
    return string

print(func([1, 2, 3, 4, 6], 5))

#%% Exercise 7
#7. The USGS Water Data service provides retrival of streamflow data at the USGS stream gages. 
#The download url follows the pattern below. Write a Python program 
#1) generate the url for a given list of gage numbers; 
#2) read this url and download the data to csv file (do not use numpy or pandas); 
#3) based on the downloaded data calculate the monthly stasticstics including maximum, minimum and average of the streamflow data and save it to another csv file. 
    #The data need to be formatted to 2 decimal digits. 
#4) calculate the average annual runoff of each gage (expressed in acre-feet)

#url: https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no=06803495&referred_module=sw&period=&begin_date=2019-02-11&end_date=2020-02-11
#where &site_no=06803495 define which gages are included in this data retrieval; for multiple gages, simply repeat it, e.g. &site_no=06803495&site_no=06803486;
#the datas are specified by &period=&begin_date=2018-02-11&end_date=2020-02-11
#You could test your program using the gages ['06803495', '06803486'] for the period between 2000-10-1 and 2019-9-30

#Hint 1: using the str.format() method to construct the url.

#Hint 2: use the urllib.request.urlopen() to download the url:
#from urllib.request import urlopen
#    f = urlopen(a_url)
#    lines = f.readlines()
#Hint 3: skip the lines starts with # in the downloaded data.

#Hint 4: print some of the downloaded lines and identify the elements in each line.

#Hint 5: using the str.format() or f-string method to write csv file.

#Hint 6: the monthly stasticstics refer to the time series of monthly stasticstics.

#Hint 7: for the average annual runoff, you need to calculate the total runoff for each year and then calculate average of these annual runoff.
    
    
#generate URL for gages '060803495' and '06803486'

#Part1: generate URL for gages '060803495' and '06803486'
def usgsURL(gage1, gage2, startdate, enddate):
    return f"https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no={gage1}&site_no={gage2}&referred_module=sw&period=&begin_date={startdate}&end_date={enddate}"
print("URL:", usgsURL(gage1="06803495", gage2="06803486", startdate="2000-10-01", enddate="2019-09-30"))

#%% More robust generating of gages...
#Part 1: Generate URL
import urllib.request
import math
import datetime

def gen_url(gagelist, begin_date, end_date):
    try:
        bdate = datetime.date.fromisoformat(begin_date)
        edate = datetime.date.fromisoformat(end_date)
    except:
        raise ValueError ("The input formats for the begin_date and end_date must be YYYY-MM-DD")
        
    if type(gagelist) is not list:
        raise TypeError('The gagelist must be a list type.')
    
    if gagelist == []:
        raise ValueError('The gagelist must not be an empty list.')
        
    gages = ('&site_no={}' * len(gagelist)).format(*gagelist)
    period = f'&period=&begin_date={begin_date}&end_date={end_date}'
    return f'https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb{gages}&referred_module=sw{period}'

print('URL:', gen_url(['06803495', '06803486'], '2000-10-10', '2019-09-30'))

#Part2: read url and download the data to csv file
f = urllib.request.urlopen(gen_url(['06803495', '06803486'], '2000-10-10', '2019-09-30'))
lines = f.readlines()

for l in lines[:40]:
    print(l)

def save_date(data_lines, csvfile):
    for n, l in enumerate(data_lines):
        if not l.startswith(b'#'):
            break
    with open(csvfile, 'w') as f:
        f.write(data_lines[n].decode().replace('\t', ','))
        n += 2
        for i, l in enumerate(data_lines[n:]):
            if l.startswith(b'USGS'):
                f.write(l.decode().replace('\t', ','))
                
save_date(lines, 'usgs_streamflow.csv') 

! head -20 'usgs_streamflow.csv'

def save_date(data_lines, csvfile):
    for n, l in enumerate(data_lines):
        if not l.startswith(b'#'):
            break
    with open(csvfile, 'wb') as f:
        f.write(data_lines[n].replace(b'\t', b','))
        n += 2
        for i, l in enumerate(data_lines[n:]):
            if l.startswith(b'USGS'):
                f.write(l.replace(b'\t', b','))
                
save_date(lines, 'usgs_streamflow.csv') 

! head -20 'usgs_streamflow.csv'
! tail -20 'usgs_streamflow.csv'

#3) based on the downloaded data calculate the monthly stasticstics including maximum, minimum and average of the streamflow data and save it to another csv file. 
#The data need to be formatted to 2 decimal digits. 

def mean(lst): 
    try:
        while math.nan in lst:
            lst.remove(math.nan)
        return sum(lst) / len(lst) if len(lst) > 0 else 0
    except:
        print(' ')
            
def cal_month_stat(daily_csv, monthly_csv):
    site = ''
    date = ''
    begin = True
    with open(daily_csv) as f:
        f.readline()
        idx_site = 1
        idx_date = 2
        idx_val  = 3
        for i, l in enumerate(f):
            items = l.split(',')
            if items[idx_site] != site or items[idx_date][:7] != date:
                site = items[idx_site]
                date = items[idx_date][:7]
                key = f'{site},{date}'
                if begin:
                    site_month = {key: []}
                    begin = False
                else:
                    site_month[key] = []       
            if items[idx_val].replace('.', '0').isnumeric():
                site_month[key].append(float(items[idx_val]))
            else:
                print(' ')

#Write file with 2 decimals    
    with open(monthly_csv, 'w') as fw:
        fw.write('site_no,month,mean,min,max\n')
        for k in site_month:
            if site_month[k] == []:
                print(k, site_month[k]) 
            else:
                fw.write(f'{k}-01,{mean(site_month[k]):.2f},{min(site_month[k]):.2f},{max(site_month[k]):.2f}\n')
            
cal_month_stat('usgs_streamflow.csv', 'monthly_streamflow.csv')
! head -20 'monthly_streamflow.csv'
! tail -20 'monthly_streamflow.csv'


#4) calculate the average annual runoff of each gage (expressed in acre-feet)
def cal_annual_runoff(daily_csv, annual_runoff_csv):
    site = ''
    year = ''
    begin = True
    with open(daily_csv) as f:
        #skip the header
        f.readline()
        idx_site = 1
        idx_date = 2
        idx_val  = 3
        for i, l in enumerate(f):
            items = l.split(',')

            if items[idx_site] != site or items[idx_date][:4] != year:
                site = items[idx_site]
                year = items[idx_date][:4]
                key = f'{site},{year}'
                if begin:
                    site_year = {key: []}
                    begin = False
                else:
                    site_year[key] = []
                           
            if items[idx_val].replace('.', '0').isnumeric():
                site_year[key].append(float(items[idx_val]) * 86400 / 43560)
    
#write file with 2 decimals.
    with open(annual_runoff_csv, 'w') as fw:
        fw.write('site_no,year,runoff\n')
        for k in site_year:
            fw.write(f'{k}-01-01,{sum(site_year[k]):.2f}\n')
            
cal_annual_runoff('usgs_streamflow.csv', 'annual_runoff.csv')
! head -20 'annual_runoff.csv'
! tail -20 'annual_runoff.csv'

