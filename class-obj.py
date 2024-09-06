class Person:
    name="Akshat"
    occupation="Software Developer"
    
    #!Self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
    def info(self):
        print(f"{self.name} is a {self.occupation}")

ob=Person()
ob2=Person()
ob.name="Harshita"
ob.occupation="Railway Minister"
# print(ob.name)
ob.info()


ob2.name="Pingu"
ob2.occupation="Igloo Builder"
ob2.info()