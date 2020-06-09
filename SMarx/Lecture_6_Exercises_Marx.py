#6.1 Given two 1-d arrays of simulated values and observed values, Write a Pyhton function
#    to calculate the mean error, coefficient of determination and nash coefficient. 
#    Loops are NOT allowed.

import numpy as np
As=[1,2,3]
Ao=[1.1,2.1,3.3]
np.As=(As)
np.Ao=(Ao)
print('Simulated:', np.array(As),'Observed:', np.array(Ao))
Error=np.array(Ao)-np.array(As)
print('Error:', Error)
Mean_Error=np.mean(Error/(np.array(Ao),np.array(As)))
print('Mean Error is:', Mean_Error)

correlation_matrix=np.corrcoef(As,Ao)
correlation_AsAo=correlation_matrix[0,1]
R_Squared=correlation_AsAo**2
print('R^2:', R_Squared)

# 6.2 Given x and y, write a Python function to perform linear regression
#     which returns a, c and sum of square errors where ax + c = y
#         def linear_regression(x, y):
#           return a, c, ssqe

import numpy as np
from scipy import stats
def linear_regression(x,y):
    x=np.As
    y=np.Ao
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    print("slope:", slope, "intercept:", intercept, "R^2 Error:", r_value**2)

linear_regression([1,2,3], [1.1,2.1,3.3])

# 6.3 Eestimate the mean precipitation on different land use types.
#     landuse = np.random.randint(1, 5, [5, 5])
#     precip  = np.random.random([5, 5])
#     print('landuse\n', landuse)
#     print('precip \n', precip)

import numpy as np
landuse = np.random.randint(1, 5, [5, 5])
precip  = np.random.random([5, 5])
print('landuse\n', landuse)
print('precip \n', precip)

landuse1=np.dstack((landuse ==1, precip))
mean1=np.mean(landuse1)
print('Mean precip for type 1 is', mean1)
landuse2=np.dstack((landuse ==2, precip))
mean2=np.mean(landuse2)
print('Mean precip for type 2 is', mean2)
landuse3=np.dstack((landuse ==3, precip))
mean3=np.mean(landuse3)
print('Mean precip for type 3 is', mean3)
landuse4=np.dstack((landuse ==4, precip))
mean4=np.mean(landuse4)
print('Mean precip for type 4 is', mean4)
landuse5=np.dstack((landuse ==5, precip))
mean5=np.mean(landuse5)
print('Mean precip for type 5 is', mean5)

# for i in range(1,5):
#     landuse[i]=np.dstack((landuse ==i, precip))
#     {mean[i]}=np.mean(landuse[i])
#     print(f'Mean precip for type {[i]}  is {mean[i]}')

# 4. We have two array. The first array is the distribution of irrigated land.
#    The second array is the precipitation.
#       landuse = np.random.randint(0, 1, [6, 6])
#       precip  = np.random.random([6, 6])

#       print('landuse\n', landuse)
#       print('precip \n', precip)
#   A. Create a function to create the buffer zones of varied distances to the irrigated land.

#   B. Calculate the mean precipitation in the buffer zones of different distance to the irrigated land.

#Feel that not enough information is provided for what the buffer zone is supposed to be.
import numpy as np
landuse = np.random.randint(0, 1, [6, 6])
precip  = np.random.random([6, 6])

print('landuse\n', landuse)
print('precip \n', precip)

# 5. Write a Python function to find the nearest point of a list of given points.
#   You are not allowed to use any type of loops.
#   e. g. points = [(3, 4), (1, 2), (7, 8), (9, 4), (6, 5), (8, 7), (4, 7)]

#   Hint: using numpy to create a N x N array which contain the distances between 
#   each ith an jth point pair; where N is the numer of points.

import numpy as np
points=[(3, 4), (1, 2), (7, 8), (9, 4), (6, 5), (8, 7), (4, 7)]
a=np.array(points)
print(a)

print(a[0,:])
#Unable to complete. For some reason I am having a hard time figuring out how to set this up.