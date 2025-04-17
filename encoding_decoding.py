import random
import string

def generate_random_string():
    return ''.join(random.choices((string.ascii_letters  + string.digits), k=3))

def Encoding():
    first_3 = generate_random_string()
    last_3 = generate_random_string()
    word = input("Enter word : ")
    if len(word) >= 3:
        for char in word:
            word = first_3 + char + last_3
            print(word,end="")
    else:
        print(word[::-1])
    
def Decoding():
    word = input("Enter word : ")
    first_3 = word[:3]
    last_3 = word[-3:]
    if len(word)<3 :
        print(word[::-1])
    else:
        word = word.replace(first_3,"").replace(last_3,"")
        print(word)

def main():
    print("What do you want to prefer : ")
    choice = int(input("1.Encoding\n2.Decoding\n3.Quit\nEnter choice: "))
    match(choice):
        case 1:
            Encoding()
        case 2:
            Decoding()
        case 3:
            print("Exiting...")
            exit()            
        case _:
            print("Invalid Input, please choose 1,2 and 3")

main()
