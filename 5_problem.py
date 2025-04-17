with open("Table.txt", "a") as f:
    num = int(input("Enter number : "))
    table = [i*num for i in range(1,11)]
    f.write(f"Table of {num} = {str(table)}\n")