# importing of some useful libraries that wil be used throughout the code.

import csv
import sys
import re
import os
import string
import random
from functions import load_csv, insertion, deletion, sort, search


# PART 2: MAIN 

# this file runs the main program.
# First, display a welcome message and use a blank line before to emphasize the text.

print('\n')
print('Hello, this is your Belgian Beer Guidebook.\n')

# the program starts in asking the user to mention a file name (that can be an existing one or a name for a new one).
file = raw_input("Please make sure that your file is in your current directory. Please enter the file name that you want to use (without '.csv'): ")

# Check if the file is already in the current directory. If there is an existing csv file, then it opens the file with load_csv and saves it in an object called tmp (temporary dictionary).

if os.path.exists('./' + file + '.csv'):
    tmp = load_csv(file,2,6)

# Otherwise, start with an empty dictionary.

else:
    tmp = {}

# quit is a boolean variable that will be used to quit the program. As long as quit is not true, the program runs (here it is never going to be True so that it runs infinitely).

quit = False
while quit == False:

    # Check, if the file already exists. If so, the program always displays the dictionary to the user as a starting message and the user can choose between insert, delete, sort and search. If not, no guidebook will be shown and the user can only insert something in the guidebook.

    if os.path.exists('./' + file + '.csv'):
        display = raw_input("\nDo you want to see the current guidebook?  yes or no? ").strip().lower()
        if display == 'yes':
            print('\nHere is your current Guidebook.\n')
            print(tmp)
            print('\n')
        
        answer = raw_input("\nWhat do you want to do? Please select between insert, delete, sort or search ?").strip().lower()
    else:
        answer = 'insert'

    # Now, the program goes into a conditional jump, where it tests which input has been given, "insert", "delete", "search" or "sort".
    # The conditional jump starts checking if the provided user input is "insert". If so, the program continues to interact with the user in asking several information (beer name, alcoholic level, features, region, city and final rating). It does this repeatedly until a stopping criteria is reached (therefore the inserter boolean and the while loop).
    # After that, the insertion function will be called whereas the tuple consists of the tuple (beer name, alcoholic level) and the list section of a list of values. Finally, the user will be asked if wants to keep going in inserting new rows. If so, then the while loop doesn' t stop, otherwise it will break.

    if answer == "insert":
    
        inserter = True
        while inserter == True:
            beer_name = raw_input("Beer name? ").strip().lower()
            alcohol_level = raw_input("Alcohol level? ").strip().lower() 
            feature1 = raw_input("Feature 1? ").strip().lower()
            feature2 = raw_input("Feature 2? ").strip().lower()
            feature3 = raw_input("Feature 3? ").strip().lower()
            region = raw_input("Which region? ").strip().lower()
            city = raw_input("Which city? ").strip().lower()
            score = raw_input("Your score (0.5 lowest, 5.0 highest?) ")
            list1 = [feature1,feature2,feature3,region,city,score]
            tuple1 = (beer_name,alcohol_level)
            tmp = insertion(file, tmp, tuple1, list1)        
            more = raw_input("Do you still want to insert? yes or no?")
            if more.lower() == "no" or more.lower() != "yes":
                break
    
    # the second if-clause checks whether the the answer provided by the user was "delete". If so, only beer name and alcoholic level will be asked and the deletion will be called directly afterwards.

    elif answer == "delete":
        
        beer_name = raw_input("Beer name? ").strip().lower()
        alcohol_level = raw_input("Alcohol level? ").strip().lower()
        print('\n')
        length_before = len(tmp)
        tmp = deletion(file,tmp,(beer_name,alcohol_level))
        if length_before == len(tmp):
            print("Key not found\n")
        else:
            print("Key successfully deleted\n") 
    
    # third check of the conditional jump checks for the userinput of "sort". If it is correct, then it still asks for two auestions, 1) which category, name, region, city or rating? and 2) ascending or descending?

    elif answer == "sort":
           
        category = raw_input("By name, region, city or rating? ").strip().lower()
        order = raw_input("Asc or desc? ").strip().lower()
        print('\n')

        # The program still has to convert the rating variable into a floating point number (up to now it is still a string).

        for k,v in tmp.items():
            v[-1] = float(v[-1])

        # The program is still in the sort-clause. Here, the program differentiates between the different inputs that the user can provide (category, order). Depending on this, the sort function will be called differentely. 

        if category == "name":
            if order == "desc":
                print(sort(tmp,0,0,True))
            else:
                print(sort(tmp,0,0,False))
        if category == "region":
            if order == "desc":
                print(sort(tmp,-1,3, True))
            else:
                print(sort(tmp,-1,3, False))
        if category == "city":
            if order == "desc":
                print(sort(tmp,-1,4, True))
            else:
                print(sort(tmp,-1,4, False))
        if category == "rating":
            if order == "desc":
                print(sort(tmp,-1,5, True))
            else:
                print(sort(tmp,-1,5, False))

    # Last check, if the answer given by the user was "search", once again beer name and alcohol level will be asked, followed by calling the search function.        

    elif answer == "search":
               
        beer_name = raw_input("Enter your beer name: ").strip().lower()
        output = search(tmp,beer_name)
        print('\n')
        print(output)
   
    # In all other cases, the user did a mistake. Hence, the program returns a short feedback and it lets try him again.

    else:
        print("\nThis wasn't one of the options. Please type in 'insert', 'delete', 'sort' or 'search' and try again.")



