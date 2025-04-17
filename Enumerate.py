list1 = [344,4234,5,2,"heoeo",5,3]
for x,y in enumerate(list1):
    print(f"Item at index {x} is {y}")

print("Using for loop in a list")
list2 = [1,2,3,4,5,6,7,8]
list3 = [i*i for i in list2]
print(list3)