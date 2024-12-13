import random

valid_colors=['red','blue','green','yellow','purple','orange','pink','black','white']

scoreboard={}

def start_game(play_name):
    attempts=5
    win=0
    loss=0

    color=random.choice(valid_colors)
    print("Welcome to the Colour guessing game>>>>>>")
    print("Please enter the colour you like>>>")

    while attempts>0:
        user_color=input("Enter your the colour you like>>>")

        if user_color not in valid_colors:
            print("Invaild color entered")
            continue
        if user_color==color:
            win=win+1
            print("Congratulation ! you won the game.")
            print(f"Number of attempts left:{5-attempts+1}")
            break
        else:
            attempts-=1
            print("Your guess was wrong.")
            print(f"Number of attempts left:{attempts:02d}")

    if attempts==0:
        loss+=1
        print("Sorry you  have lost the game.")
    print("\n Game Over!")
    print("1> See Score Board")
    print("2> Play again")
    print("3> Exit")

    choice=input("Enter your choice")
    if choice=='1':
        show_scoreboard()
    elif choice=='2':
         start_game(play_name)
    elif choice=='3':
         exit_game()

def show_scoreboard():
    print("\n ScoreBoard:")
    for name, scores in scoreboard.items():
        print(f"Name:{name}")
        print(f"Game won:{scores['won']}")
        print(f"game lost:{scores['lost']}")
        print("---------------------------------------------------")

def exit_game():
    print("------------------Thanks for playing the game------------------")
    exit()
def main():
     print("Welcome to the color Game>>>")
     player_name=input("Please enter your name for the scoreboard:")
     if player_name not in scoreboard:
            scoreboard[player_name]={'won':0,'lost':0}
     while True:
           print("\n1> Start game")
           print("2> Exit")
           choice=input("Enter your Choice:")
           if choice=='1':
              start_game(player_name)
           elif choice=='2':
               exit_game()


if __name__=='__main__':
    main()
