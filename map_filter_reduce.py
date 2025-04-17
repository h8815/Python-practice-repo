# Map function 
def cube(x):
    return x*x*x
list1 = [1,2,3,4,5]
maplist = map(cube,list1)
print("List =",list1)
print(f"List using map function : {list(maplist)}")


# Filter function
def greater(x):
    return x>2
filterlist = filter(greater,list1)
print(f"List using filter function : {list(filterlist)}")


# Reduce function
from functools import reduce
def mysum(x,y):
    return x*y

list1 = [1,2,3,4,5]
sum = (reduce(mysum,list1))
print(sum)