
#====================================================Number guessing game using python============================================

import random

a = random.randrange(1,5)	# random.randrange :- usesd to generate Random number in python.


user = int(input("Enter number between 1 to 5 : "))

while a	!= user:

	if user<a:
		print("_____Too low_____")
		
		print("")

		user = int(input("Enter try again : "))

		print("")

	elif user>a:
		print("_____Too high_____")
	
		print("")

		user = int(input("Enter try again : "))
		
		print("")

	else:
		break

print("Congratulation you guess right number...!")

print("")

user = int(input("Enter try again : "))


