emoji = {'r' : '🪨', 
     'p' : '📃', 
     's' : "✂️"}

import random

print("welcome to rock paper scissors game")
print("Choose rock by Typing: \"r\"\n choose paper by Typing: \"p\"\n choose scissors by Typing: \"s\"")


while True:
    print("rock, paper or scissors? [r/p/s]:", end=" ")
    a = input("").lower()
    b = random.choice(['r','p','s'])

    if a not in emoji:
        print("invalid choice")
        continue   

    elif a==b:
        print("you choose:" , end="") 
        print(emoji[a])
        print("computer choose:", end=" ")
        print(emoji[b])
        print("tie")

    elif (a== "r" and b == "s" or a== "s" and b == "p" or a== "p" and b == "r"):
        print("you choose:", end =" ")
        print(emoji[a])
        print("computer choose:", end=" ")
        print(emoji[b])

        print("You Win!!!!")

        print("continue?:(y/n)", end="")
        c = input("").lower()
        if c == "y":
            continue
        elif c == "n":
            print("thanks for playing")
            break
    else:
        print("you choose:", end = "")
        print(emoji[a])
        print("computer choose:", end = "")
        print(emoji[b])

        print("you lose")

            