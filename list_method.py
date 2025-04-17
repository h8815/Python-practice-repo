# changing list items 
list1 = ["Apple","Kiwi","Banana"]
list1[0] = "Watermalon"
print(list1,"\n")

#changing the range of items
list2 = ["Apple","Kiwi","Banana","Watermalon","Kela","Cherry"]
list2[1:3] = ["Pineaple"]  #Pineaple will replace Kiwi and Banana
print(list2,"\n")

#insert items
list3 = ["Apple","Kiwi","Banana"]
list3.insert(0,"Cherry")
print(list3,"\n")

#append item
list4 = ["Apple","Kiwi","Banana"]
list4.append("Cherry")
print(list4,"\n")

#extend items
list5 = ['a','b','c','d']
list6 = ['e','f','g','h']
list5.extend(list6)
print(list5,'\n')

#removing specific item
list7 = ["Apple","Kiwi","Banana"]
list7.remove("Apple")
print(list7,'\n')

#removing item using index number
list8 = ["Apple","Kiwi","Banana"]
list8.pop(0)
print(list8,'\n')

#using delete(del) keyword 
list9 = ["Apple","Kiwi","Banana"]
del list9[0]
print(list9,'\n')