import random
u_score = 0
c_score = 0
# choice = random.choice(["bowling", "batting"])
print("Welcome to hand cricket! :)\nCredits: Arnav Saket")
toss = input("heads/tails?: ")
result = random.choice(["heads", "tails"])                                                     #toss
if(toss == result):
    print("You won the toss!")
    choice = input("batting or bowling?: ")
else:
    print("You've lost the toss")
    choice = random.choice(["batting", "bowling"])

print(f"You are {choice}!\nWhile batting, make sure that your runs are between 1-6.")
if(choice == "batting"):
    while True:
        run = int(input("Your run: "))                                                     #user's batting
        c = random.randint(1, 6)
        if(c != run):
            print(f"Computer chose {c}")
            u_score += run
        else:
            print("You are out!")
            break
    print(f"Your score is {u_score}.Now computer is batting")
    while True:
        run = int(input("Run: "))
        c = random.randint(1, 6)
        if(c != run):
            print(f"Computer chose {c}")
            c_score += c                                                                  #computer's batting
        else:
            print("Computer is out!")
            break
    print(f"Computer's score is {c_score}, your score is {u_score}")
    if(c_score > u_score):
        print("Computer Won!")                                                            #result
    elif(u_score > c_score):
        print("You won!")
    elif(u_score == c_score):
        print("Its a draw!")




if(choice == "bowling"):
    while True:
        run = int(input("Run: "))
        c = random.randint(1, 6)
        if(c != run):
            print(f"Computer chose {c}")
            c_score += c
        else:                                                                           #computer's batting 
            print("Computer is out!")
            break
    print(f"Computer's score is {c_score}.Now, you will bat.")
    while True:
        run = int(input("Your run: "))
        c = random.randint(1, 6)
        if(c != run):                        
            print(f"Computer chose {c}")
            u_score += run
        else:                                                                             #user's batting
            print("You are out!")
            break
    print(f"Your score is {u_score}, and computer scored {c_score}")
    if(c_score > u_score):
        print("Computer Won!")
    elif(u_score > c_score):
        print("You won!")                                                                  #result
    elif(u_score == c_score):
        print("Its a draw!")
