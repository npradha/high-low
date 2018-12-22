game = True

while game:
	print("\n")
	print("******************************")
	print("Welcome to the High-Low Game!!")
	print("******************************\n")
	print("Think of a number between 1-100")
	low = 1
	high = 100
	mid = (low + high) / 2
	while high>=low:
	  print("Is your number less than " + str(mid) + " (y/n)")
	  answer = raw_input()
	  answer = answer.lower() 
	  if answer == 'y':
		high = mid - 1
		mid = (low + high) / 2 
	  elif answer == 'n':
		low = mid + 1
		mid = (low + high) / 2
	  else:
		print("**Invalid input**")
		continue
	print("******************************")	
	print("The number is " + str(mid) + "!!")
	print("******************************\n")	
	print("Do you want to play again? (y/n)")
	answer = raw_input()
	answer =  answer.lower()
	if answer == 'y':
		continue
	else:
		game = False
print("\n")	
print("Thanks for playing!!! :) ")
	
		

