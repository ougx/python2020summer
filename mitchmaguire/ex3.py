# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:51:11 2020

@author: mmaguire2
"""

# takes a list of words and returns the length of the longest one.
def get_longest_word(word_list):
    max_len = 0
    for word in word_list:
        if len(word) > max_len:
            max_len = len(word)
            result = word        
    return max_len, result

# counts number of different characters in a string.
def count_char(string):
    return len(set(list(string)))

# sorts a dictionary by ascending value.
def sort_dict_value_ascending(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=False)
  

# sorts a dictionary by decending value.
def sort_dict_value_decending(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    

# changes a given string to a new string where the first and last chars have been exchanged.
def swap_first_and_last_string(string):
    new_string = string[-1] + string[1:-1] + string[0]
    return new_string





# returns True if two list have at least one common member.
def common_item(list1, list2):
    result = False
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                result = True
                break
    return result
common_item([2, 3, 4], [7, 2, 9])


# returns the minimum number of coins (penny, dime, quater, dollar) that make a given value.
def coin_change(val):
    val = val *100
    dollars = int(val // 100)
    remainder = val-dollars*100
    quarters = int(remainder // 25)
    remainder = remainder-quarters*25
    dimes = int(remainder//10)
    remainder = remainder-dimes*10
    pennies = int(remainder // 1)
    return dollars, quarters, dimes, pennies
    













