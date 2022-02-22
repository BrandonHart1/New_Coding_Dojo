class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self, pet):
        self.play.noise






# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self, pet):
        self.eat





# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self, pet):
        self.noise()





class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy


# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25




# eat() - increases the pet's energy by 5 & health by 10
    def eat(self, pet):
        self.energy += 5
        self.health += 10


# play() - increases the pet's health by 5
    def play(self, pet):
        self.health += 5



# noise() - prints out the pet's sound
    def noise(self, pet):
        print("Ruff, ruff, ruff")






major = Pet("Major", "Dog", "Running down a ball", 90, 75)

ninja_1 = Ninja("John", "Smith", "Any Treat in Sight", "Merrick", major)


# kuma = Pet("Kuma", "Dog", "Chasing birds", 90, 90)