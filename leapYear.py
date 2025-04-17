def single_leapyear():
    year = int(input("Enter year you want to check : "))
    if ((year%4 == 0 and year%100 != 0 ) or year%400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    check_again()

def leapyear_range():
    yr_list = []
    Syear = int(input("Enter start year : "))
    Eyear = int(input("Enter end year : "))
    for year in range(Syear,Eyear+1):
        if year%4 == ((0 and year%100 != 0 ) or year%400 == 0):
            yr_list.append(year)
    print(yr_list)
    check_again()

def check_again():
    check = input("Do you want to check again (y/n) : ").lower()
    if (check == 'y'):
        choose = int(input("Press {1} for single leap \nPress {2} for range of leap year\nEnter choice : "))
        match choose:
            case 1:single_leapyear()
            case 2:leapyear_range()
            case _:print("Invalid Input..!!");exit()
    else:
        print("Thank you..!!")
        exit()

print("Welcome to leap year checker...")
choose = int(input("Press {1} for single leap \nPress {2} for range of leap year\nEnter choice : "))
match choose:
    case 1:single_leapyear()
    case 2:leapyear_range()
    case _:print("Invalid Input..!!");exit()