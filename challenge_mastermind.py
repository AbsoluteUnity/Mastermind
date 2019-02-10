import sys
import random
import re


attempts = 0
while True: 
	userguess = input("Guess the 4 numbers in as few tries as possible ")
	actualnumber = random.randint(1,9999)
	x = re.split([actualnumber],{userguess})
	print (x)
	attempts += 1
	if userguess == actualnumber:
		print (f'You did it in {attempts} tries')
		break
	break
print ("test")