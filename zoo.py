from tokenize import Name
from unicodedata import name

class zoo:
    def __init__(self,name) -> None:
        pass

    def feed(self,num):
        self.hp+=10*num
        self.sad-=2*num
        return self

    def display(self):
        print( self.name, self.hp ,self.sad)
        return self

class animal(zoo):
    def __init__(self):
        pass

class lion(animal):
    def __init__(self,name,hp=100,sad=80):
        self.name=name
        self.hp=hp
        self.sad=sad

class Taiger(animal):
    def __init__(self,name,hp=50,sad=40) :
        self.name=name
        self.hp=hp
        self.sad=sad

class cheetah(animal):
    def __init__(self,name,hp=30,sad=90):
        self.name=name
        self.hp=hp
        self.sad=sad


Fahad = lion("Fahad")
scar = Taiger("scar")
useless = cheetah("useless")


Fahad.feed(2).display()
scar.feed(5).display()
useless.feed(10).display()
