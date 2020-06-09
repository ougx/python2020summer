
# 1. Write a format string (using str.format() and f'string') that will take the following four element tuple:
#   (2, 123.4567, 10000, 12345.67)
#   and produce:
#   'file_002 :   123.46, 1.00e+04, 1.23e+04'

print('Using str.format():')
print('file_{:>03}: {:.5} {:.2e} {:.2e}'.format(2, 123.4567, 10000, 12345.67))
print('Using f String:')
tup=(2, 123.4567, 10000, 12345.67)
print(f'file_{tup[0]:>03}: {tup[1]:.5} {tup[2]:.2e} {tup[3]:.2e}')

#  2. Write a python function that output the following formatted string based on the input iterable:
#   'The n numbers are: i1, i2, i3, ...'
#    where n is the number in the iterable and i1, i2 ... are the items inside the iterable.
#   for example:
#   func([1, 2, 3]) will return 'The 3 numbers are: 1, 2, 3'
#   func((6, 7, 8, 9)) will return 'The 4 numbers are: 6, 7, 8, 9'

#input_iterable=[1,2,3]
def iterable(input_iterable):
    length=len(input_iterable)
    print(f'The {length} numbers are: {input_iterable[0]},{input_iterable[1]},{input_iterable[2]}')
iterable([1,2,3])
def iterable(input_iterable):
    length=len(input_iterable)
    print(f'The {length} numbers are: {input_iterable[0]},{input_iterable[1]},{input_iterable[2]},{input_iterable[3]}')
    
iterable([6,7,8,9])


#  2. Write a python function that output the following formatted string based on the input iterable:
#   'The n numbers are: i1, i2, i3, ...'
#    where n is the number in the iterable and i1, i2 ... are the items inside the iterable.
#   for example:
#   func([1, 2, 3]) will return 'The 3 numbers are: 1, 2, 3'
#   func((6, 7, 8, 9)) will return 'The 4 numbers are: 6, 7, 8, 9'

#input_iterable=[1,2,3]
def iterable(input_iterable):
    length=len(input_iterable)
    print(f'The {length} numbers are: {str(input_iterable)[1:-1]}')
iterable([1,2,3])    
iterable([6,7,8,9])

#  4. Write a format string (f'string') that will take the following tuple and return the formatted string below:
#     Tuple: (4, 30, 2017, 2, 27)
#     Return: '02 27 2017 04 30'

tup=(4, 30, 2017, 2, 27)
print('The input is:', tup)
print(f'The output is: {tup[0]-2} {tup[1]-3} {tup[2]} {tup[3]+2} {tup[4]+3}')

# 5. Write a format string (f'string') that will take the following input and return the formatted string below:
#   Input: ['oranges', 1.3, 'lemons', 1.1]
#   Return: 'The weight of an orange is 1.3 and the weight of a lemon is 1.1 and the total weight is 2.4'

ind=['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {ind[0]:.6} is {ind[1]} and the weight of a {ind[2]:.5} is {ind[3]} and the total weight is {(ind[1]+ind[3]):.2}')

# 6. Write a function that will format each item in an input iterable object into a customized width
# syntax: func(iterable, width
# for example:
# func([1, 2, 3, 4, 5], 3) return '  1  2  3  4  5'
# func([1, 2, 3, 4, 5], 2) return ' 1 2 3 4 5'
def input_variables(iterable, width):
    print(f'{iterable[0:-1]:>{width}s}'})   
input_variables([1,2,3,4,5],2)
input_variables([1,2,3,4,5],3)
#I know that the number for the width needs to inserted into the index spacing, but couldn't come up with the correct syntax to do so. 

# 7. The USGS Water Data service provides retrival of streamflow data at the USGS stream gages. 
#The download url follows the pattern below. Write a Python program 
#   1) generate the url for a given list of gage numbers; 
#   2) read this url and download the data to csv file (do not use numpy or pandas); 
#   3) based on the downloaded data calculate the monthly stasticstics including maximum, minimum and average of 
#      the streamflow data and save it to another csv file. The data need to be formatted to 2 decimal digits. 
#   4) calculate the average annual runoff of each gage (expressed in acre-feet)

# url: https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no=06803495&referred_module=sw&period=&begin_date=2019-02-11&end_date=2020-02-11

# where &site_no=06803495 define which gages are included in this data retrieval; for multiple gages, simply repeat it, e.g. &site_no=06803495&site_no=06803486;
# the datas are specified by &period=&begin_date=2018-02-11&end_date=2020-02-11
# You could test your program using the gages ['06803495', '06803486'] for the period between 2000-10-1 and 2019-9-30
# Hint 1: using the str.format() method to construct the url.
# Hint 2: use the urllib.request.urlopen() to download the url:
# from urllib.request import urlopen
#     f = urlopen(a_url)
#     lines = f.readlines()
# Hint 3: skip the lines starts with # in the downloaded data.
# Hint 4: print some of the downloaded lines and identify the elements in each line.
# Hint 5: using the str.format() or f-string method to write csv file.
# Hint 6: the monthly stasticstics refer to the time series of monthly stasticstics.
# Hint 7: for the average annual runoff, you need to calculate the total runoff for each year and then calculate average of these annual runoff.

# #5.7.1 Attempt made but unsuccessful
# import urllib
# getVars={'var1':'some_data', 'var2':1337}
# url='http://domain.com/somepage/?'
# print(url+urllib.urlencode(getVars))

#5.7.2
import urllib.request

webUrl=urllib.request.urlopen('https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no=06803495&referred_module=sw&period=&begin_date=2019-02-11&end_date=2020-02-11')
print('result code:' +str(webUrl.getcode()))
outF=open("file_test.txt","w")
for line in webUrl:
    decoded_line=line.decode("utf-8")
    outF.write(decoded_line)
    print(decoded_line)
outF.close()

#Made multiple attempts at skipping lines that start with # (two sections that are commented below),
#using both methods found in class examples and examples online with no success.  Unable to complete parts 3 and 4. 

# import itertools
# new_data=open("new_data.txt", "w")
# with open("file_test.txt", "r") as f:
#     for line in itertools.islice(f,56,None):
#         new_data.write(f)
#         print(new_data)
# new_data.close()

# webUrl=urllib.request.urlopen('https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb&site_no=06803495&referred_module=sw&period=&begin_date=2019-02-11&end_date=2020-02-11')
# print('result code:' +str(webUrl.getcode()))           
# outSkip=open("line_test.txt","w")
# for line in webUrl:
#     decoded_line=line.decode("utf-8")        
#     outSkip.write(decoded_line)
#     outSkip.write("\n")
#     if line.startswith("#"):
#         continue
#     else:
#         print(decoded_line)
# outSkip.close()

