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
