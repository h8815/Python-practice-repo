# class Cars:
#     @staticmethod
#     def BMW(car1,car2):
#         print(f"I owe two cars\n1.{car1}\n2.{car2}")

# c1 = Cars()
# c1.BMW("As","ASA")          # Using object
# Cars.BMW("BMW","GT")        # Without using object


class MyClass:
    
    @staticmethod
    def get_max_value(x, y):
        return max(x, y)

# Create an instance of MyClass
obj = MyClass()

print(MyClass.get_max_value(20, 30))  # Using class
print(obj.get_max_value(20, 30))