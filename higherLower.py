import random
from art import hl_logo, vs_art
from game_data import instagram_data
from replit import clear

#This is a guessing game to guess who has more instagram followers. Game continues until wrong answer is given.


should_continue = True
score = 0
hl_logo()
choice_a = random.choice(instagram_data)

while should_continue:
  
  choice_b = random.choice(instagram_data)
  if choice_b == choice_a:
    choice_b = random.choice(instagram_data)

  print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
  vs_art() 
  print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
  

  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  count_a = choice_a['follower_count']
  count_b = choice_b['follower_count']
  
  if (guess == 'A' and count_a > count_b) or (guess == 'B' and count_a < count_b):
    score += 1
    clear()
    hl_logo()
    print(f"You're Right! Score is: {score}")
    choice_a = choice_b
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    should_continue = False
