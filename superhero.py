class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This should be a list
        self.weakness = weakness
        self.energy_level = energy_level
        self.is_hero = True  # All instances are heroes by default

    def use_power(self, power_index):
        if self.energy_level <= 0:
            print(f"{self.name} is too exhausted to use powers!")
            return False
        
        if power_index < len(self.powers):
            power = self.powers[power_index]
            print(f"{self.name} uses {power}!")
            self.energy_level -= 10
            return True
        else:
            print(f"{self.name} doesn't have that power!")
            return False

    def rest(self):
        print(f"{self.name} is resting to regain energy...")
        self.energy_level = min(100, self.energy_level + 30)
        print(f"Energy level is now {self.energy_level}")

    def reveal_secret(self):
        print(f"{self.name}'s secret identity is {self.secret_identity}!")

    def _str_(self):
        return f"{self.name} - Powers: {', '.join(self.powers)} | Weakness: {self.weakness}"


# Inheritance example - A Villain is a type of Superhero (but is_hero is False)
class Villain(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100, evil_plan=""):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.is_hero = False
        self.evil_plan = evil_plan

    def use_power(self, power_index):
        # Villains use powers more aggressively
        if super().use_power(power_index):
            print("MUHAHAHA! Feel my power!")
            return True
        return False

    def reveal_evil_plan(self):
        print(f"{self.name}'s evil plan: {self.evil_plan}")


# Testing the classes
if __name__ == "__main__":
    # Create a hero
    spiderman = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web slinging", "Spider sense", "Wall climbing"],
        weakness="Ethyl chloride"
    )

    # Create a villain
    green_goblin = Villain(
        name="Green Goblin",
        secret_identity="Norman Osborn",
        powers=["Super strength", "Goblin glider", "Pumpkin bombs"],
        weakness="Insanity",
        evil_plan="To destroy Spider-Man!"
    )

    # Test methods
    print(spiderman)
    spiderman.use_power(0)  # Web slinging
    spiderman.use_power(2)  # Wall climbing
    spiderman.reveal_secret()

    print("\n")

    print(green_goblin)
    green_goblin.use_power(1)  # Goblin glider
    green_goblin.reveal_evil_plan()
    green_goblin.reveal_secret()