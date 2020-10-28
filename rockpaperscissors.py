import random
print("rock, paper, scissors\ntype 'exit' to leave")

user_score = 0
cpu_score = 0

hands = ["rock", "paper", "scissors"]

def win():
    global user_score
    print("You won!")
    user_score = user_score + 1

def lose():
    global cpu_score
    print("You lost!")
    cpu_score = cpu_score + 1

while True:
    cpu = random.choice(hands)
    user = input("\n> ")

    if user == "exit" or user == "'exit'":
        break

    else:

        if user.lower().strip() not in hands:
            print("ERROR")

        if user.lower().strip() in hands:
            print("< " + cpu)

            if user.lower().strip() == cpu:
                print("Tie")

            elif user.lower().strip() == "rock" and cpu == "scissors":
                win()
    
            elif user.lower().strip() == "scissors" and cpu == "paper":
                win()

            elif user.lower().strip() == "paper" and cpu == "rock":
                win()

            elif user.lower().strip() == "rock" and cpu == "paper":
                lose()

            elif user.lower().strip() == "paper" and cpu == "scissors":
                lose()

            elif user.lower().strip() == "scissors" and cpu == "rock":
                lose()

            print(str(user_score) + "/" + str(cpu_score))