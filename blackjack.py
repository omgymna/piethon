import random
from art import blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#deal card
def deal_card(cards_in_hand):
  score = check_score(cards_in_hand)
  if score < 17:
    index = random.randint(0, 12)
    cards_in_hand.append(cards[index])

def check_score(cards_in_hand):
  score = 0
  for n in range(len(cards_in_hand)):
    score += cards_in_hand[n]
    if score > 21 and cards_in_hand[n] == 11:
      score-= 11
      cards_in_hand.remove(11)
      cards_in_hand.append(1)
      score += 1
  return score

def compare(user_score, computer_score):
  if computer_score > 21:
    print(f"Your score is currently {user_score}. Opponent's score is {computer_score}. You win!")
    play_again = input("Do you want to play again? (y/n) : ")
  elif user_score > computer_score:
    print(f"Your score is currently {user_score}. Opponent's score is {computer_score}. You win!")
    play_again = input("Do you want to play again? (y/n) : ")
  elif user_score == computer_score:
    print(f"Your score is currently {user_score}. Opponent's score is {computer_score}. You tied.")
    play_again = input("Do you want to play again? (y/n) : ")
  else:
    print(f"Your score is currently {user_score}. Opponent's score is {computer_score}. You lose.")
    play_again = input("Do you want to play again? (y/n) : ")

user_cards = []
computer_cards = []
play_again = 'y'
#deal 2 random cards
while play_again == 'y':
  print(blackjack_logo)
  user_cards = []
  computer_cards = []
  deal_card(user_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  deal_card(computer_cards)

  print(f"Your starting cards are {user_cards[0]} and {user_cards[1]}.")
  
  #checking if BJ
  computer_score = check_score(computer_cards)
  user_score = check_score(user_cards)
  
  if computer_score == 21:
    print("Opponent has blackjack. You lose.")
    play_again = input("Do you want to play again? (y/n) : ")
  elif user_score == 21:
    print("You Win!")
    play_again = input("Do you want to play again? (y/n) : ")
  #if either isn't blackjack
  
  print(f"Opponent's first card is: {computer_cards[0]}")
  
  user_score = check_score(user_cards)
  should_draw = input(f"Your score is currently {user_score}, do you want to draw again? (y/n) : ")
  
  while should_draw == 'y':
    deal_card(user_cards)
    user_score = check_score(user_cards)
    if user_score > 21:
      print("You're over 21. Game Over")
      play_again = input("Do you want to play again? (y/n) : ")
      break
    elif user_score == 21:
      print("You got blackjack. You win!")
      play_again = input("Do you want to play again? (y/n) : ")
      break
    should_draw = input(f"Your score is currently {user_score}, do you want to draw again? (y/n) : ")
    
  while computer_score < 17:
    deal_card(computer_cards)
    computer_score = check_score(computer_cards)

  compare(user_score, computer_score)
  
