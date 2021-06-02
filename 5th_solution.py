from re import split

file_name=input("enter the name of file Example= storyline :")

with open(file_name, "r") as file:
    a=file.read()
    a=a.replace(",", " ")
    alist=a.split(" ")
    print(alist)
    print(len(alist))