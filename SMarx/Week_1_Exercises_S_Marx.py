# Week 1 Exercises, Sam Marx

#1 Seconds in 42 minutes and 42 seconds
minutes=42
seconds=42
print('Total seconds =', minutes*60 +seconds)
#2 Miles in 10km
kilometers=10
miles=kilometers*1.61
print(kilometers, 'km=', miles, 'miles')
#3 If you run 1 10km race in 42 min 42 s, what is your average pace?  What is your average speed?
minutes=42
seconds=42
TotalSeconds= minutes*60 +seconds
TotalHours=TotalSeconds/3600
kilometers=10
miles=kilometers*1.61
pace=(TotalSeconds/60)/miles
print('Pace=',pace, 'minutes/mile')
print('Avg Speed=', miles/TotalHours, 'MPH')
#4 Python program to convert radian to degree
import math
rad=1
deg=rad * 180/math.pi
print(rad,'radians=', deg, 'degrees')
#5 Python program to calculate surface volume and are of a cylinder with height 4 and radiu 6.
import math
h=6
r=4
Volume=math.pi*r**2*h
print('volume=',Volume, 'units^3')
SurfaceArea=2*math.pi*r*h+2*math.pi*r**2
print('surface area=',SurfaceArea, 'units^2')
#6 Python program to caculate the distance between two points using lat and lon.
#written using the halversine formula (found on Google)
import math
Lat1=41.727489
Lat2=41.364629
Lon1=-99.442851
Lon2=-99.530958
Lat1=Lat1*math.pi/180
Lat2=Lat2*math.pi/180
Lon1=Lon1*math.pi/180
Lon2=Lon2*math.pi/180
r=6371 #Earth's radius in km
d=2*r*math.asin(math.sqrt((math.sin((Lat2-Lat1)/2)**2)+(math.cos(Lat1)*math.cos(Lat2)*(math.sin((Lon2-Lon1)/2)**2))))
print('Distance=',d, 'km')
#7 Print a stop sign
print('    _____    ')
print('  /       \  ')
print(' /         \ ')
print('|    STOP   |')
print(' \         / ')
print('  \_______/  ')

print('OR')

print('    ________    ')
print('   /        \   ')
print('  /          \  ')
print(' / _ _  _   _ \ ')
print('| |_ | | | |_| |')
print('|  _|| |_| |   |')      
print(' \            / ')
print('  \          /  ')      
print('   \________/   ')


