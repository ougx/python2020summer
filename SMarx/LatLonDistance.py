#written using the halversine formula (found on Google)
import math
Lat1=53.32055555555556
Lat2=53.31861111111111
Lon1=-1.7297222222222221
Lon2=-1.6997222222222223
Lat1=Lat1*math.pi/180
Lat2=Lat2*math.pi/180
Lon1=Lon1*math.pi/180
Lon2=Lon2*math.pi/180
r=6371 #Earth's radius in km
d=2*r*math.asin(math.sqrt((math.sin((Lat2-Lat1)/2)**2)+(math.cos(Lat1)*math.cos(Lat2)*(math.sin((Lon2-Lon1)/2)**2))))
print('Distance=',d, 'km')
