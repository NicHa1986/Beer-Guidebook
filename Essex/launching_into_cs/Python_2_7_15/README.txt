# Beer Guidebook

This piece of work takes the opportunity to set up an application that covers the idea of a personal beer guidebook. The guidebook can be run in typing into a python command line "python guidebook.py". The application itself is divided into two python files, functions.py and guidebook.py. 

The **functions.py** contains all the main actions that the application can take. These are:

* load_csv: Handles the mapping of the data from the CSV file to a python dictionary where the key of the dictionary is a tuple of size "length_key" and the value section is a list of values of size "length_value".

* insertion: Is a function that takes a userinput, inserts this as a new key and a new value in a dictionary and then writes this new entry as a new row into CSV file (in append modus, no cancellation of the old entries).  

* deletion: It is a bit different compared to insertion because it still takes a csv file, a tuple and a dictionary and it searches for the tuple as a key in the dictionary. If there is a key that is equal to the tuple, then it removes this key from the dictionary and prints "Key successfully deleted". Though, the important change is that the csv file will be completely overwritten by the adapted (new) dictionary (no append modus). If they Key wasn't found at all, then an error message appears ("Key not found"). Finally, the new dictionary will be returned.

* search: Is very simple because it only takes two arguments, a dictionary and a beer_name and then checks if the name is a part of a key in the dictionary. If it is, it prints out the value section of all keys that are found, otherwise it prints ("No Key found").

* sort: It takes four arguments: a dictionary, a boolean to differ between sorting by key or value, an item number for within key and within value sorting and an order category to sort in ascending or descendig modus. Hence, this can lead to different sorting requirements. For sorting itself, it uses the python sorted function which can iterate over a dictionary and can sort it in different ways based on the timsort algorithm.

The **guidebook.py** file depicts the main program and therefore includes the user. 

The main idea is that the program should run infinitely and it therefore constantly listens to the user whether he wants to create or work with an existing guidebook (a CSV file). After the user has provided a name for his guidebook, the selection of one action begins. Here, the user will be asked what he wants to do, insert, delete, search or sort? (Note: If he creates a new notebook, the user automatically goes into insert because there are no existing entries) After selecting one of the four actions, the program always asks the user to provide more information. These are for:

* insert: beer name, alcoholic level, feature 1, feature 2, feature 3, city, region, rating score.
 
* delete: beer name, alcoholic level

* search: beer name (No alcoholic level because it should allow the user to be less precise, i.e. perhaps more than one value section. On the other side, deletion needs to be precise because it has direct consequences).

* sort: category (beer name, region, city, rating), order (ascending, descending)

Getting the information of one action, the program then calls the equivalent function above and displays in some cases an output. Because the program runs continuously, the program starts again from the beginning after this last step.

Beside functions.py and guidebook.py, the program also includes a file called **testing.py** which simply tests an existing csv file with respect to 6 dimensions ((1) Test for immutability of key, (2) - (5) test for correct use of inserting, deletion, searching, sorting, (6) test for spelling errors). This application test can be run in typing into the command line 'python testing.py filename' where filename is only the name of the csv file (without the ending of '.csv') and then presents an output for every test.

Finally, the zip package also includes 3 testdata csv files which include some duplicates and whitespace errors. Furthermore, testdata2.csv is an artificially generated data set which has been evaluated by running the **datacreation.py** file (python code 'python datacreation.py'). This python file allows for randomly generated csv files of different size (5,10,50 or 100 rows) which have the same format as the guidebook. 

Limitations:

* No handling of spelling errors aside from upper/lower case and whitespace issues (for example stopwords) because efficiency in running time is given more priority.

* No class is included for the guidebook because the application is too specific. Similar books such as a contactbook seem to give more opportunity to work with classes.





 
 