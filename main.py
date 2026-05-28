"""@title: main.py
Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""
from hackship import HackShip
# import random
import random   
from mission import run_hack_mission
from quiz import QUESTION_BANK
from enemySS import EnemySpaceShip
from homebase import Homebase   
from animation import texttime, slow_progress_bar
# from timer import countdown
from fleet import fleet

    # countdown(60)  # Start the mission timer (10 minutes)
# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────
def main():
    # texttime("\n" + "★" * 55)
    # texttime("       GONE IN 60 PARSECS")
    # texttime("       Space Heist | Hack or Be Hacked       ")
    # texttime("★" * 55)

    # --- Setup Homebase ---
    dottie = Homebase("Dottie", "Asteroid near Pluto, Milky Way", 12)
    dottie.summary()

    # --- Setup Player Ship ---
    player_ship = HackShip(
        name="The Phantom Byte",
        speed=4.2,
        capacity=6,
        weapons=["EMP Cannon", "Cyber Spike", "Signal Jammer"]
    )
    player_ship.summary()

    # --- Setup Target Ships ---
    targets = [
        EnemySpaceShip("Enterprise",  "Top Gun",   "Planet Vulcan",       2.3,  "Network Security"),
        EnemySpaceShip("Eleanor",     "ANDROMEDA", "Planet Vega",         5.1,  "Encryption"),
        EnemySpaceShip("Tardis",      "Tesla",     "Jupiter's Moon: Io",  1.8,  "Social Engineering"),
        EnemySpaceShip("Serenity",    "Firefly",   "Saturn's Moon: Titan",1.2,  "Malware & Intrusion"),
    ]

    print("\n\n📋  ACTIVE TARGETS")
    print("─" * 55)
    for t in targets:
        t.summary()

    # --- Ship Selection Menu ---
    print("\n\n🎮  SELECT YOUR TARGET")
    print("─" * 55)
    for i, t in enumerate(targets, 1):
        print(f"  {i}. {t.name} [{t.codename}] — {t.location} ({t.distance} parsecs) | Topic: {t.cyber_topic}")

    while True:
        choice = input("\n  Enter target number (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            selected = targets[int(choice) - 1]
            break
        print("  Invalid choice. Enter 1, 2, 3, or 4.")

    # --- Run the Mission ---
    result = run_hack_mission(player_ship, selected)

    # --- Final Status ---
    print("\n📊  END OF MISSION REPORT")
    print("─" * 55)
    player_ship.summary()
    selected.summary()
    ourFleet = fleet()
    if result:
        print(f"\n  🎉 '{selected.name}' has been added to the Gone in 60 Parsecs fleet!")
        ourFleet.add_ship(selected)
    else:
        print(f"\n  🔧 Return to Dottie for repairs and try again.")
        print(f" Your fleet is sad. 😢 \n {ourFleet.summary}")

if __name__ == "__main__":
    main()
