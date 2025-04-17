import random
x = random.randint(1,1000)
count = 0
user = -1
while (user != x):
    count+=1
    user = int(input("Guess number from (1 - 1000) : "))
    if(user < x):
        print("higher number please")
    elif(user > x):
        print("Lower number please")

print(f"Congratulation...You guess {x} correctly in {count} attempts")
