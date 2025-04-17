
line = int(input("Enter the number of lines : ")) 
for i in range(1,line+2):
    for k in range(line,i-1,-1):
        print(end=" ")
    for j in range(1,i):
        print(end="* ")
    print("")
for a in range(1,line):
    for k in range(0,a):
        print(end=" ")
    for b in range(line,a,-1):
        print(end="* ")
    print("")