class MyClass:

    def say_hello(self):
        print("Hello World")

obj = MyClass()

print(MyClass.say_hello)
print(obj.say_hello)

MyClass.say_hello()
obj.say_hello()



"""
    content:
        type(CLASS.FUNCTION attr) == FUNCTION // bound to nothing
        type(INSTANCE.FUNCTION attr) == METHODE // bound to the INSTANCE and pass it by default as SELF
    
    summary:
        Function that are defiend in class are transformed into methode when they are called from a instance of that class
        If we add a FUNCTION attr in the INSTANCE it will just be a FUNCTION of that INSTANCE
"""