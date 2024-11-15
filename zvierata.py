
class Animal:
    total_weight = 0

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        Animal.total_weight += weight

    def look(self):
        print("the animal looks over there")

    def breathe(self):
        print("the animal takes a breath of fresh air")


class Fish(Animal):
    def swim(self):
        print("the fish swims")

    def run(self):
        print("the fish runs")


class Mammal(Animal):
    def run(self):
        print("the mammal runs")


class Bird(Animal):
    def fly(self):
        print("the bird flies")


class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print("the dog barks")

    def retrieve(self):
        print("the dog retrieves the ball")


class DomesticFish(Mammal, Fish):
    pass
# ked trieda dedi z dvoch tried a zdiela rovnaku metodu, zavola sa ktora je specifikovana ako prva (mammal)



#
#
#
animal1 = Animal(300, 11)
animal2 = Animal(420, 23)
animal3 = Animal(570, 300)

#
#
#

print(Animal.total_weight)

animals = [animal1, animal2, animal3]
for animal in animals:
    print(f"Zviera má {animal.age} rokov  a vazi {animal.weight}")