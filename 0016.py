"""
#PracticeCode: 0016                                              
Task: 
You have to create a program where you have to print first 3 letters of a the given word 3 times.
If the given input is less then 3 then print it 3 times as well.

input - Python
output - PytPytPyt

input - Ad
output - AdAdAd
__________________________________________
"""

#Take an input
n = input()
#Convert it to string
sample_str= str(n)
# Get First 3 character of a string in python
first_chars= sample_str[0:3]
#Print it 3 times by multiplying by 3
print(first_chars*3)
