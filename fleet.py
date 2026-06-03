"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  CLASS: Fleet
# ─────────────────────────────────────────────

from animation import texttime
from console_utils import banner

class Fleet():
    """
    A class to represent a fleet of spaceships.
    Attributes:
    ships (list): A list to hold the spaceships in the fleet.
    """
    def __init__(self):
        """Initializes the Fleet with an empty list of ships."""
        self.ships = []
    
    def add_ship(self, ship):
        """Adds a ship to the fleet."""
        self.ships.append(ship)
    
    def summary(self):
        """Prints a summary of the fleet's current status."""
        print(banner("🚀 YOUR CURRENT FLEET STATUS"), end="")
        print("\n")
        for ship in self.ships:
            texttime(f" 🚀 {ship.name}\n")

fleet = Fleet()