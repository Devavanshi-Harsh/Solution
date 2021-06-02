#You can stop the chain by pressing 0 after the completion of a file otherwise just press any character keys.



import os
from pathlib import Path


#i am taking my storylines content as random log
from random import choices
with open("storyline", "r") as file:
    a=file.read()


file_number = 0

#if the size will be less than 2mb then the file will be consistently
# updated with same storyline content until size is not reached 2mb



while True:


    with open("xyz%d.txt"%file_number, "a") as file:
        pass
    size = os.path.getsize("xyz%d.txt"%file_number)

    if size<1024*2*1024:
        with open("xyz%d.txt"%file_number, "a") as file:
            file.write(a)
    else:
        file_number+=1
        print("A file of size 2 mb is creaded do you want stop Press\n 0 to stop")
        break_chain = int(input("press 0 to stop"))
        if break_chain==0:
            break




print("completed")