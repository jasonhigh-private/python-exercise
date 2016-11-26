class Person:
    Name = "Default Name"
    def Print(self):
        print("My Name is {0}".format(self.Name))


p1 = Person()
p1.Print()