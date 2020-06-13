# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:58:40 2020

@author: mmaguire2
"""
# ex 4.1
for n in range(7):
    if n == 3:
        continue
    if n == 6:
        continue
    print(n)
    
# ex 4.2
def check_password(password):
    symbols = ['$','#','@']
    if any(c for c in password if c.islower()):
        if any(c for c in password if c.isupper()):
            if any(c for c in password if c.isdigit()):
                if 1 in [c in password for c in symbols]:
                    if len(password) > 5:
                        if len(password) < 17:
                            return("Password is good")
                        else: 
                            return("Password does not meet requirements")
                    else: 
                        return("Password does not meet requirements")
                else: 
                    return("Password does not meet requirements")
            else: 
                return("Password does not meet requirements")
        else: 
            return("Password does not meet requirements")
    else: 
        return("Password does not meet requirements")
        
        
# ex 4.3
for n in range(1):
    print('*')
    for a in range (1):
        print('**')  
        for b in range(1):
            print('***')
            for b in range(1):
                print('****')
                for b in range(1):
                    print('*****')
                    for b in range(1):
                        print('****-')
                        for b in range(1):
                            print('***--')
                            for b in range(1):
                                print('**---')
                                for b in range(1):
                                    print('*----')
            



# ex 4.4
Brand = ['Ford', 'Ford',   'Chevy',   'Chevy',   'Honda', 'Ford',   'Honda', 'Honda', 'Ford', 'Chevy']
Model = ['F150', 'Escape', 'Charger', 'Charger', 'Civic', 'Escape', 'CRV',   'CRV',   'F150', 'Silverado']
Type = ['Pickup', 'SUV', 'Sedan', 'Sedan', 'Sedan', 'SUV', 'SUV',   'SUV',   'Pickup', 'Pickup']
Accidents = [25, 79, 46, 90, 29, 88, 79, 93, 20, 11]

# brand and model of the safest car
index = Accidents.index(min(Accidents))
print("The brand and model of the safest car is a", Brand[index], Model[index])

# safest brand for each vehicle type
pickup=[]
p_acc=[]
suv=[]
suv_acc=[]
sedan=[]
sedan_acc=[]

for a, b, c in zip(Brand, Type, Accidents):
    if b == 'Pickup':
        pickup.append(a)
        p_acc.append(c)   
        index_pickup= p_acc.index(min(p_acc))
    if b == 'SUV':
        suv.append(a)
        suv_acc.append(c)   
        index_SUV= suv_acc.index(min(suv_acc))
    if b == 'Sedan':
        sedan.append(a)
        sedan_acc.append(c)   
        index_Sedan= sedan_acc.index(min(sedan_acc))
        
print("The safesst brand for a Pickup is ", pickup[index_pickup])
print("The safesst brand for an SUV is ", suv[index_SUV])
print("The safesst brand for a Sedan is ", sedan[index_Sedan])

# total accidents for each brand and vehicle type
accident_brand = {b:0 for b in set(Brand)} 
accident_type =  {t:0 for t in set(Type)} 
for b, t, a in zip(Brand, Type, Accidents):
    accident_brand[b] += a
    accident_type[t] += a
print(accident_brand)
print(accident_type)

# ex 4.5
import statistics
temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5, -4.6,5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6, -2.7, -4.6,3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8, 4.0, 8.6, 4.1, 1.4, 8.9,3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8,6.3, 2.6, -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

cold=[]
slippery=[]
comfortable=[]
warm=[]
cold_days=[]
slippery_days=[]
comfortable_days=[]
warm_days=[]
day=1

for temp in temperatures:
    if temp < -2:
        cold.append(temp)
        cold_days.append(day)
        day += 1
    if (temp >= -2 and temp < 2):
        slippery.append(temp)
        slippery_days.append(day)
        day += 1
    if (temp >= 2 and temp < 15):
        comfortable.append(temp)
        comfortable_days.append(day)
        day += 1
    if temp >= 15:
        warm.append(temp)
        warm_days.append(day)
        day += 1        
print(cold_days)
print(slippery_days)
print(comfortable_days)
print(warm_days)

if not cold:
    print('no cold days')
else: 
    print('cold day average temp', statistics.mean(cold))

if not slippery:
    print('no slippery days')
else: 
   print('slippery day average temp', statistics.mean(slippery))

if not comfortable:
    print('no comfortable days')
else: 
  print('comfortable day average temp', statistics.mean(comfortable))

if not warm:
    print('no warm days')
else: 
  print('warm day average temp', statistics.mean(warm))


# ex 4.6 
def UniqueSubsttr(string):  # string - is a string of various characters
    seen = {} 
    maximum_length = 0
    start = 0    
    for end in range(len(string)): 
        if string[end] in seen: 
            start = max(start, seen[string[end]] + 1) 
        seen[string[end]] = end 
        maximum_length = max(maximum_length, end-start + 1) 
    return print("The length of the longest non-repeating character substring is", maximum_length) 
   

# ex 4.7
def findTriplets(numbers): # numbers - is a list of numbers
    num_length = len(numbers)
    found = False
    for i in range(num_length - 1): 
  
        # Find all pairs with sum  
        # equals to "-numbers[i]"  
        s = set() 
        for j in range(i + 1, num_length): 
            x = -(numbers[i] + numbers[j]) 
            if x in s: 
                print(x, numbers[i], numbers[j]) 
                found = True
            else: 
                s.add(numbers[j]) 
    if found == False: 
        print("No Triplet Found") 
  
numbers = [0, -1, 2, -3, 1, 2 ,-4, -1, 2, 3, 1, 0, -2]  
findTriplets(numbers)
