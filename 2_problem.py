# print element of a list at index 2,4,6
num = [1,2,3,4,5,6,7,8]
for index,item in enumerate(num):
    if index == 2 or index == 4 or index == 6:
        print(f"Value at index {index} is {item}")