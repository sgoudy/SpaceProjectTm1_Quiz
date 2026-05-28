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
# instantiate all enemy ships
targets = [
        EnemySpaceShip("Enterprise",  "Top Gun",   "Planet Vulcan",       2.3,  "Network Security"),
        EnemySpaceShip("Eleanor",     "ANDROMEDA", "Planet Vega",         5.1,  "Encryption"),
        EnemySpaceShip("Tardis",      "Tesla",     "Jupiter's Moon: Io",  1.8,  "Social Engineering"),
        EnemySpaceShip("Serenity",    "Firefly",   "Saturn's Moon: Titan",1.2,  "Malware & Intrusion"),
    ]

def main():
    # texttime("\n" + "★" * 25)
    # texttime("       GONE IN 60 PARSECS")
    # texttime("       Space Heist | Hack or Be Hacked       ")
    # texttime("★" * 25)

    # --- Setup Homebase ---
    
    # --- Setup Player Ship ---
    player_ship = HackShip(
        name="The Phantom Byte",
        speed=4.2,
        capacity=6,
        weapons=["EMP Cannon", "Cyber Spike", "Signal Jammer"]
    )
    player_ship.summary()

   
        # --- Display Targets ---
    texttime("\n" + "─" * 25)
    texttime(" 📋 ACTIVE TARGETS ")
    texttime("─" * 25)
    for t in targets:
        t.summary()

    # --- Ship Selection Menu ---
    texttime("\n" + "─" * 25)
    texttime(" 🎮 SELECT YOUR TARGET ")
    texttime("─" * 25 + "\n\n")
    for i, t in enumerate(targets, 1):
        texttime(f"  {i}. {t.name} [{t.codename}] — {t.location} ({t.distance} parsecs) | Topic: {t.cyber_topic}\n")

    while True:
        choice = input("\n  Enter target number (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            selected = targets[int(choice) - 1]
            break
        texttime("\nInvalid choice. Please enter a number between 1 and 4.")

    # --- Run the Mission ---
    result = run_hack_mission(player_ship, selected)

    # --- Final Status ---
    texttime("\n" + "═" * 25)
    texttime(" 📊 GENERATING END OF MISSION REPORT ")
    texttime("═" * 25 + "\n")
    
    if result:
        texttime(f"\n  🎉 '{selected.name}' has been added to the Gone in 60 Parsecs fleet!\n")
        fleet.add_ship(selected)
        targets.remove(selected)  # Remove the captured ship from the target list
        fleet.summary()
        texttime(f"\n Would you like to attempt another mission? (y/n)")
        again = input("  > ").strip().lower()
        if again == 'y':
            main()  # Restart the game loop
        else:
            texttime("\n  🚀 Thanks for playing Gone in 60 Parsecs! Safe travels, space pirate! 🌌\n")
    else:
        texttime(f"\n  💀 Mission Failed. '{selected.name}' remains out of reach.")
        texttime(f"\nCurrent fleet status:")
        fleet.summary()
        texttime(f"\n  🔧 Return to Dottie for repairs and try again.")

if __name__ == "__main__":
    main()
