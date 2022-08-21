from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name
    
    def register_do_work(self, func):
        setattr(self, "_do_work", MethodType(func, self))

    def do_work(self):
        do_work_methode = getattr(self, "_do_work", None)

        if do_work_methode:
            return do_work_methode()
        else:
            raise AttributeError("instance must have do_work methode using register_do_work().")

p1 = Person("Eric")
p2 = Person("Alex")

print(p1.__dict__)
print(p2.__dict__) 

def say_hello(self):
    print(f'{self.name} says hello!')

p1.say_hello = MethodType(say_hello, p1)           # assing a function as methode attr
p2.say_hello = MethodType(lambda self: print(f'{self.name} not interested'), p2)          # assing a lambda func as methode attr

print(p1.__dict__)
print(p2.__dict__) 

p1.say_hello()
p2.say_hello()

math_teacher = Person("Ahasan")
english_teacher = Person("John")
art_teacher = Person("Charus")

def work(self):
    return f'{self.name} will teach Algebra today.'


math_teacher.register_do_work(work)
def work(self):
    return f'{self.name} will teach Translation today.'
english_teacher.register_do_work(work)

teachers = [math_teacher, english_teacher, art_teacher]

for teacher in teachers:
    if hasattr(teacher, "_do_work"):
        print(teacher.do_work())
    else:
        print(f'{teacher.name} has no work to do today!')





"""
    content:
        first of all "impoort MethodeType from types" to bind a function to a object
    
    summary:

"""