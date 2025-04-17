def func(num):
    try:
        print(f"Table of {num} is:")
        for val in range(1,11):
            print(f"{int(num)} X {val} = {int(num)*val}")
        return 0            # Using return means finally will execute but  else not
    except ValueError as v:
        print(v)
    
    else:
        print("Else will execute when there is no error but if we return any thing it wont execute")
    finally:
        print("Finally will execute at any condition whatever their is any return in a function or not")
        
num = eval(input("Enter number : "))
func(num)