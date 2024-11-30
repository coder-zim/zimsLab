# Random Guessing Game
# Coder: zim

'''
This is a random number guessing game.  The user is prompted for the range
of numbers they want to guess from.  The program then generates a random number
and compares it to their guesses, counting each attempt. 
Upon completion, the program displays number of attempts it took to get the 
correct number.  The user can also quit the game by typing 'q' at any time.
'''

import random

print("Welcome to the Number Guessing Game!")

def main(): 
    
  while True:
    range = input('How large do you want the range to be? ').lower()
    
    try:
        range = int(range)  # Tries to convert input to an int
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a valid number.")

  try: 
    random_num = random.randint(0, range)
    attempts = 0

    while True: 
      guess = input((f'Guess a number between 0 - {range}: ')).lower()

      # Allows user to quit the game
      if guess == 'q': 
        print('Bye, Felicia! Quitters do not get a score. ✌️💩')
        quit()  

      # Converts input to an integer
      guess = int(guess) 
      attempts += 1 # Increments the number of attempts

      # Compares the user's guess to the random generated number
      if guess < random_num:
        print('Incorrect, your guess is too low. Try again! (q to quit): ')
      elif guess > random_num:
        print('Incorrect, your guess is too high. Try again! (q to quit): ')
      else: 
        print(f'Correct!👏 YOU WON!!! \nAttempts: {attempts}')
        break
  except ValueError: 
    print('Invalid input. Please enter a valid number.')

main()