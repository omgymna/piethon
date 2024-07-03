import random
from art import guess
print(guess)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

lives = 10
if difficulty == 'hard':
  lives = 5

correct_number = random.randint(1,100)
while lives != 0:
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

  if guess == correct_number:
    print("You guessed it right!")
    break
  elif guess < correct_number:
    lives -= 1
    if lives != 0:
      print("Too low.\nGuess again.")
    else:
      print("You're out of attempts.")
  else:
    
    lives -= 1
    if lives != 0:
      print("Too high.\nGuess again.")
    else:
      print("You're out of attempts.")
