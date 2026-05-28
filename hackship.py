# ─────────────────────────────────────────────
#  CLASS: HackShip  (your Vehicle / Asset)
# ─────────────────────────────────────────────
class HackShip:
    """
    Your personal heist ship launched from Dottie.

    Attributes:
        name (str): Ship name.
        speed (float): Speed in parsecs per hour.
        capacity (int): Max crew it can carry.
        hull (int): Hull integrity 0–100%. Damaged by wrong answers.
        weapons (list): List of weapons loadout.
    """

    def __init__(self, name: str, speed: float, capacity: int, weapons: list):
        self.name = name
        self.speed = speed
        self.capacity = capacity
        self.hull = 100          # starts at full health
        self.weapons = weapons

    def take_damage(self, amount: int = 25):
        """Reduce hull integrity when a question is answered wrong."""
        self.hull -= amount
        if self.hull < 0:
            self.hull = 0

    def is_destroyed(self):
        return self.hull <= 0

    def summary(self):
        print(f"\n🚀  HACK SHIP: {self.name}")
        print(f"   Speed    : {self.speed} parsecs/hr")
        print(f"   Capacity : {self.capacity} crew")
        print(f"   Hull     : {self.hull}%")
        print(f"   Weapons  : {', '.join(self.weapons)}")
