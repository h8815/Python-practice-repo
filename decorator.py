
def greet(fx):
    def modifier_function():
        fx()
        print("How are you")
        print("thankx for using this ")
    return modifier_function


@greet
def hello():
    print("Hello..!")

hello()