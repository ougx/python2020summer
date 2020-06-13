# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:57:51 2020

@author: lthompson8
"""

#%%
#Exercise 4.1: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Use if, loop, and continue statements
#expected output: 0 1 2 4 5

for i in range(6):
    if i == 3:
        continue
    elif i >= 6:
        break
    print(i)


#%% class example option for 4.1:
for i in range(7):
    if i in [3,6]: continue
    print(i)

#can put both 3 and 6 in.
    
#%%
#Exercise 4.2: Write a Python program to check the validity of password input by users.
    #At least 1 letter between [a-z].
    #At least 1 letter between [A-Z].
    #At least 1 character from [$ # @].
    #Minimum length 6 characters.
    #Maximum length 16 characters.

def checkpassword(password):
    if (len(password)) > 5 and (len(password)) < 17 and (any(c.islower() for c in password)) and (any(c.isupper() for c in password)) and ("#" in password or "$" in password or "@" in password):
        print('Congratulations, password is valid!')
    elif(len(password)) < 6:
        print('Password is too short. Make sure password is at least 6 characters.')
    elif(len(password)) > 16:
        print('Password too long. Make sure password is no more than 16 characters.')
    elif "#" not in password and "$" not in password and "@" not in password:
        print('Make sure password contains one of the following special characters: # $ @')
    else:
        print('Please make sure you have at least one upper and lower case letter.')


password='herpnDerpy27yay#'
checkpassword(password)

#%%class example answer:
def check_password(password):
    number_req = False
    special_req = False
    lower = False
    upper = False
    for c in set(password):
        if c >= 'a' and c <= 'z': lower = True
        if c >= 'A' and c <= 'Z': upper = True
        if c >= '0' and c <= '9'
        ....
        
#%%
#Exercise 4.3: Write a Python program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
# *****
# ****-
# ***--
# **---
# *----

for i in range(1, 10):
    nstar = i if i <=5 else 10 - i
    ndash = i-5 if i > 5 else 0
    
    for j in range(nstar):
        print('*', end='')
    for j in range(ndash):
        print('-', end='')
    print('')

#%%
#Exercise 4.4: There are ten cars and their information are stored in four lists:
#Find the brand and model of the safest car

Brand = ["Ford", "Ford", "Chevy", "Chevy", "Honda", "Ford", "Honda", "Honda", "Ford", "Chevy"]
Model = ["F150", "Escape", "Charger", "Charger", "Civic", "Escape", "CRV", "CRV", "F150", "Silverado"]
Type = ["Pickup", "SUV", "Sedan", "Sedan", "Sedan", "SUV", "SUV", "SUV", "Pickup", "Pickup"]
Accidents_each_year = [25, 79, 46, 90, 29, 88, 79, 93, 20,11]

#Find the brand and model of the safest car
least_accidents = Accidents_each_year.index(min(Accidents_each_year))
print(Brand[least_accidents], Model[least_accidents], "is the safest with", min(Accidents_each_year), "accidents per year")

#Find the safest brand for each vehicle type
naccident_cartype = {t:{} for t in set(Type)}

for b, t, n in zip(Brand, Type, Accidents_each_year):
    if b in naccident_cartype[t]:
        naccident_cartype[t][b] += n
    else:
        naccident_cartype[t][b] = n

for t in naccident_cartype:
    min_accident = 10000
    for b in naccident_cartype[t]:
        if naccident_cartype[t][b] < min_accident:
            min_accident = naccident_cartype[t][b]
            brand_safest = b
    naccident_cartype[t] = b
    
for t in naccident_cartype:
    print(t + "'s safest brand is " + naccident_cartype[t])

#Calculate the total accidents for each brand and vehicle type, respectively.
naccident_brand = {b:0 for b in set(Brand)}
naccident_type = {t:0 for t in set (Type)}
for b, t, n in zip(Brand, Type, Accidents_each_year):
    naccident_brand[b] += n
    naccident_type[t] += n
print(naccident_brand)
print(naccident_type)
 
# naccident_brand[b] += n   this adds the accidents and assigns into naccident

#%%
#Exercise 4.5: Classify daily temperatures (in degrees Celsius) stored in the temperatures list below into four different classes:
#Cold: Temperature below -2 degrees
#Sippery: Temperature equal to or warmer than -2 degrees and up to +2 degrees
#Comfortable: Temperatures equal to or warmer than +2 degrees and up to +15 degrees
#Warm: Temperatures warmer than +15 degrees

#Store the index of day for each of the classes.
#Calculate the mean temperature in each class.

temperature = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5, -4.6,5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6, -2.7, -4.6,3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8, 4.0, 8.6, 4.1, 1.4, 8.9,3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8,6.3, 2.6, -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]
for i in temperature:
    if i < -2:
        print('Cold')
    elif i < 2:
        print('Slippery')
    elif i < 15:
        print('Cormfortable')
    else:
        print('Warm')
print(temperature)
#this is a simple solution but does not help with mean question next.

#%%
#Calculate the mean temperature in each class.
# so to calculate, would be better to index each and add list, then can look for different weathers.
#modifying above code to create dictionary
temperature = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5, -4.6,5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6, -2.7, -4.6,3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8, 4.0, 8.6, 4.1, 1.4, 8.9,3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8,6.3, 2.6, -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

weather = dict(cold=[], slippery=[], comfortable=[], warm=[])
for i, t in enumerate(temperature):
    if t < -2:
        weather['cold'].append(i)
    elif t < 2:
        weather['slippery'].append(i)
    elif t < 15:
        weather['comfortable'].append(i)
    else:
        weather['warm'].append(i)
#store the index of day for each of the classes
print(weather)

#The enumerate() function assigns an index to each item in an iterable object 
#that can be used to reference the item later.

t_mean = {}
for c in weather:
    t_sum = []
    for i in weather[c]:
        t_sum.append(temperature[i])
    t_mean[c] = 'na' if t_sum == [] else sum(t_sum)/len(t_sum)
print(t_mean)


#%% 
#Exercise 4.6: Given a string, find the length of the longest substsring without repeating characters.

def longestUniqueSubsttr(string): 
       
    # Creating a set to store the last positions of occurrence 
    seen = {} 
    maximum_length = 0
   
    # starting the inital point of window to index 0 
    start = 0 
       
    for stop in range(len(string)): 
   
        # Checking if we have already seen the element or not 
        if string[stop] in seen: 
  
            # If we have seen the number, move the start pointer to position after the last occurrence 
            start = max(start, seen[string[stop]] + 1) 
   
        # Updating the last seen value of the character 
        seen[string[stop]] = stop
        maximum_length = max(maximum_length, stop-start + 1) 
    return maximum_length 
   
string = "cookiesareforpeople"
length = longestUniqueSubsttr(string) 
print("The length of the longest non-repeating character substring is", length)

#%%
#Exercise 4.7: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c =0? Find all unique triplets in the array which gives the sum of zero.
#The solution set must not contain duplicate triplets.

#solution would have to have a positive and negative number, so first split the list.
def find_zerosum(num_list):
    positives = list(filter(lambda x: x > 0, num_list))
    negatives = list(filter(lambda x: x < 0, num_list))
 
    zero_in = 0 in num_list
    positives.sort(reverse=True)
    negatives.sort()

    triplets = []

    #A lambda function is a small anonymous function.
    #A lambda function can take any number of arguments, but can only have one expression.


    #first find v, -v, 0 if there is 0 in the list.
    #This means, if there is a zero in the triplet, then the other 2 numbers need to be the same, but one positive and one negative.
    if zero_in:
        for v in set(negatives):
            if -v in set(positives):
                triplets.append([v, 0, -v])
    
            #now, if there isn't a 0 in the triplet, there would need to be 2 values who sum to the same value as the third, but they need to be negative and it positive or vice-versa
            #v1, v2, v3: v2+ v3 = -v1
    for v1 in set(negatives):
        for i, v2 in enumerate(positives):
            if -v1 -v2 in positives[i+1:]:
                if [v1, v2, - v1 -v2] not in triplets:
                    triplets.append([v1, v2, - v1 - v2])

    for v1 in set(positives):
        for i, v2 in enumerate(negatives):
            if - v1 -v2 in negatives[i+1:]:
                if [v1, v2, -v1 -v2] not in triplets:
                    triplets.append([v1, v2, -v1 -v2])

    return triplets

print(find_zerosum([-1, 0, 1, 2, -1, -4]))
print(find_zerosum([5, 3, 2, -1, 0, 0, 5, 7, 9, 10, 10, -11, -10, 100, 60, 50, -50]))

