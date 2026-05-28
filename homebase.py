# ─────────────────────────────────────────────
#  CLASS: Homebase
# ─────────────────────────────────────────────
class Homebase:
    """
    Represents your team's base of operations.

    Attributes:
        name (str): Name of the homebase.
        location (str): Where the homebase is located.
        SOB (int): Soles on Board — number of crew at base.
    """

    def __init__(self, name: str, location: str, SOB: int):
        self.name = name
        self.location = location
        self.SOB = SOB

    def summary(self):
        print(f"\n🪨  HOMEBASE: {self.name}")
        print(f"   Location : {self.location}")
        print(f"   Soles on Board: {self.SOB} crew members")

