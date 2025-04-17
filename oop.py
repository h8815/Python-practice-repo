# class Student:
#     def __init__(self):
#         print("Hello")
        
#     def __init__(self,name,age = 0):  #constructor 
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"   
# p1 = Student("alice")       # First Object(p1) 
# print(p1.name)
# print(p1)
# p2 = Student("Ajit")        # Second Object(p2)
# print(p2.name)


#use of methods(function that belong to class) here date is a method  
# class Student:
#     def __init__(self,age):
#         self.age = age

#     def date(self):
#         print(f"my age is {self.age}")

# age = int(input("Enter age :"))
# s1 = Student(age)
# s1.date()

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = 0
        for val in self.marks:
            avg += val   
        print(f"{self.name}'s average - {avg/3:.2f}")

s1 = Student("Ajit",[97,98,99])
s1.average()