# A standard function "a_function" that prints a message when called
def a_function():
    print("This is a standard function, to be called by its name, followed by parentheses")


# This creates a new Class called AClass, which has an initialization function __init__ that runs when the class is initialized
class AClass:
    def __init__(self):
        print("This is an initialization function inside a Class")
        self.a = "this prints when you call a_class.a"


# This will call the function and print the message inside it
a_function()


# Initialize the class, which will call the __init__ function and print the message inside it
a_class = AClass()


# To Print the value of a, we can call it using the class instance followed by a dot and the variable name
print(a_class.a)