"""
#PracticeCode: 0038
🎯 FORWARD IF YOU LIKE IT 🎯

Task:
Create a program to input a number and check if it is multiple of 2 than print "Sel" , if multiple of 5 then print "fish" or if multiple of both then print "Selfish".

Sample :-
input - 5
output - fish

input - 10
output - Selfish
_________&____________________________________________________________________________
"""


#print("Enter a Number: ")
n= int(input())    # Take Input Number
if n%2==0  and n%5==0:    # This should be first condition & use modules sign
	print("Selfish")
elif n%2==0:
	print('Sel')
elif n%5==0:
	print("fish")
else:
	("")
