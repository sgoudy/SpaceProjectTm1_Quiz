# ─────────────────────────────────────────────
#  CLASS: EnemySpaceShip  (Destination / Target)
# ─────────────────────────────────────────────
import time


class EnemySpaceShip:
    """
    A target ship to be hacked and stolen.

    Attributes:
        name (str): Real ship name.
        codename (str): Your crew's alias for this target.
        location (str): Fictional location in the Milky Way.
        distance (float): Distance from Dottie in parsecs.
        defenses (int): Cyber defense rating 0–100%.
        cyber_topic (str): The cybersecurity domain protecting this ship.
    """

    def __init__(self, name: str, codename: str, location: str,
                 distance: float, cyber_topic: str):
        self.name = name
        self.codename = codename
        self.location = location
        self.distance = distance
        self.defenses = 100      # starts fully defended
        self.cyber_topic = cyber_topic

    def breach(self, amount: int = 25):
        """Lower defenses when a question is answered correctly."""
        self.defenses -= amount
        if self.defenses < 0:
            self.defenses = 0

    def is_taken(self):
        return self.defenses <= 0

    def summary(self):
        print(f"\n🎯 TARGET SHIP: {self.name}  [{self.codename}]")
        time.sleep(0.3)
        print(f"   Location  : {self.location}")
        time.sleep(0.3)
        print(f"   Distance  : {self.distance} parsecs from Dottie")
        time.sleep(0.3)    
        print(f"   Defenses  : {self.defenses}%")
        time.sleep(0.3)
        print(f"   Cyber Topic: {self.cyber_topic}\n")