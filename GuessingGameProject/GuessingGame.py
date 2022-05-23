"""
Author Name: Junior David Roche
Project 1
"""

from random import randint

welcome = '*******Welcome To the guessing game*******'
info = '.....can you guess what it is? .....'
extraInfo = '-----the computer is thinking of a number between 0 to 100-----\n' + info.center(len(info) + 45)
print(welcome.upper().center(len(welcome) + 40))
print(extraInfo.title().center(len(extraInfo) + 20))
print('\n' + '~' * 98)

# create an empty list to fill in incorrect guess
badGuessList = []
count = 0
# Computer generates random number
xRand = randint(0, 100)
print(xRand)

# Ask user of their names
userName = input('Please, enter your name here: ')
print('\nGood luck', userName + '! You gonna need it 😀')
congrat = 'Congratulations ' + userName.upper() + '!'

# Ask user to enter guessed number
while True:
  userInput = input('\nPlease, enter your guessing number: ')
  try:
    validInput = int(userInput)
    if validInput == xRand:
      print(f'\nBravo!🥳 The Computer was thinking of number {xRand} as well.\n')
      print(('~' * 30) + congrat + ('~' * 30))
      print(f'Your incorrect guesses were: {badGuessList}')
      print('It took you', count, 'tries to get the correct answer.')
      break
    elif validInput < xRand and 0 <= validInput <= 100:
      print('Hmmmm... You guessed too low. Guess higher.')
      badGuessList.append(validInput)
      count += 1
    elif validInput > xRand and 0 <= validInput <= 100:
      print('Hmmmm... You guessed too high. Guess lower.')
      badGuessList.append(validInput)
      count += 1
    elif int(userInput) not in range(101):
      print('Invalid input. Please, keep your guesses between 0 and 100')
      
  # Catch and Throw Error message    
  except ValueError:
    print('Invalid input. Please, keep your guesses as an integer between 0 and 100')
