# importing of some useful libraries that wil be used throughout the code.

import csv
import sys
import os
from functions import load_csv, insertion, deletion, sort, search


# Because the testing program can only be run when the developer provides into the command line two arguments, csv file and testing.py file, this should lead to restricted use of this check file (i.e. only the developer). To start the tesing, the program here starts to check if there are two command line arguments. If so, then it continues to proof whether the csv file is in the current directory. If so, it loads it with load_csv from functions.py. After that, it begins with the list of checkpoints. 

if len(sys.argv) == 2:
    file = sys.argv[1]
    if os.path.exists('./' + file + '.csv'):
        tmp = load_csv(file,2,6)

    # check 1 - no duplicates
    # Because a set doesn't insert duplicates, the length of a set which includes all the kays should be the same as the length of the dictionary itself.
  
    set1 = set()
    for k,v in tmp.items():
        set1.add(k)
    if len(set1) == len(tmp):
        print("check 1: OK")
    else: 
        print("check 1: False")

    # check 2 - insertion and sorting

    dic1 = insertion(file,tmp,('aaaaaa','aaaaaa'),['aaaaaa','aaaaaa','aaaaaa','aaaaaa','aaaaaa',0])
    if search(dic1,'aaaaaa') == ['aaaaaa','aaaaaa','aaaaaa','aaaaaa','aaaaaa',0]:
        print("check 2: OK")
    else:
        print("check 2: False")

    # check 3 - deletion            

    dic1 = deletion(file, dic1, ('aaaaaa','aaaaaa'))
    if dic1 == tmp:
        print("check 3: OK")
    else:
        print("check 3: False")

    # check 4 - insertion and sorting

    dic1 = insertion(file,dic1,('aaaaaa','aaaaaa'),['aaaaaa','aaaaaa','aaaaaa','aaaaaa','aaaaaa',float(0.0)])
    for k,v in dic1.items():
        v[-1] = float(v[-1])
    if sort(dic1,1,5,False)[0][1][5] == 0.0:
        print("check 4: OK")
    else: 
        print("check 4: False")

    # check 5 - search

    if search(dic1,'aaaaaa') == ['aaaaaa','aaaaaa','aaaaaa','aaaaaa','aaaaaa',float(0.0)]:
        print("check 5: OK")
    else:
        print("check 5: False")

    # check 6 - error message

    if search(dic1,'aaaaab') == 'No Key found':
        print('check 6: OK')
    else:
        print('check 6: False')

    # bring the dictionary back to its initial state
      
    dic1 = deletion(file, dic1, ('aaaaaa','aaaaaa'))