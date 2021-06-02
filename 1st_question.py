#1: Write a Python program to read a file line by line and store it into a list.



#opening a file in read mode

with open("storyline",  "r") as file:
    storylist=[]
    print()
    #iterating the lines from the storyline file.


    for line in open('storyline').readlines(  ):
        print(line)


        #adding lines in the list
        storylist.append(line)
    print("----"*10, sep="*")
print("List is shown here --> \n")
print(storylist)