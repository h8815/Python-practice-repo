# # creating and writing in practice.txt
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using Java\nI like programming in Java.")

# # reading practice.txt
# with open("practice.txt", "r") as f:
#     str = f.readline()

# # replacing Java with Python
# data = str.replace("Java", "Pyhton")

# # saving it into the practice.txt
# with open("practice.txt", "w") as f:
#     f.write(data)


# # searching "learning" at what index it is present in a file or not
# with open("practice.txt", "r") as f:
#     str = f.readline()
# presentORnot = str.find("learning")
# if (presentORnot != -1):
#     print(f"Found at {presentORnot} indexs")
# else:
#     print("Not found")

# #checking for "learning" present in practice.txt or not
# with open("practice.txt", "r") as f:
#     str = f.read()
# if "learning" in str:
#     print("Found")
# else:
#     print("Not found")

# #checking for line in which "learning" present using function
# def checking_line():
#     word = input("Enter word you want to found : ")
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(f"{word} found at line no.{line_no}")
#             else:
#                 print(f"Not found at line no.{line_no}")
#             line_no+=1

# checking_line()


# checking even number in word.txt 
count = 0
even_list = []
with open("word.txt", "r") as f:
    data = f.read()
num = data.split(",")
print(num)
for i in num:
    if (int(i)%2==0):
        even_list.append(i)
        count+=1
print("Even number list : ",even_list)
print(f"total no.of even number is : {count}")