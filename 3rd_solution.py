# 3. Write a Python program to convert the Python dictionary object (sort by key) to
# JSON data. Print the object members with indent level 4.




#importing json
from json import *

# A dictionary is loaded
l_dict = {'def': 33, 'abc': 21, 'ghi': 85, 'jkl': 45}
print(f"loaded dictionary : {l_dict}")

#using formate string and dumps function to covert the data and used sort as key and indent at 4
print(f"\nConverted Json Data : \n{dumps(l_dict, sort_keys=True, indent=4)}")
