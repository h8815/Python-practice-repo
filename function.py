#length of a list 
''' def lenOFlist(list):
    return len(list)

list1 = [1,2,3,4,5,2,113,31,2]
result = lenOFlist(list1)
print(result) '''

#element of list in single line
''' work = ["doctor", "CA", "CS", "Engineer", "CMA", "Teacher"]

def inline1(list):
    for i in list:
       print(i,end=" ")
inline1(work) '''

#factorial on n number 
''' def factorial(n):
    product = 1
    i=1
    while i<=n:
        product *=i
        i+=1
    print(product)
factorial(5) '''

#usd to inr
''' def usdTOinr(inr):
    return inr*86.54
usd = int(input("Enter USD : "))
TO_inr = usdTOinr(usd)
print(f'value of {usd} USD is {TO_inr:.3f} INR') '''

#odd and even function
def oddANDeven(num):
    if (num%2 == 0):
        print("EVEN")
    else:
        print("ODD")
        
number = int(input("Enter number : "))
oddANDeven(number)