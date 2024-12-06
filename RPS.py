player_wins = 0
computer_wins = 0
import random
while True:
  print("Let's play rock, paper, or scissors.")
  player_choice = input("Rock, paper, or scissors?").lower()
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  print(f"Computer chose: " + computer_choice)
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
    print("Congratulations! You won.")
  elif (player_choice == computer_choice):
    winner = "Tie"
  else:
    winner = "Computer"
    print("Computer won!")
  if winner == "Player":
    player_wins += 1
  elif winner == "Computer":
    computer_wins += 1
  else:
    print("It's a tie")
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
  play_again_choice = input("Press x to end game or enter to continue").lower()
  if (play_again_choice == "x"):
    print("Thanks for playing!")
    break