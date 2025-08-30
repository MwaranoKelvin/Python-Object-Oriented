"""
Object-Oriented Programming Demo
Part 1: Class Design with Inheritance
Pary 2: Polymorphism Challenge
"""
# ============= Part 1: Designing the Class =============#
class Superhero: 
    """Base class representing a superhero with basic attributes and methods."""
    def __init__(self, name, power, strength = 50):
        self.name = name
        self.power = power
        self._strength = strength #Encapsulated attribute
        self._energy = 100 # Energy level starts at 100

    def use_power(self):
         """Use the hero's special power. Consumes energy."""
         if self._energy >= 20:
             self._energy -= 20
             return f"{self.name} uses {self.power}!"
         return f"{self.name} is too tired to use {self.power}."
    
    def rest(self):
        """Restore some energy by resting."""
        self._energy = min(100, self._energy + 30)
        return f"{self.name} rested. Energy is now: {self._energy}%"
    def get_stats(self):
         """Return current stats for the hero."""
    