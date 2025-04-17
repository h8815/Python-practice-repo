# num1 = float(input("Enter first number : "))
# num2 = float(input("Enter second number : "))

print("Select any operation : \n1.Addition\n2.Substraction\n3.Multlipication\n4.Division\n5.Modulo")
inp = int(input("Enter operational number : "))

if (inp == 1):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print("Addition =",num1+num2)
elif (inp == 2):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print("Substraction =",num1-num2)
elif (inp == 3):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(f"Multlipication of {num1} * {num2} is =",num1*num2)
elif (inp == 4):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print("Division =",num1/num2)
elif (inp == 5):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print("Modulo =",num1%num2)
else:
    print("Invalid operational input")