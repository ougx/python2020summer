#3.1 Write a Python function that takes a list of words and returns the length of the longest one.
words=['hello', 'plus', 'one','equals','one']
print('lenghth of the longest word is', max(len(w)for w in words), 'letters')

#3.2 Write a Python program to count the number of unique characters in a string.
string='sameletters'
print(string)
print('unique characters:', set(string))
print('number of unique characters is', len(set(string)))

#3.3 Write a Python program to sort (ascending and descending) a dictionary by value.
aliens= {'Green': 5, 'Blue': 7, 'Yellow': 12,'Orange': 15}
print('Dictionary values', aliens)
asc=list(aliens.items())
asc.sort()
print('Ascending order is', asc)

dsc=list(aliens.items())
dsc.sort(reverse=True)
print('descending order is', dsc)

#3.4 Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
string='Fred'
newString=(string[1:len(string)-1])
print(string[len(string)-1]+newString+string[0])

#3.5 Write a Python function that takes two lists and returns True if they have at least one common member.
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                    result=True
                    return result
a=[1,2,3]
b=[3,4,5]
print(common_data(a,b))

#3.6 Write a Python function that return the minimum number of coins ($0.01, $0.1, $0.25, $1) that make a given value.
Amount=1.22
Value=Amount
Value=int(round(Value*100))
Dollars=0
Quarters=0
Dimes=0
Pennies=0

Dollars=Value/100
Value = Value % 100  #calculates the remainder of the value
Quarters=Value/25
Value=Value % 25
Dimes=Value/10
Value=Value % 10
Pennies=Value
#print(int(Dollars), int(Quarters), int(Dimes), int(Pennies))
min_coins=(int(Dollars), int(Quarters), int(Dimes), int(Pennies))
print('Minimum number of coins to change', Amount, ' is:', sum(min_coins))