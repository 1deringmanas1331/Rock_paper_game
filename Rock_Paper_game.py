# Import the Random Library
import random 

# Define a Function to take user's choice
def get_user_choice():
    # Asks the user to choose between rock ,paper and scissor
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            
    # Takes the computer's choice
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to decide who is the winner or if it is a tie or if computer wins(you lose)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win congrats!"
    else:
        return "Computer wins!"

def main():
    # Game Starts from here
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
