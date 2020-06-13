# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:07:08 2020

@author: lthompson8
"""
#%% 1. Given two 1-d arrays of simulated values and observed values, Write a Pyhton function
#to calculate the mean error, coefficient of determination and nash coefficient. Loops are NOT allowed.
import numpy as np
ObservedValues = np.array([1, 40, 31, 40, 57, 88])
SimulatedValues = np.array([-13, 79, 71, 81, 104, 42])
print(SimulatedValues)
print(ObservedValues)

#MSE
mse = np.mean((ObservedValues - SimulatedValues)**2)
print('mean error:', mse)

#coefficient of determination
correlation_matrix = np.corrcoef(SimulatedValues, ObservedValues)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print('coefficient of determination:', r_squared)

#Nash
numerator = np.nansum((SimulatedValues - ObservedValues)**2)
denominator = np.nansum((SimulatedValues-np.mean(ObservedValues))**2)
NSE = 1 - (numerator/denominator)
print('nash efficiency:', NSE)
#%% 2. Given x and y, write a Python function to perform linear regression
# which returns a, c and sum of square errors where ax + c = y
# def linear_regression(x, y):
#    return a, c, ssqe
def linear_regression(x, y):
    #first get rid of nans
    not_nan = ~ (np.isnan(x) | np.isnan(y))
    x = np.array(x)[not_nan]
    y = np.array(y)[not_nan]
    if x.size != y.size:
        print('the sizes are different between x and y')
        return
    sumx = x.sum()
    sumxx = (x ** 2).sum()
    sumy = y.sum()
    sumxy = (x*y).sum()
    n = x.size
    a = (sumxy - sumx * sumy / n) / (sumxx - sumx ** 2 / n)
    c = y.mean() - a * x.mean()
    ssqe = np.nansum((a * x + c - y) **2)
    return a, c, ssqe
    
x = ObservedValues
y = SimulatedValues
linear_regression(x,y)
    
#%% 3. Eestimate the mean precipitation on different land use types.
#create the datasets
landuse = np.random.randint(1, 5, [5, 5])
precip  = np.random.random([5, 5])
print('landuse\n', landuse)
print('precip \n', precip)

#can call for individual landuse precips...
landuse1precip = (precip[landuse == 1]).mean()
print(landuse1precip)

#calculation
def landuse_precipitation(landuse, precip, prefix='landuse'):
    return [(f'{prefix}{i}', (precip[landuse == i]).mean()) for i in np.unique(landuse)]
landuse_precipitation(landuse, precip)

#if I can get month and year separated in lecture 5 exercise, I could maybe use this to calculate average monthly flow for the hydrology question.
#but would be using numpy

#%% 4. We have two array. The first array is the distribution of irrigated land.
#The second array is the precipitation.
landuse = np.random.randint(0, 1, [6, 6])
precip  = np.random.random([6, 6])

print('landuse\n', landuse)
print('precip\n', precip)

#A. Create a function to create the buffer zones of varied distances to the irrigated land.
#is 1 the irrigated land and 0 is the non-irrigated?

import matplotlib.pyplot as plt
plt.imshow(landuse)

#keep getting landuse of all 0 in random. Will create array myself to make some irrigated always present.
#this will be landuse 2

landuse2 = [
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1],
]

plt.imshow(landuse2)

#ok, now I have irrigated land [1] to work with.
#need to define center distance array
distance_x = np.arange(13).reshape([1, 13])
distance_y = np.arange(13).reshape([13, 1])
distance = np.sqrt((distance_x - 6) ** 2 + (distance_y -6) ** 2)
plt.imshow(distance, cmap='jet'); plt.colorbar()
#this plot shows distance from center on a 13 x 13 grid.

def create_buffer(landuse2, distance=distance):
    
    buffer = np.full_like(landuse2, 1e9)
    #Full_like = return a full array with the same shape and type as a given array.
    n , m = buffer.shape
    index = np.nonzero(landuse2)
    for i, j in np.array(index).T:
        #.T is the transposed array. not clear on why it needs to be transposed.
        distance_buffer = distance[(6-i):(6-i+n), (6-j):(6-j+m)]
        buffer = np.where(distance_buffer < buffer, distance_buffer, buffer)
    return buffer

buffer = create_buffer(landuse2)
plt.imshow(buffer, cmap='jet'); plt.colorbar()

#B. Calculate the mean precipitation in the buffer zones of different distance to the irrigated land.

landuse_precipitation(buffer, precip, prefix='')
#uses previously created function named landuse_precipitation.

#%% 5. Write a Python function to find the nearest point of a list of given points.
#You are not allowed to use any type of loops.
# e. g. points = [(3, 4), (1, 2), (7, 8), (9, 4), (6, 5), (8, 7), (4, 7)]
# Hint: using numpy to create a N x N array which contain the distances between each ith an jth point pair; where N is the numer of points.

points = [(3, 4), (1, 2), (7, 8), (9, 4), (6, 5), (8, 7), (4, 7)]
for x, y in points:
    plt.scatter(x , y, 10)
    
pointsarray = np.array(points)
print(pointsarray)
distances = ((pointsarray.reshape(7, 1, 2) - pointsarray.reshape(1, 7, 2)) ** 2).sum(axis=2)
#arguments in reshape are = a, newshape, order=c. 
#There are 7 pairs of 2. Not sure what the 1 is.
#don't understand how 7, 1, and 2 are applied? 
print(pointsarray.reshape(7, 1, 2))
#this makes an array of 7 pairs of 2 spread out horizontally like:
# [3 4] [1 2] [7 8] [9 4] [6 5] [8 7] [4 7]
#so the arguments are saying 7 columns, with one row, and pairs of 2
print(pointsarray.reshape(1, 7, 2))
#this makes an array of 7 pairs of 2 spread vertically like:
#so the argument here is saying 1 column, with 7 rows, and pairs of 2
# [3 4]
# [1 2]
# [7 8]
# [9 4]
# [6 5]
# [8 7]
# [4 7]
print(pointsarray.reshape(7, 1, 2)-(pointsarray.reshape(1, 7, 2)))
# then these are simply subtracted so there are 49 pairs of numbers
print((pointsarray.reshape(7, 1, 2) - pointsarray.reshape(1, 7, 2)) ** 2)
#Then do squares of each number
print(distances)
#Then sums the paired squares so now back to 7 numbers

distances[np.arange(7), np.arange(7)] = 1e9
#1e9 is 1000000000. why is this used? - ok, this goes in the center line of the matrix, like the 1.0 if the values were decimals
np.argmin(distances, axis=0)
print(np.argmin(distances, axis=0))
#don't understand how the subtracting, squaring, and summing gets us to a distance between the original points.....??
# I guess we are actually trying to get distnace between points, which are pairs...