# importing of some useful libraries that wil be used throughout the code.

import sys
import csv
import re
import os
import string
import random

    # As mentioned in the README file, there is a special input that the developer can use to build artifical testdata. The for loop uses a randomly chosen range from 0 to [5,10,50,100] (Note: random.choice takes a list as argument an picks up one value randomly). 
    # Within the loop, the dataset will be created once more in randomly choosing always two letters of the alphabet/two string-numbers for each part of the key and each part of the value section, concatenates these and adds it to a temporary list called list1.

for i in range(0,random.choice([5,10,50,100])):
    list1 = []

    # Note: The join function can be used for concatenation of two characters.    

    key1 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(key1)
    key2 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(key2)
    value1 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(value1)
    value2 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(value2)
    value3 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(value3)
    value4 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(value4)
    value5 = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(value5)
     
   # As seen before, for the rating value the program has first to convert it to a floating point number. Second, an ouput between [0.5,5.0] is expected (Interval of 0.5).
    
    value6 = float(random.choice([x * 0.5 for x in range(1,11)]))
    list1.append(value6)
            
    # For exporting the data, the loop still has to pay attention to start in writing the file. If so, then the "w" modus will be called. Otherwise, the append modus has to be chosen ("a").

    if i == 0:
        with open(sys.argv[1] + '.csv', 'wb',) as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list1)
    else:
        with open(sys.argv[1] + '.csv', 'ab',) as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list1)