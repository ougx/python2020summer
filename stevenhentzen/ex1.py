#%% Question 1

m = 42
s = 42

print('Total seconds: ', (m*60)+s)

#%% Question 2

km = 10
mi = 1.61*km
print('Total miles:', mi)

#%% Question 3

km = 10
mi = 1.61*km
m = 42
s = 42
hr = (s/60+m)/60
print('Average speed in mph: ', round(mi/hr, 2))

#%% Question 4
import math

print('\nRadian to Degree Converter')
rad = float(input('Enter radians: '))
degree = rad*(180/math.pi)
print(degree)

#%% Question 5
import math 
print('\nCylinder Surface Area and Volume Calculator')
h = float(input('Enter Cylinder Height: '))
r = float(input('Enter Cylinder Radius: '))
SA = ((2*math.pi*r*4)+(2*(math.pi*r**2)))
V = (4*(math.pi*r**2))
print('Surface Area: ', round(SA, 2))
print('Volume: ', round(V, 2))

#%% Question 6
import math

print("\nDistance Between Two Points of Latitude and Longitude")
latA = float(input('Enter Point \"A\" Latitude: '))
lonA = float(input('Enter Point \"A\" Longitude: '))
latB = float(input('Enter Point \"B\" Latitude: '))
lonB = float(input('Enter Point \"B\" Longitude: '))
latDif = (latA-latB)*math.pi/180
lonDif = (lonA-lonB)*math.pi/180
R = 6371
a = math.sin(latDif/2)*math.sin(latDif/2)+math.cos(latA*math.pi/180)*math.cos(latB*math.pi/180)*math.sin(lonDif/2)*math.sin(lonDif/2)
c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
dist = R*c

print('\nDistance between two points in km: ', round(dist))

#%% Question 7

print('  ____  ')
print(' /    \\')
print('/      \\')
print('| STOP |')
print('\\      /')
print(' \\____/')
