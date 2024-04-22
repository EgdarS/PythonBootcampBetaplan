from pets import Pets

class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food
        self.Pets=Pets('Bella','Labrador','Jumping',0,0)

    def walk(self):
        self.Pets.play()
        return self
    def feed(self):
        self.Pets.feed()
        return self
    def bathe(self):
        self.Pets.noise
        print('Dog noise!')
        return self
    
andy=Ninja('Andy','Ding','dog','treats','dog food')

# andy.bathe()
# andy.walk()
# andy.feed(int(input('Enter number of treats: ')))  #not finished yet