import random

options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

if user_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Congratulations! You win!")

elif user_choice == 'paper' and computer_choice == 'rock':
    print("Congratulations! You win!")

elif user_choice == 'scissors' and computer_choice == 'paper':
    print("Congratulations! You win!")

# use this way of constructing the boolean expression and turn
# the three elifs above into one big one!  Less code, same logic!
    
#elif ( 
#    (user_choice == 'rock' and computer_choice == 'scissors') or
#    (user_choice == 'paper' and computer_choice == 'rock') or
#    (user_choice == 'scissors' and computer_choice == 'paper')
#):
#    print("Congratulations! You win!")

else:
    print("Oops! Computer wins!")
