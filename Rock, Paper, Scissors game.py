import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()

        result = get_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing! Final Score:")
    print(f"You: {user_score} | Computer: {computer_score}")

play_game()
