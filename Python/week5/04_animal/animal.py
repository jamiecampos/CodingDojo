class Animal(object):
    def __init__ (self, name, health = 100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print "Walking."
        return self

    def run(self):
        self.health -= 5
        print "Running."
        return self

    def displayHealth(self):
        print "Name: " + self.name + ", Health: " + str(self.health)
        return self

animal = Animal("Animal")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        print "Petting."
        return self

dog = Dog("Dog")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        print "This is a dragon!"
        return self

dragon = Dragon("Dragon")
dragon.walk().walk().walk().run().run().fly().displayHealth()
