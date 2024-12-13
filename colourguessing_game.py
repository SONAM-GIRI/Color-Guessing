import random

valid_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'black', 'white']
scoreboard = {}

def start_game(player_name):
    attempts = 5
    color = random.choice(valid_colors)
    print("\nWelcome to the Colour Guessing Game!")
    print("Guess the correct color from the following list:")
    for col in valid_colors:
        print(f"- {col}")

    while attempts > 0:
        user_color = input("Enter your color guess: ").lower()

        if user_color not in valid_colors:
            print("Invalid color entered. Please choose from the given list.")
            continue

        if user_color == color:
            print("Congratulations! You guessed the correct color!")
            scoreboard[player_name]['won'] += 1
            break
        else:
            attempts -= 1
            print("Wrong guess!")
            print(f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"Sorry, you lost! The correct color was {color}.")
        scoreboard[player_name]['lost'] += 1

    print("\nGame Over!")
    while True:
        print("\n1. See Scoreboard")
        print("2. Play Again")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_scoreboard()
        elif choice == '2':
            start_game(player_name)
        elif choice == '3':
            exit_game()
        else:
            print("Invalid choice. Please try again.")

def show_scoreboard():
    print("\nScoreboard:")
    for name, scores in scoreboard.items():
        print(f"Player: {name}")
        print(f"Games Won: {scores['won']}")
        print(f"Games Lost: {scores['lost']}")
        print("-" * 50)

def exit_game():
    print("\nThank you for playing the Color Guessing Game. Goodbye!")
    exit()

def main():
    print("Welcome to the Color Guessing Game!")
    player_name = input("Please enter your name for the scoreboard: ").strip()

    if player_name not in scoreboard:
        scoreboard[player_name] = {'won': 0, 'lost': 0}

    while True:
        print("\n1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_game(player_name)
        elif choice == '2':
            exit_game()
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main()
