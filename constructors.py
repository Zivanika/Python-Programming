class Person:
    def __init__(self,n,o):
        print("Hey I am a constructor")
        self.name=n
        self.occ=o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
# a=Person()
# b=Person() #required positional arguments n and o

c=Person("Akshat","SDE") #1st arg is object itself rest are paramenters
c.info()
