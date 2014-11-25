from random import randrange

restart = True
userChoice = 0
cpuChoice = 0
choice = ['rock', 'paper', 'cisors']

while restart == True:
	while userChoice != 1 and userChoice != 2 and userChoice != 3:
		try:
			userChoice = int(input('Roc, paper or cisors ?\n1 - Roc\n2 - Paper\n3 - Cisors\n'))
		except:
			print('Invalid value, please enter a valid value.')
			continue
		if userChoice != 1 and userChoice != 2 and userChoice != 3:
			print('Invalid value, please enter a valid value.')

	cpuChoice = randrange(1, 4)

	print('You choosed the ' + choice[userChoice - 1])
	print('The computer choosed the ' + choice[cpuChoice - 1])

	if userChoice == 1:
		if cpuChoice == 3:
			print('You win !')
		elif cpuChoice == 2:
			print('You lose !')
		else:
			print('Tie !')
	elif userChoice == 2:
		if cpuChoice == 1:
			print('You win !')
		elif cpuChoice == 3:
			print('You lose !')
		else:
			print('Tie !')
	else:
		if cpuChoice == 2:
			print('You win !')
		elif cpuChoice == 1:
			print('You lose !')
		else:
			print('Tie !')

	userChoice = 0
	cpuChoice = 0

	while restart != 'Y' and restart != 'y' and restart != 'N' and restart != 'n':
		restart = input('Would you like to restart? Y/N\n')
		if restart != 'Y' and restart != 'y' and restart != 'N' and restart != 'n':
			print('Invalid value, please enter a valid value.')

	if restart == 'Y' or restart == 'y':
		restart = True
	else:
		restart = False
