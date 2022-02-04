# importing of some useful libraries that wil be used throughout the code.

from cs50 import get_string, get_float
import csv
import sys
import re
import os
import string
import random

# PART 1: FUNCTIONS

# 1. load_csv 
# This is a function that takes an existing (csv) file, reads every line in this file and saves it first in a list where every element in the list is a line saved as a single list of values (this is what csv.reader does)

def load_csv(filename, length_key, length_value):
    dic1 = {}
    list1 = []
    with open(filename + '.csv', newline='') as f:
        c = csv.reader(f, skipinitialspace=True, delimiter=',')

        # To transform this in a python dictionary where every key is an (immutable) tuple of (name,alcoholic_level) and every value is a list of values/words, load_csv then puts all the elements of the csv.reader object in only one list (list1)

        for i in c:
            for j in range(length_key+length_value):
                list1.append(i[j])

    # After this, the function uses a nested for loop to make the split between the start of a new line and additionally to split the key from the value section. Finally, the dictionary will be returned.
    # The tuple structure guarantees that there aren't any duplicates as a key in the dictionary.

    for j in range(int(len(list1)/(length_key + length_value))):  
        tuple1 = tuple([list1[0 + (j * (length_key + length_value))].strip().lower()])
        for i in range(1,length_key):
            tuple1 = tuple1 + tuple([list1[i + (j * (length_key + length_value))]])
        list2 = [list1[length_key + (j * (length_key + length_value))]] 
        for i in range(length_key+1,length_key+length_value):
            list2 = list2 + [list1[i + (j * (length_key + length_value))]]
        dic1[tuple1] = list2
    return dic1 

# 2. insertion
# insertion takes a file, a dictionary, a userinput (already splitted in key and value section) and uses the existing file to open it and to use the append modus (i.e. expand the file). The writer option of the csv library creates an writer object.
# Therefore, it allows for inserting of new rows or columns in a file. Finally, the writerow option then actually does the writing process where it uses an iterator object (here a list) that will be transmitted in calling the function writer.writerow. 

def insertion(filename, dictionary, key, value):
    
    dictionary[key] = value

    # list1 is a temporary list that will be used for bringing keys and values in the right order so that it can be written accurately into the csv file (key1 first, then key2, value1, value2, etc.).

    list1 = []
    for k in range(len(key)):
        list1.append(key[k])
    for v in range(len(value)):
        list1.append(value[v])
    with open(filename + '.csv', 'a', newline='') as output:
        writer = csv.writer(output, delimiter = ',')
        writer.writerow(list1)
    return dictionary
    
# 3. deletion 
# deletion takes a CSV file, a dictionary and a userinput (a key only) as input. The function then loops over all keys and values in the dictionary and checks if the tuple is in the dictionary. If so, the particular item will be added (to a temporary list called "list1").
# After this step, the function checks, if there is an item in this temporary list. If so, then it deletes this item from the dictionary and then rewrites all rows in the existing CSV file (without the poped key).
# Though, while wiriting the new dictionary into the csv file, the application has to distinguish between the first line and following ones. Whereas the first line uses the "w" (write) option, the next lines require the "a" (append) modus. This step will be ensured in using a counter variable.Only in the case of the first insertion, the writing modus is called (counter == 0), all other insertions will be done by the append modus (counter != 0).
# At the end, an output will be presented to the user whether the key has been found or not.

def deletion(filename,dictionary,tuple):

    list1 = []
    for k,v in dictionary.items():
        if k == tuple:
            list1.append(k)
    for i in list1:
        if list1 != []:
            dictionary.pop(i)
            print('Key successfully deleted')
            counter = 0
            for k,v in dictionary.items():

                # list2 is similar to list1 in the insertion function. Thus, it is also a temporary list for ordering keys and values so that it is written correctly afterwards into the the csv file.

                list2 = []
                for key in k:
                    list2.append(key)
                for value in v:
                    list2.append(value)
                if counter == 0:
                    with open(filename + '.csv', 'w', newline='') as output:
                        writer = csv.writer(output, delimiter=",")
                        writer.writerow(list2)
                else:
                    with open(filename + '.csv', 'a', newline='') as output:
                        writer = csv.writer(output, delimiter=",")
                        writer.writerow(list2)
                counter += 1
    if list1 == []:
        print("Key not found")
    return dictionary

# 4. search 
# search also takes a dictionary and a userinput (a beer name) as arguments and then simply checks for every key and value in the dictionary if there is one key that is equal to given tuple. If so, the value of this key will be displayed. Otherwise an error message appears.

def search(dictionary, key):
   
    for k,v in dictionary.items():
        k = k[0].strip()
        k = k.lower()        
        if key == k:
            return v
    return "No Key found"

# 5. sort
# An interesting part is when the user wants to sort for items. The function takes a dictionary, a boolean value (to differ key (0) from value (1)), an item number (i.e. which index in the key/values should be chosen) and an order (also boolean, asc = False,  desc = True) as inputs. Depending on the input, the programs checks for the different scenarios. 
# For every sorting procedure, it uses the sorted function from python which uses the timsort algorithm which is a combination of binary insertion sort and merge sort and therefore decides depending on the size of the dictionary which algorithm to choose. (Python Software Foundation, 09/21)
# To understand the sorted function, it takes an iterable object (dict.items() allows iteration over an dictionary), sorts it by the item that one wants to choose in reverse or non reverse order. 
# The argument "key=lambda" simply means that this process should be done in using a lambda function which simply stands for a non specific function name (no declaration at this point). Despite the lambda function, the sorted dic will be saved in an object called "sortdic". 
def sort(dictionary,boolean_keyORvalue, item_number, order=True):

    sortdic={k: v for k, v in sorted(dictionary.items(), key=lambda item: item[boolean_keyORvalue][item_number], reverse = order)}
    return sortdic