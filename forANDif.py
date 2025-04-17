# taking input from user in list using for loop

list1 = []
list2 = []
a = int(input("Enter range of the list :"))
print("\nEnter element of list1 :-")
for i in range(a):
    list1.append(input(f"Enter {i} index element :"))
print("\nEnter element of list2 :-")
for i in range(a):
    list2.append(input(f"Enter {i} index element :"))
print(f"\nlist1 ={list1}\nlist2 ={list2}")
if (list1[0] == list1[-1]):
    print("\nThe first and last element of list1 are same")
elif (list2[0] == list2[-1]):
    print("\nThe first and last element of list2 are same")
else:
    print("\nnot same in both list")
