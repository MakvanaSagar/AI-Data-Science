
#========================================Local & Global Variable====================================================

#Global variable :- Global variable data acccess to program any location (LIKE "IN FUNCTION" or "OUT OF FUNCTION")

#Local variable :- Local variable data access for Ristricted are ("For under Function can access data")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[1]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
a = 99 #"Global variable" means that out of Function or out of Program (You can access global varible any location of Program)

def myFun(): 
	b = 178
	print(b) 	#178
			#Local variable it can be data access for the Inside of Function

myFun()
print(a) #99
print(b) #through error WHY(by ruls)
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[2]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = 498

def myFun():
	global y
	y = 52
	print(y)	#52

myFun()

print(x)	#498
print(y)		#You can access the data in LOCAL VARIABLE OF FUNCTION USING A "Global keyword inside of Function"