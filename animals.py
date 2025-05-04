class Animal:
    def _init_(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs happily on four legs! 🐕")
    
    def speak(self):
        print(f"{self.name} says: Woof! Woof!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims gracefully through the water! 🐟")
    
    def speak(self):
        print(f"{self.name} says: Blub blub...")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies high in the sky! 🦅")
    
    def speak(self):
        print(f"{self.name} says: Tweet tweet!")

class Snake(Animal):
    def move(self):
        print(f"{self.name} slithers silently across the ground! 🐍")
    
    def speak(self):
        print(f"{self.name} says: Hisssss...")

# Function demonstrating polymorphism
def animal_concert(animals):
    for animal in animals:
        animal.move()
        animal.speak()
        print("---")

# Testing the classes
if __name__ == "__main__":



    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Sky"),
        Snake("Viper")
    ]

    animal_concert(animals)