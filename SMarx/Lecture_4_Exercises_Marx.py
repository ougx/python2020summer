#4.1-Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note: Use 'continue' statement. 
for number in 0,1,2,3,4,5,6:
    if number == 3:
        continue
    if number == 6:
        continue
    print('Current number:', number)
    
#4.2-Write a Python program to check the validity of password input by users.
#   At Least 1 letter between [a-z] and 1 letter between [A-Z].
#   At least 1 number between [0-9].
#   At least 1 character from [$ # @].
#   Minimum 6 characters.
#   Maximum 16 characters.
Password='Smarx2#'
print('Password:', Password)
def password_validity(Password):
    validity=True
    if not any(char.islower() for char in Password):
        validity=False
    if not any(char.isupper()for char in Password):
        validity=False
    if not any(char in ['$','#','@'] for char in Password):
        validity=False                
    if len(Password)<6:
        validity=False
    if len(Password)>16:
        validity=False
    if validity:
        return validity
if (password_validity(Password)):
    print('Valid Password')
else:
    print('Invalid Password')

#4.3-Write a python program to construct the following pattern, using a nested for loop

#*
#**
#***
#****
#*****
#****-
#***--
#**---
#*----

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=' ')
    print("\r")
for i in range(6, 1, -1):
    for j in range(1, i - 1):
        print("*", end=' ')
    if i>2:
        for k in range(i-1,6):
            print('- ',end='')
    print("\r")

#4.4-There are 10 cars with information stored in four lists.
#Based on these lists,
#   1 Find the brand and model of the safest car
#   2 Find the safest brand of each vehicle type
#   3 Calculate the total accidents for each brand and vehicle type, repectively

Brand=['Ford', 'Ford', 'Chevy', 'Chevy', 'Honda', 'Ford', 'Honda', 'Honda', 'Ford', 'Chevy']
Model=['F150', 'Escape', 'Charger', 'Charger', 'Civic', 'Escape', 'CRV', 'CRV', 'F150', 'Silverado']
Type=['Pickup', 'SUV', 'Sedan', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'Pickup', 'Pickup']
Accidents=[25, 79, 46, 90, 29, 88, 79, 93, 20, 11]
#4.4.1
zipped=zip(Brand, Model, Type, Accidents)
safest=min(zip(Accidents, Brand, Model))
print('Safest brand and model is:', safest)
#4.4.2
Accidents_sort=sorted(zip(Accidents, Brand, Type))
check_val = set()      #Check Flag
res = []
for i in Accidents_sort:
    if i[2] not in check_val:
        res.append(i)
        check_val.add(i[2])
print('Safest brand of each type of vehicle is:', res) 
#4.4.3
brand=sorted(zip(Brand, Accidents))
sum = {}
for item in brand:
    if not item[0] in sum:
          sum[ item[0] ] = 0
    sum[ item[0] ] += item[1]
print('Total accidents per brand is:', sum.items())

veh_type=sorted(zip(Type, Accidents))
sum = {}
for item in veh_type:
    if not item[0] in sum:
          sum[ item[0] ] = 0
    sum[ item[0] ] += item[1]
print('Total accidents per type is:', sum.items())

# Classify daily temperatures (in degrees Celsius) stored in the temperatures list below into four different classes:
# -Cold: Temperatures below -2 degrees
# -Slippery: Temperatures equal to or warmer than -2 degrees and up to +2 degrees
# -Comfortable: Temperatures equal to or warmer than +2 degrees and up to +15 degrees
# -Warm: Temperatures warmer than +15 degrees
#   1 Store the index of day for each of the classes.
#   2 Calculate the mean temperature in each class. 

temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5, -4.6,
5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6, -2.7, -4.6,
3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8, 4.0, 8.6, 4.1, 1.4, 8.9,
3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8,
6.3, 2.6, -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

print('there are', len(temperatures),'days in this list')
days=list(range(1, len(temperatures)+1))
#print(len(days))
daily_temps=sorted(zip(days, temperatures))
#print(daily_temps)

for item in daily_temps:
    if item[1] < -2:
        print(item[0], 'Cold')
    else: 
        if -2<= item[1] <= 2:
            print(item[0], 'Slipery')

        else:
            if 2< item[1] <= 15:
                print(item[0], 'Comfortable')
            else:
                if 15 < item[1]:
                    print(item[0], 'Warm')
                    
cold_days=[i for i in daily_temps if i[1] < -2]
slippery_days=[i for i in daily_temps if -2<= i[1] < 2]
comfortable_days=[i for i in daily_temps if 2< i[1] < 15]
warm_days=[i for i in daily_temps if i[1] >= 15]
print('there are', len(cold_days), 'cold days')
#print('cold days', cold_days)
print('there are', len(slippery_days), 'slippery days')
#print('slippery days', slippery_days)
print('there are', len(comfortable_days), 'comfortable days')
#print('comfrotable days', comfortable_days)
print('there are', len(warm_days), 'warm days')
#print('warm days', warm_days)

avg_cold_temp=sum(i[1] for i in cold_days) / len(cold_days)
print('Average cold temp is:', avg_cold_temp, 'degrees')
avg_slippery_temp=sum(i[1] for i in slippery_days) / len(slippery_days)
print('Average slippery temp is:', avg_slippery_temp, 'degrees')
avg_comfortable_temp=sum(i[1] for i in comfortable_days) / len(comfortable_days)
print('Average comfortable temp is:', avg_comfortable_temp, 'degrees')
if len(warm_days)==0:
    print('There are no warm days in this data set')
else:
    avg_warm_temp=sum(i[1] for i in warm_days) / len(warm_days)
    print('Average warm temp is:', avg_warm_temp, 'degrees')
    
#4.6 Given a string, find the length of the longest substring without repeating characters.
str1='abcdefghijklmnopqrstuvwxyz'
def longestSubstring(str1, str2):
    str1='abcdefghijklmnopqrstuvwxyz'
    longest = ''
    for j in range(0,len(str1)):
        for i in range(len(str1)+1):
            if str1[j:i] in str2 and len(str1[j:i])>len(longest):
                longest = str1[j:i]
    return longest
print(longestSubstring(str1, 'abcabcbbb'))

#4.7 Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets.
def Triplets(array_nums):    
    for i in range(len(array_nums)):
        combo=set()
        for j in range(i+1, len(array_nums)):
            x= -(array_nums[i]+array_nums[j])
            if x in combo:
                print(x, array_nums[i], array_nums[j])
            else:
                combo.add(array_nums[j])        
print(Triplets([-1,0,1,2,-1,-4]))