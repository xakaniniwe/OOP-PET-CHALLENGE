class Pet:
    def __init__(self, name):
        """
        Initializes a new Pet object.

        Args:
            name (str): The name of the pet.
        """
        self.name = name
        self.hunger = 5  # Start with a moderate hunger level
        self.energy = 5  # Start with a moderate energy level
        self.happiness = 5  # Start with a moderate happiness level
        self.tricks = []  # Initialize an empty list to store learned tricks

    def eat(self):
        """
        Reduces the pet's hunger and increases happiness.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Yum!")

    def sleep(self):
        """
        Increases the pet's energy.
        """
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Zzz...")

    def play(self):
        """
        Decreases energy, increases happiness, and increases hunger.
        """
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing! Whee!")

    def get_status(self):
        """
        Prints the current status of the pet.
        """
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print("-------------------------\n")

    # Bonus 🎯
    def train(self, trick):
        """
        Teaches the pet a new trick and stores it in the tricks list.

        Args:
            trick (str): The name of the trick to teach.
        """
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        """
        Prints all the tricks the pet has learned.
        """
        if self.tricks:
            print(f"\n--- {self.name}'s Tricks ---")
            print(", ".join(self.tricks))
            print("-----------------------\n")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")