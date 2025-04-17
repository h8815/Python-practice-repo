str = input("Enter something for checking that it is palindrome or not :")
revstr = str[::-1];

if (str == revstr):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")