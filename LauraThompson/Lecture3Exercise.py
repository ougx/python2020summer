# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:07:54 2020

@author: lthompson8
"""


#%%Question 1: Write a Python function that takes a list of words and returns the length of the longest one
fruitlist=["apple", "orange", "strawberry", "bananas"]

def find_longest_word(fruitlist):
    longest_word = ' '
    for word in fruitlist:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)

find_longest_word(fruitlist)

#%%Question 2: Write a Python program to count the number of unique characters in a string
myname = "My name is Laura Thompson"
#now count it.
#first counting with both upper and lower case a unique
allcount=len(set(myname))
print("The number of characters with upper and lower unique is:", allcount)
#set to all lower case so that letters of upper and lower aren't unique.
lowercount=len(set(myname.lower()))
print("The number of characters without case sensitivity is:", lowercount)

#%%Question 3: Wrtie a Python program to sort (ascending and descending) a dictionary by value

dict1 = {"first": "Laura", "middleinitial": "J", "last": "Thompson"}
#print(dict1)
#print(dict1.keys())
#print(dict1.values())
dict1["birthstate"]="Nebraska"
#print(dict1)

#now sort it.
sorted_ascending_dict1 = sorted(dict1)
print(sorted_ascending_dict1)

sorted_descending_dict1 = sorted(dict1, reverse=True)
print(sorted_descending_dict1)

#%%Question 4: Write a Python program to change a given string to a new string where the first and last chars have been exchanged
dogstory = "The little dog jumped over the large, tall fence"

#now switch it.
dogstory[1:-1]
reversedogstory=dogstory[-1:]+dogstory[1:-1]+dogstory[:1]
print(reversedogstory)
#%%Question 5: Write a Python function that takes two lists and returns True if they havea least one common member

cropslist = ["corn", "soybean", "wheat", "sorghum"]
grocerylist = ["milk", "apples", "flour", "corn"]

def common_elements(cropslist, grocerylist):
    result = []
    for element in cropslist:
        if element in grocerylist:
            result.append(element)
    return result

print(common_elements(cropslist, grocerylist))

#%%Question 6: Write a Python function that returns the minimum number of coins ($0.01, $0.1, $0.25, $1) that make a given value.
#from math import remainder
#from decimal import decimal
# more complicated...first needs to divide by 1, then 0.25, then 0.1, then 0.01... or something like that...
#print(Decimal('3.5')%Decimal('0.1'))
#print(4.5%1)
#print(remainder(4.5,1))
#CurrencyValue=7.75
#CurrencyValue/1
#rem=rem%1;

#greedy method example with options of $.25, $.10, $.05, and $0.01.
#def num_coins(cents):
 #   coins = [25,10,5,1]
  #  count = 0
   # for coin in coins:
    #    while cents >= coin:
     #       cents = cents - coin
      #      count = count + 1
            
#    return count
#print(num_coins(10))


#greedy method
#but we did not have $0.05 as an option, and also have whole dollar options. So adding 100, and removing 5.
def num_coins(cents):
    cents = cents*100
    coins = [100,25,10,1]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1
            
    return count
#for this function, value must be input in cents, not dollars. So $1.75, needs to be input as 175.
#trying to figure out how to take input *100 prior to running function...
print(num_coins(5.27))

