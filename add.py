# Dev changes for Staging
from getpass import getpass
import pwinput

pwd = 1234

def add_two_integers(a, b):
	add_two = a + b
	print(f"Sum of {a} + {b} is {add_two}")

def multi_two_integers(a, b):
	add_two = a * b
	print(f"Product of {a} * {b} is {add_two}")

def sub_two_integers(a, b):
	sub_two = a - b
	print(f"Difference of {a} * {b} is {sub_two}")


usrname = input("Enter username:")
pwd = int(pwinput.pwinput(prompt='Enter password: ', mask='*'))
#pwd = getpass("Enter password:")
if pwd == 1234:
	pass
else:
	print(f"Username/Password is incorrect")
    
print("Enter two numbers:")
num_1 = float(input("First num:"))
num_2 = float(input("Second num:"))
			  
add_two_integers(num_1,num_2)
sub_two_integers(num_1,num_2)
multi_two_integers(num_1,num_2)
print(f"Username is {usrname}.")
print(f"Password is {len(pwd)} .")













