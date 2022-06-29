import random
import colorama
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
heading="ROCK PAPER SCISSOR"
h=heading.center(160)
print(h)

name=input("ENTER YOUR NAME PLAYER: ")
print("Hi,", name, "I Am Alexi Your Game Patner")
print()
print("1 FOR Rock")
print("2 FOR Paper")
print("3 FOR Scissor")
number_of_times=3
rock_paper_scissor=[1,2,3]
count_of_wins=[]
print("Player is",name)
def rps(number_of_times):
 for i in range(number_of_times):
    print()
    a =int(input("Your Turn Player: "))
    if a>4:
        print("That's Not a Valid Number ")
        a=int(input("Enter Valid Number "))
    if a==1:
        print("Your Choice is ROCK ")
    elif a==2:
        print("Your Choice is PAPER")
    elif a==3:
        print("Your Choice is SCISSOR")
    else:
        print("Enter Valid Number")
    time.sleep(0.10)
    b = random.choice(rock_paper_scissor)
    if b==1:
        print("Alexi Choice is ROCK ")
    elif b==2:
        print("Alexi Choice is PAPER")
    else:
        print("Alexi Choice is SCISSOR")
    if  (a==1 and b==3):
        print(Fore.YELLOW+name+Fore.YELLOW+" WINS "+Fore.GREEN+ name+Fore.GREEN+" Smashes Alexi")
        count_of_wins.append(1)
        print()
    if (a==1 and b==2):
        print(Fore.CYAN+"ALEXI WINS "+Fore.GREEN+" Alexi Catch "+Fore.GREEN+ name)
        count_of_wins.append(2)
        print()
    if (a==2 and b==1):
        print(Fore.YELLOW+name,Fore.YELLOW+" WINS "+Fore.GREEN+ name+Fore.GREEN+" Catch Alexi")
        count_of_wins.append(1)
        print()
    if (a==2 and b==3):
        print(Fore.CYAN+"ALEXI WINS "+Fore.GREEN+" Alexi Cut "+Fore.GREEN+ name)
        count_of_wins.append(2)
        print()
    if (a==3 and b==2):
        print(Fore.YELLOW+name+Fore.YELLOW+" WINS "+Fore.GREEN+ name+Fore.GREEN+" Cut Alexi")
        count_of_wins.append(1)
        print()
    if (a==3 and b==1):
        print(Fore.CYAN+"ALEXI WINS "+Fore.GREEN+" Alexi Smashes ",Fore.GREEN+ name)
        count_of_wins.append(2)
        print()

    if (a==1 and b==1) or (a==2 and b==2) or (a==3 and b==3) :
        count_of_wins.append(0)
        print("Draw")

 more_play=int(input(" PLAY MORE (Press 1)\n END GAME(Press 2): "))
 if more_play == 1 :
        number_of_times=3
        rps(number_of_times)
 else:
        return "END GAME"

(rps(number_of_times))

w=[]
for j in count_of_wins:
    w.append(count_of_wins.count(j))

maxx_of_count=(max(w))
finding_index=w.index(maxx_of_count)
result=(count_of_wins[finding_index])

if result == 1:
    print(Fore.MAGENTA+"\n'CONGRATULATIONS PLAYER'")
# elif result == 0:
#     print(Fore.MAGENTA+"\n'MATCH DRAW")
else:
    print(Fore.MAGENTA+"\n'BETTER LUCK NEXT TIME'")