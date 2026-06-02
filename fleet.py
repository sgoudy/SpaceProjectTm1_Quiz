"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  CLASS: Fleet
# ─────────────────────────────────────────────

from animation import texttime

class Fleet():
    """
    A class to represent a fleet of spaceships.
    Attributes:
    ships (list): A list to hold the spaceships in the fleet.
    """
    def __init__(self):
        self.ships = []
    
    def add_ship(self, ship):
        self.ships.append(ship)
    
    def summary(self):
        print("\n" + "═" * 31+"   🚀  YOUR CURRENT FLEET STATUS    "+"═" * 31 + "\n")
        for ship in self.ships:
            texttime(f" 🚀 {ship.name}\n")

fleet = Fleet()