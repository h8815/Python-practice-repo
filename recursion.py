def recurse(n):
    if (n<=0):
        return
    print(n)    # for 6 5 4 3 2 1
    recurse(n-1)   
    #print(n)   # for 1 2 3 4 5 6 
recurse(6)

# sum of n number 
''' def recurs(n): 
    if(n == 0):
        return 0
    return recurs(n-1)+n
sum = recurs(4)
print(sum) '''

# print list element using recursion
''' list1 = ['a', 'b', 'c', 'd']
def listel(list,index=0):
    if(index == len(list1)):
        return 0
    print(list[index],end=" ")  # for a b c d
    listel(list,index+1)
    # print(list[index],end=" ")   # for d c b a
listel(list1,0) '''