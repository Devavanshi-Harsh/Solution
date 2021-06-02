#Write a script which can read the files line by line with .log ext and print it into a
# file , while printing the data from the suffix with present date and time of the system.



#the program takes a file named sample.log and print it line by line also updates the data in another log file with
#present date and time of the system as a prefix and suffix as a sample.log data.

from datetime import *

with open("sample.log",'r') as file:
    for line in file:
        appn=str(datetime.now())+file.readline()
        file2= open("newfile.log", "a")
        file2.write(appn)
        file2.close()
        print(datetime.now(),file.readline())
