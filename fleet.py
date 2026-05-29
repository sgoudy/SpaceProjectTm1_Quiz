# Create a fleet of one spaceship to begin with. As we answer questions correctly, we can add those ships to our fleet. Each ship will have its own unique attributes and capabilities.

class Fleet():
    def __init__(self):
        self.ships = []
    
    def add_ship(self, ship):
        self.ships.append(ship)
    
    def summary(self):
        print("\n🚀  YOUR FLEET")
        print("─" * 55)
        for ship in self.ships:
            print(f"  {ship.name}\n")

fleet = Fleet()