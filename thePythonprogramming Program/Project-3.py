
#=================================================Snake-Water-Gun=====================================================

import random

x = ['snake','water','gun']

computer = random.choice(x)

player = input("Enter snake,water,gun : ").lower()

if player == computer:
	print("Match tie...")

elif( (player == 'snake' and computer == 'water') or \
     (player == 'water' and computer == 'gun') or \
     (player == 'gun' and computer == 'snake') ):
    print("You win...")

else:
     print("You loss...")

print(f"Your chose: {player} and Computer chose {computer}")
