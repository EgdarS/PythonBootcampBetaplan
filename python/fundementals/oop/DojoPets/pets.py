class Pets:
    def __init__(self,name,type,tricks,health, energy):   # Encapsulation
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep(self):
        self.energy=self.energy + int(25)
        print('Your pets energy was increased by 25!')
        return self
    def eat(self,treats):
        self.energy=self.energy +int(treats*5)
        self.health=self.health +int(treats*10)
        print(f"Your pets health was incread by 10*{treats} and it's energy by 5*{treats}!")
        return self
    def play(self):
        self.health=self.health +(5)
        print('Your pets health was increased by 5!')
        return self
    def noise(self,pet):
        print('Pet sounds')

dog=Pets('Bella','Labrador','Jumping',0,0)
# Puppy is a subclass of Pets that gets all 5 attributes from Pets class and has a different extra attribute named age(Inheritance)
class Puppy(Pets):
    def __init__(self,name,type,tricks,health,energy,age):
        super().__init__(name,type,tricks,health,energy)
        self.age=age
#Polymorphism
    def noise(self,Puppy):
        super().noise(Puppy)
        print('Puppy sounds')
    def noise(self,pet):
        print(f'{pet} sounds')