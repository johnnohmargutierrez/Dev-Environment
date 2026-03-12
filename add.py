#just added a comment
def add_two_integers(a, b):
	add_two = a + b
	print(f"Sum of {a} + {b} is {add_two}")

def multi_two_integers(a, b):
	add_two = a * b
	print(f"Product of {a} * {b} is {add_two}")

def sub_two_integers(a, b):
	add_two = a - b
	print(f"Difference of {a} * {b} is {add_two}")
    
print("Enter two numbers:")
num_1 = float(input("First num:"))
num_2 = float(input("Second num:"))
			  
add_two_integers(num_1,num_2)
diff_two_integers(num_1,num_2)
multi_two_integers(num_1,num_2)











