class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Ahasanul")
print(Person.__dict__, end='\n\n')
print(p1.__dict__)









"""
    content:
        all init methode initialized attr will be added to the instance obj attr
    
    summary:

"""