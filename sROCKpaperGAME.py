import random
def playORnot():
    inp = input("Do you want to play again ?(y/n) : ").lower()
    if (inp == "y"):
        game(user)
    else:
        print("Exiting...")
        exit()

def game(user):
    choose = ["rock", "paper", "scissor"]
    bot = random.choice(choose)
    user1_choice = input(f"{user}, what do you want to choose(rock, paper, scissor) : ").lower()
    print(f"computer choose : {bot}")
    if(user1_choice == bot):
        print("Tie...")
        playORnot()
    elif (user1_choice == "rock" and bot == "scissor"):
        print(f"{user} is winner")
        playORnot()
    elif (user1_choice == "paper" and bot == "rock"):
        print(f"{user} is winner")
        playORnot()
    elif (user1_choice == "scissor" and bot == "paper"):
        print(f"{user} is winner")
        playORnot()
    elif (bot == "rock" and user1_choice == "scissor"):
        print(f"computer is winner")
        playORnot()
    elif (bot == "paper" and user1_choice == "rock"):
        print(f"computer is winner")
        playORnot()
    elif (bot == "scissor" and user1_choice == "paper"):
        print(f"computer is winner")
        playORnot()
    else:
        print("Invalid input, Please correct it..!!")
        playORnot()

user = input("Enter your name : ")
game(user)


