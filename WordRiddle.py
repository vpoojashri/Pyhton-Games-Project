import colorama
from colorama import Fore, Back, Style
import time
colorama.init(autoreset=True)
heading=("WORD RIDDLE")
print(heading.center(160))
gener=int(input("Select 1 for Space  Riddle \n"
            "Select 2 for Food   Riddle \n"
            "Select 3 for Common Riddle : "))
print()
question=["1.What word contain all of 26 letter","2.Which word in the dictionary is spelled incorrectly","3.What room has no door or window",
          "4.What color can you eat","5.I have many words but i will never speak"]

space=["1.At night they come without being fetched. By day they are lost without being stolen. What are they?","2.I'm sometimes full, but I never overflow. What Am I?",
       "3.What planet has the shortest year?","4.It can fill a room without occupying space. What is that?",
       "5.I am bigger than Venus and smaller than Uranus,I am a living rock"]

food=["1.What kind of cup doesn't hold water?","2.It looks green, it opens red. What you eat is red, but what you spit out is black",
      "3.What has no beginning, end, or middle?","4.What kind of dog has no tail?","5.I am a fruit with seeds on the outside.What am I?"]

ans = ["alphabet", "incorrectly","mushroom","orange","book"]
space_ans = ["stars", "moon", "mercury", "light", "earth"]
food_ans = ["cupcake", "watermelon", "doughnut", "hotdog", "strawberry"]

def riddle(q,a):
    i=0
    print(q,end=" ")
    x1 = ["_" for i in range(len(a))]
    x = [print(i,end=" ") for i in x1]
    print()

    while i<len(a):
            user=input("Guess the Letter/word: ")
            j = (",").join(a)
            ans1 = j.split(",")
            if user.lower()==a:
                print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"YOU GOT IT")

                print()
                return
            elif i==len(a)-1:
                if user.lower()==a:
                    print(Back.BLUE+Style.BRIGHT+Fore.BLACK+"YOU GOT IT")

                    print()
                    return

                else:
                    print("OOPS You missed it")

                    print()
                    return
            elif user.lower() in ans1:
                ind=ans1.index(user.lower())
                x1[ind]=user.lower()
                x = [print(i,end=" ") for i in x1]
                print()
            else:
                print("The Letter/word is Missing!")

            chances=[c for c in reversed(range(len(a)))]
            print("                                Remaining Life",end=" ")
            rem_chances=[print("\u2764\uFE0F",end="") for j in range(chances[i])]

            print()
            i=i+1


if gener==1:
    r = [riddle(q, a) for q, a in zip(space, space_ans)]
elif gener==2:
    r = [riddle(q, a) for q, a in zip(food,food_ans)]
else:
    r = [riddle(q, a) for q, a in zip(question, ans)]
print("NICE PLAY")

