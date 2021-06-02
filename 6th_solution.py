# 6.  Write a Python program to convert an array to an array of machine values and
# return the bytes representation.
# Expected Output:
# Original array:
# A1: array('i', [1, 2, 3, 4, 5, 6])
# Array of bytes: b'010000000200000003000000040000000500000006000000'


from binascii import hexlify
from array import array


Ar = array('i', [1,2,3,4,5,6])
print('A1:', Ar)

bytes_array = Ar.tobytes()
print(f" Array of Bytes : \n\t\t{ hexlify(bytes_array)}")