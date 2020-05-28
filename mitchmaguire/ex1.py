# -*- coding: utf-8 -*-
"""
Created on Thu May 28 08:48:27 2020

@author: mmaguire2
"""
# converts minutes and secnods to seconds
def time_to_seconds(minutes, seconds): 
    seconds = minutes*60 + seconds
    return seconds

# converts kilometers to miles
def km_to_miles(kilometers): 
    miles = kilometers*1.61
    return miles

# calulates race pace based on distance ran(km), minutes and seconds it took to complete the race
# calulated average speed
def race_pace(kilometers, minutes, seconds):
    distance = km_to_miles(kilometers)
    time = time_to_seconds(minutes, seconds)
    pace = time/distance
    pace_min = int( pace / 60)
    pace_seconds = pace % 60
    speed = distance / time * 3600
    return print("Average pace: %d minutes and  %f seconds, Average speed %f mph" % (pace_min, pace_seconds, speed))

    
# converts radians to degrees
import math   
def radians_to_degrees(radians):
    degrees = radians * 180/math.pi
    return degrees   

# calculated volume and surface area of a cylinder given the height and radius of cylinder
def calc_vol_area(height, radius):
    volume = math.pi*radius**2*height
    surface_area = 2*math.pi*radius*height + 2*math.pi*radius**2
    return volume, surface_area

# calculates distance between two lat long points
def calc_distance(point1_lat,point1_long,point2_lat,point2_long):
    distance = math.sqrt((point1_lat-point2_lat)**2+(point1_long-point2_long)**2)
    return distance

# print stop sign
print("  ______")
print(" /      \\")
print("/        \\")
print("|  STOP  |")
print("\\        /")
print(" \\      /")
print("  ------")