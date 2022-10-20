import random

print ("-----------------------------------------------")
print ("-- If you win 3 times, You'll win 500 pesos! --")
print ("-----------------------------------------------\n")

name = input("Enter your name: ")

play = input("Type start to continue: ")
print("   ")

print("THE FIRST GAME IS ROCK, PAPER, SCISSORS!!")

user = input("Enter a choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
computer = random.choice(actions)
print(f"You chose {user}, computer chose {computer}.")

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        
print("   ")
print("THE SECOND GAME IS COIN TOSS")

coin = ["Heads","Tails"]
toss = random.choice(coin) # This simulates the coin being tossed

selection = input("Heads or Tails: ")

if selection == toss:
    print("You win! The coin landed on " + toss)
else:
    print("You lose! The coin landed on " + toss)
