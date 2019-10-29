# defining a decorator 
@decorator 
def hello_decorator(func): 

	# inner1 is a Wrapper function in 
	# which the argument is called 
	
	# inner function can access the outer local 
	# functions like in this case "func" 
	def f(): 
		print("Hello, this is before function execution") 

		# calling the actual function now 
		# inside the wrapper function. 
		func()  

		print("This is after function execution") 
		
	return f

# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 


# calling the function 
function_to_be_used() 

