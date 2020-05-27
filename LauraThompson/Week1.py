# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% Question 0
print('Hello, NRES898!')
print('Hello, Michael')

#%% Question 1
print('Total seconds is', 42*60+42)


#%% Question 2
print('There are', 10/1.61, 'miles in 10 kilometers')

#%% Question 3
print('Your pace in miles per minutes and seconds is', (10/1.61), 'miles in 42 min 42 sec')
print('Your speed in miles per hours is', (10/1.61)/(2562/60/60), 'mph')

#%% Question 4
import math
degree = r * (180/math.pi)
#test
r = 5
print('5 radians equal', degree, 'degrees')
print('1 radian equals', degree, 'degrees')

#%% Question 5
import math
h=4
r=6
v = math.pi * r **2 * h
print('Volume is ',v)
a = 2 * math.pi * r * h + 2*math.pi*r**2
print('Area is ',a)

#%% Question 6
import math
 
#test input lat and long here:
lata=40.0726474712
longa=-95.60997
latb=40.429647
longb=-87.051524

#Convert from degrees to radians
lata= math.radians(lata)
longa= math.radians(longa)
latb= math.radians(latb)
longb= math.radians(longb)

#Haversine formula
r=3956
d=r*math.acos((math.sin(lata)*math.sin(latb))+math.cos(lata)*math.cos(latb)*math.cos(longb-longa))
print(d)

print("distance is", d, "miles")

#%% Question 7
print('   ---   ')
print('  /   \  ')
print(' /     \ ')
print('|  STOP |')
print(' \     /')
print('  \   / ')
print('   ---   ')
