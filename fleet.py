# Create a fleet of one spaceship to begin with. As we answer questions correctly, we can add those ships to our fleet. Each ship will have its own unique attributes and capabilities.
from animation import texttime

class Fleet():
    def __init__(self):
        self.ships = []
    
    def add_ship(self, ship):
        self.ships.append(ship)
    
    def summary(self):
        print("\n" + "═" * 31+"   🚀  YOUR CURRENT FLEET STATUS    "+"═" * 31 + "\n")
        for ship in self.ships:
            texttime(f" 🚀 {ship.name}\n")

fleet = Fleet()