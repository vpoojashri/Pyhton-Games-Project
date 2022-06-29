from colorama import Fore, Back, Style
print()
heading=(Fore.MAGENTA+Style.BRIGHT+"         HELLO FOCKS ,WELCOME TO TRIO GAME")
print(heading.center(160))
import Registration_and_Login
print()
print(Fore.MAGENTA+Style.BRIGHT+"LIST OF GAMES:\n 1.ROCK PAPER SCISSOR \n 2.TIK TAK TOE \n 3.WORD RIDDLE")


def game():
    game = int(input("Enter The Game Number You Need To Play: "))
    if game==1:
        import RPS
    elif game==2:
        import tictaktoe
    else:
        import WordRiddle

game()




