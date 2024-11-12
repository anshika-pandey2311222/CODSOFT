import random

def get_user_choice():
    "Ask the user to select rock, paper, or scissors."
    while True:
        user_input = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        elif user_input == 'q':
            print("Thank you for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice! Please select valid option.")

def get_computer_choice():
    "Randomly select rock, paper, or scissors for the computer."
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    "Evaluate the winner based on user and computer choices."
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Output the choices made and the result of the round."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def main():
    "Main function to control the flow of the Rock-Paper-Scissors game."
    while True:
        user_score = 0
        computer_score = 0
        history = []

        print("Welcome to Rock-Paper-Scissors!")
        print("Instructions: Choose rock, paper, or scissors. The computer will randomly choose as well.")

        # Prompt the user for the number of rounds to play
        while True:
            try:
                rounds = int(input("How many rounds would you like to play? "))
                if rounds <= 0:
                    print("Please enter a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        # Loop through the specified number of rounds
        for _ in range(rounds):
            user_choice = get_user_choice()  # Get the user's choice
            computer_choice = get_computer_choice()  # Get the computer's choice
            result = determine_winner(user_choice, computer_choice)  # Determine the round result

            display_result(user_choice, computer_choice, result)  # Display the choices and result

            # Update scores based on the result
            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1

            history.append((user_choice, computer_choice, result))  # Record the choices and result
            print(f"Score - You: {user_score} | Computer: {computer_score}")

        # Show the history of all rounds played
        print("\nGame History:")
        for round_num, (user, computer, result) in enumerate(history, start=1):
            print(f"Round {round_num}: You chose {user}, Computer chose {computer}. Result: {result}")

        # Determine and display the overall winner
        if user_score > computer_score:
            print("\n'Congratulations! You are the overall winner!'")
        elif computer_score > user_score:
            print("\n'The computer is the overall winner. Better luck next time!'")
        else:
            print("\n'The game ended in a tie overall!'")

        # Ask if the user wants to play more rounds
        play_more = input("Do you want to play more rounds? (yes/no): ").lower()
        if play_more != 'yes':
            print("'Thank you for playing! Goodbye!'")
            break

if __name__ == "__main__":
    main()