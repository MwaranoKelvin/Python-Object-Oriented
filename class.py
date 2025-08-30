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
         return f"{self.name} - Power: {self.power}, Strength: {self._strength}, Energy: {self._energy}%"
    
class FlyingHero(Superhero):
        """Subclass for heroes who can fly."""
        def __init__(self, name, power, strength = 50, max_altitude = 1000):
            super().__init__(name, power, strength)
            self.max_altitude = max_altitude
        def fly(self):
            """Fly if enough energy is available."""
            if self._energy >= 15:
               self._energy -= 15
               return f"{self.name} soars through the sky! Max altitude: {self.max_altitude}ft"
            return f"{self.name} needs more energy to fly."
        def use_power(self):
             """Override: flying heroes use less energy."""
             if self._energy >= 15:
                 self._energy -= 15
                 return f"{self.name} uses {self.power} while flying!"
             return f"{self.name} is too tired to use {self.power}."

class TechHero(Superhero):
    """Subclass for technology-based heroes."""
    
    def __init__(self, name, power, strength=50, gadgets=None):
        super().__init__(name, power, strength)
        self.gadgets = gadgets or ["Scanner", "Communicator"]
    
    def use_gadget(self, gadget_name):
        """Activate a gadget if the hero owns it."""
        if gadget_name in self.gadgets:
            return f"{self.name} activates {gadget_name}."
        return f"{self.name} doesn't have {gadget_name}."


# ============= Part 2: Assignment 2: Polymorphism Challenge - Vehicles =============#
class Vehicle:
    """Base class for vehicles."""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        """Generic move method (to be overridden)."""
        return f"{self.name} is moving at {self.speed} mph."


class Car(Vehicle):
    """Car-specific implementation of move."""
    
    def move(self):
        return f"{self.name} is driving on the road at {self.speed} mph."


class Plane(Vehicle):
    """Plane-specific implementation of move."""
    
    def move(self):
        return f"{self.name} is flying at {self.speed} mph."


class Boat(Vehicle):
    """Boat-specific implementation of move."""
    
    def move(self):
        return f"{self.name} is sailing at {self.speed} mph."


class Bicycle(Vehicle):
    """Bicycle-specific implementation of move."""
    
    def move(self):
        return f"{self.name} is pedaling at {self.speed} mph."


# ==== Demonstration and Testing ====#

def main():
    print("=" * 60)
    print("SUPERHERO CLASS DEMO")
    print("=" * 60)
    
    # Create superhero objects
    hero1 = Superhero("Captain Thunder", "Lightning Strike", 75)
    hero2 = FlyingHero("Sky Guardian", "Wind Blast", 60, 5000)
    hero3 = TechHero("Cyber Knight", "Data Hack", 55, ["Scanner", "Shield", "Laser"])
    
    # Demonstrate hero functionality
    heroes = [hero1, hero2, hero3]
    
    for hero in heroes:
        print(f"\n{hero.get_stats()}")
        print(hero.use_power())
        
        # Subclass-specific abilities
        if isinstance(hero, FlyingHero):
            print(hero.fly())
        elif isinstance(hero, TechHero):
            print(hero.use_gadget("Shield"))
        
        print(hero.rest())
    
    print("\n" + "=" * 60)
    print("POLYMORPHISM DEMO - VEHICLES")
    print("=" * 60)
    
    # Create vehicle objects
    vehicles = [
        Car("Tesla Model 3", 120),
        Plane("Kenya Airways 747", 550),
        Boat("Speed Yacht", 45),
        Bicycle("Mountain Bike", 25)
    ]
    
    # Demonstrate polymorphic move() calls
    print("\nPolymorphic move() outputs:")
    for vehicle in vehicles:
        print(vehicle.move())


if __name__ == "__main__":
    main()


    