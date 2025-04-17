class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def addResult(self):
        print(f"{self.real}i + {self.img}j")
    
    def subResult(self):
        print(f"{self.real}i + {self.img}j")

    def __add__(self,num1):
        newReal = self.real + num1.real
        newImg = self.img + num1.img
        return Complex(newReal, newImg)
    
    def __sub__(self,num1):
        newReal = self.real - num1.real
        newImg = self.img - num1.img
        return Complex(newReal,newImg)

print("For addition :-") 
c1 = Complex(2,3)
c1.addResult()
c2 = Complex(5,6)
c2.addResult()
c3 = c1+c2
print(c3.addResult())

print("For substraction :-")
c1 = Complex(2,3)
c1.subResult()
c2 = Complex(5,6)
c2.subResult()
c3 = c1-c2
print(c3.subResult())