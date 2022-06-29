import numpy as np
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


x=[1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix=np.array(x).reshape(3,3)


heading=("TIC TAK TOE")
print(heading.center(160))
name=input("Enter Player Name: ")
print("Hi "+name+" i am ALEXI Your Game Patner")
print(Style.RESET_ALL+"GAME POSITIONS")
for k in matrix:
    print(str(k).strip("[,]"))

print(Back.BLUE+Style.BRIGHT+Fore.BLACK+name+" PLAYER GOT 'X'")
print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+ "Alexi GOT 'O'")

positions=0,1,2,3,4,5,6,7,8
z=[]
def rand(positions):
      rand_no= random.choice(positions)
      if rand_no not in z:

          x[rand_no] = "O"
          print("Alexi Position",rand_no+1)
          z.append(rand_no+1)
          return rand_no
      else:
          rand(positions)

def human():
    player=int(input("Player Enter Your Position:"))
    if player in z:
        print(player,"is already taken")
        a=int(input("Enter Valid Position: "))
        z.append(a)
    else:
        x[player - 1] = "X"
    z.append(player)


for i in range(4):
    player=human()

#training alexi to play

    if ((x[1]=="X" and x[2]=="X") or (x[3]=="X" and x[6]=="X") or (x[4]=="X" and x[8]=="X")) and (x[0]==1) :
      print("Alexi Position is 1")
      x[0]="O"
      z.append(1)
    elif ((x[0]=="X" and x[2]=="X") or (x[4]=="X" and x[7]=="X") or (x[0]=="O" and x[2]=="O") or (x[4]=="O" and x[7]=="O")) and (x[1] == 2):
         print("Alexi Position is 2")
         x[1]="O"
         z.append(2)
    elif ((x[0] == "X" and x[1] == "X") or (x[6] == "X" and x[4] == "X") or (x[8] == "X" and x[5] == "X") or (x[0] == "O" and x[1] == "O") or (x[6] == "O" and x[4] == "O") or (x[8] == "O" and x[5] == "O")) and (x[2] == 3):
            print("Alexi Position is 3")
            x[2] = "O"
            z.append(3)
    elif ((x[4]=="X" and x[5]=="X") or (x[0]=="X" and x[6]=="X") or(x[4]=="O" and x[5]=="O") or (x[0]=="O" and x[6]=="O")) and (x[3] == 4):
          print("Alexi Position is 4")
          x[3]="O"
          z.append(4)
    elif ((x[0] == "O" and x[8] == "O") or (x[2] == "O" and x[6] == "O") or (x[1] == "O" and x[7] == "O") or ( x[3] == "O" and x[5] == "O")) and (x[4] == 5):
                print("Alexi Position is 5")
                x[4] = "O"
                z.append(5)
    elif ((x[3]=="X" and x[4]=="X") or (x[2]=="X" and x[8]=="X") or (x[3]=="O" and x[4]=="O") or (x[2]=="O" and x[8]=="O")) and (x[5]==6):
         print("Alexi Position is 6")
         x[5]="O"
         z.append(6)
    elif ((x[7]=="X" and x[8]=="X") or (x[0]=="X" and x[3]=="X")or (x[7]=="O" and x[8]=="O") or (x[0]=="O" and x[3]=="O")) and (x[6] == 7): #0 3
         print("Alexi Position is 7")
         x[6]="O"
         z.append(7)
    elif ((x[1]=="X" and x[4]=="X") or (x[6]=="X" and x[8]=="X")or(x[6]=="O" and x[8]=="O") or (x[1]=="O" and x[4]=="O")) and (x[7] == 8):
         print("Alexi Position is 8")
         x[7]="O"
         z.append(8)
    elif ((x[6]=="X" and x[7]=="X")or (x[6]=="O" and x[7]=="O") or (x[2]=="O" and x[5]=="O") or (x[2]=="X" and x[5]=="X")) and (x[8] == 9):        #2 5
             print("Alexi Position is 9")
             x[8]="O"
             z.append(9)

    else:
     computer=rand(positions)


    matrix=np.array(x).reshape(3,3)
    for s in matrix:
        print(str(s).strip("[,]"))


    if x[0]=="X" and x[1] =="X"and x[2] == "X" :
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"Player Wins")
        break
    elif (x[3]=="X" and x[4]=="X" and x[5] == "X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif (x[6]=="X"and x[7]=="X" and x[8]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif (x[0]=="X"and x[3]=="X" and x[6]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif (x[1]=="X"and x[4]=="X" and x[7]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif(x[2]=="X" and x[4]=="X" and x[6]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif(x[0]=="X" and x[4]=="X" and x[8]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break

    elif (x[2]=="X"and x[5]=="X" and x[8]=="X"):
        print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"player Wins")
        break
    elif x[0]=="O" and x[1] =="O"and x[2] == "O" :
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[3]=="O" and x[4]=="O" and x[5] == "O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[6]=="O"and x[7]=="O" and x[8]=="O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[0]=="O"and x[3]=="O" and x[6]=="O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[1]=="O"and x[4]=="O" and x[7]=="O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[2]=="O"and x[5]=="O" and x[8]=="O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"ALexi Wins")
        break
    elif (x[2] == "O" and x[4] == "O" and x[6] == "O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
    elif (x[0] == "O" and x[4] == "O" and x[8] == "O"):
        print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+"Alexi Wins")
        break
else:
    print(Style.BRIGHT+Fore.RED+"MATCH DRAW")

