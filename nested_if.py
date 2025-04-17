name = input("Enter name : ")
age = int(input("Enter age : "))
gender = input("Enter your gender(m/M for male and f/F for female) : ")

print("Name :",name,"\nAge :",age,"\nGender :",gender)

if (age >=18):
    print("You are eligible to vote")
    if (age >= 21 and gender == "m" or gender == "M"):
        print("You are also eligible for shadi")
    elif (age >= 18 and gender == "f" or gender == "F"):
        print("You are also eligible for shadi")
    else:
        print("You are only eligible for vote not for shadi")

else:
    print("You are not eligible for voting and not eligible for shadi")
    