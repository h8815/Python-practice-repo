# Single level inheritance
# class Parent :
#     def hello(self):
#         print("Hello, I am in Parent class")
# class child(Parent):
#     pass
# p1 = child()
# p1.hello()

#Multi-level inheritance
# class Base:
#     car = "BMW"
#     def __init__(self):
#         print("I own")
# class child(Base):
#     def pri():
#         print("I am derive class")
# class Derived(child):
#     pass

# d1 = Derived()
# print(d1.car)

# Multiple inheritance
class A:
    varA = ("I am A class")
class B:
    varB = ("I am B class ")
class C(A,B):
    varC = ("I am C class")
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)