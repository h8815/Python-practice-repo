# checking version
# import sys
# print(f"version - {sys.version} \nversion info - {sys.version_info}")
# ----------------------------------------------------------------------------

# printing date and time
# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# ----------------------------------------------------------------------------

# using math module
# from math import pi
# r = float(input("Enter radius : "))
# area = pi*r**3
# print("area - ",area)
# ----------------------------------------------------------------------------

# reverse full string
# name = input("Enter full name : ")
# rev = name[::-1]
# print(rev)
# ----------------------------------------------------------------------------

# generating list and tuple using comma seperated value
# val = input("Enter comma saparated value: ")
# list = val.split(",")
# tuple = tuple(list)
# print("List - ",list)
# print("Tuple - ",tuple)
# ----------------------------------------------------------------------------

# printing extention any input file
# ext = input("Enter file name : ")
# extention = ext.split(".")
# print("The extention of file is :",extention[-1])
# ----------------------------------------------------------------------------

# printing first and last color
# color = ["red", "black", "white", "blue", "green"]
# print(f"List - {color}\nFirst color : {color[0]} \nLast color : {color[-1]}")
# ----------------------------------------------------------------------------

# using placeholder in tuple 
# exam_date = (11,12,2023)
# print("Exam on : %a/%a/%a"%exam_date)
#                ^placeholder
# ----------------------------------------------------------------------------
# printing in the  format of n+nn+nnn
# value = int(input("Enter value : "))
# num1 = int("%s"%value)
# num2 = int("%s%s"%(value,value))
# num3 = int("%s%s%s"%(value,value,value))
# print(num1+num2+num3)
# ----------------------------------------------------------------------------

# using calender module 
# import calendar
# year = int(input("Enter year : "))
# month = int(input("Enter month : "))
# print(calendar.month(year,month,5))
# ----------------------------------------------------------------------------

# gap between dates 
# from datetime import date
# first_date = date(2004,7,17)
# last_date = date(2025,7,17)
# diff_date = first_date - last_date 
# print(diff_date.days)
# ----------------------------------------------------------------------------

# spare Volume = 4/3 π r³
# from math import pi
# print(pi)
# radius = int(input("Enter radius : "))
# volume = 4/3*(pi*radius**3)
# print(volume)
# ----------------------------------------------------------------------------

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
# def difference(n):
#     if (n > 17):
#         return ((n-17)*2)
#     else:
#         return (17-n)
    
# num = int(input("Enter number : "))
# print(difference(num))
# ----------------------------------------------------------------------------

# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# num = int(input("Enter number : "))
# t = True
# f = False

# if (abs(1000 - num) <= 100 or abs(2000 - num) <= 100):
#     print(t)
# else:
#     print(f)
# ----------------------------------------------------------------------------

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))
# calculate = num1+num2+num3
# if (num1 == num2 == num3):
#     print(calculate*3)
# else:
#     print(calculate)
# ----------------------------------------------------------------------------

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
# def ISorNOT(word):
#     if ((word[:1] == "I","i") and word[1:2] == "s" ):
#         print(word)
#     else:
#         print(f"is{word}")
# w = input("Enter any word : ")
# ISorNOT(w)
# ----------------------------------------------------------------------------

# Write a Python program to count the number 4 in a given list.
# list1 = [1,2,3,4,4,5,4,3,4,3,2]
# num = int(input("Enter value you need to count : "))
# count = 0
# for i in list1:
#     if(i == num):
#         count+=1
# print("Count =",count)
# ----------------------------------------------------------------------------

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2
# def lessthan2(str,n):
#     if (len(str) < 2):
#         return (str*n)
#     else:
#         return str[:2]*n
    
# str = input("Enter string : ")
# n = int(input("Enter no.of copies you want : "))
# print(lessthan2(str,n))
# ----------------------------------------------------------------------------

# vowel or conconant
# def vowelORnot(str):
#     if (str == "a","i","o","u","e"):
#         print(f"{str} is a vowel")
#     else:
#         print(f"{str} is a conconant")
# s = input("Enter any letter: ")
# vowelORnot(s)
# ----------------------------------------------------------------------------

# Write a Python program that checks whether a specified value is contained within a group of values
# def value(num,search):
#     for i in num:
#         if (i == search):
#             return True
#     return False

# search = int(input("Enter word you need to search: "))
# num = [1,2,3,4,5,6,7]
# print(value(num,search))
# ----------------------------------------------------------------------------

#  List to String Concatenator
# list1 = [1,2,22,3,4]
# print(list1)
# for i in list1:
#     print(i,end="")


#  Even Numbers Until 237
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for i in numbers:
#     if(i == 237):
#         break
#     elif(i%2==0):
#         print(i)


#  Unique Colors Finder
# color1 = set(["Red", "Blue", "Green", "Black"])
# color2 = set(["Red", "Green", "White"])
# print(f"color1 - {color1}\ncolor2 - {color2}")

# print(f"Difference from color1 and color2 : {color1.difference(color2)}")
# print(f"Difference from color2 and color1 : {color2.difference(color1)}")


# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# def two_value(x,y,z):
#     if x==y==z:
#         return x+y+z
#     elif x==y or y==z or x==z:
#         return 0
#     else:
#         return x+y+z
        
# print(two_value(2,3,2))
# print(two_value(2,2,2))
# print(two_value(1,2,2))


#Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
# def btw20_25(x,y):
#     sum = x+y
#     if sum in range(15,20+1):
#         return 20
#     else:
#         return sum
    
# print(btw20_25(15,0))


#Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
# def sum_diff(x,y):
#     sum = x+y
#     diff = x-y
#     if (x==y or sum == 5 or diff == 5):
#         return True
#     else:
#         return False

# print(sum_diff(2,2))
# print(sum_diff(7,2))
# print(sum_diff(1,2))


#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
# def occurance(num):
#     print("Original list -",num)
#     return num.count(19) == 2 and num.count(5) >=3

# list1 = [19,19,2,3,2,5,5,6,4,5]
# list2 = [2,3,4,2,3,5,2]

# print(f"Checking the occurance of 19 and 5 - {occurance(list1)}")
# print(f"Checking the occurance of 19 and 5 - {occurance(list2)}")


# Write a Python program to add two objects if both objects are integers.
# def is_integer(val1,val2):
#     if not (isinstance(val1, int) and isinstance(val2, int)):
#         return "Inputs are not integer"
#     else:
#         return val1+val2

# print(is_integer(20,29))
# print(is_integer(20,29.02))
# print(is_integer(20,"abc"))

