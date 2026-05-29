"""@title: main.py
Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""
import time
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
from datetime import datetime
from intro import intro_scroll
from datetime import datetime



# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────


mission_time = None  # Global variable to track mission start time

def main():
    texttime("\n" + "★" * 25)
    texttime("       GONE IN 60 PARSECS >> Space Heist | Hack or Be Hacked       ")
    texttime("★" * 25+"\n\n")

    intro_scroll()

    # --- Setup Homebase ---
    texttime("\n\n   ...Initializing Dottie's Homebase...\n")
    dottie = Homebase("Dottie", "Asteroid near Pluto, Milky Way", 12)
    texttime(dottie.summary())


    # --- Setup Player Ship ---
    player_ship = HackShip(name="The Phantom Byte",speed=4.2,capacity=6,weapons=["EMP Cannon", "Cyber Spike", "Signal Jammer"]    )
    texttime(player_ship.summary())

   
    # --- Display Targets ---
    # instantiate all enemy ships
    targets = [
            EnemySpaceShip("Enterprise",  "Top Gun",   "Planet Vulcan",       2.3,  "Network Security"),
            EnemySpaceShip("Eleanor",     "ANDROMEDA", "Planet Vega",         5.1,  "Encryption"),
            EnemySpaceShip("Tardis",      "Tesla",     "Jupiter's Moon: Io",  1.8,  "Social Engineering"),
            EnemySpaceShip("Serenity",    "Firefly",   "Saturn's Moon: Titan",1.2,  "Malware & Intrusion"),
        ]

    texttime("\n" + "─" * 25 +" 📋 ACTIVE TARGETS >> WHO SHOULD WE ATTACK? "+"─" * 25 +"\n")
    for t in targets:
        t.summary()


    while True:
        startTime = datetime.now()
        choice = input("\n  Enter target number (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            selected = targets[int(choice) - 1]
            # make note of the time when the mission starts, so we can calculate total mission duration at the end
           

            # Get current time
            
            break

        texttime("\nInvalid choice. Please enter a number between 1 and 4.")

    # --- Run the Mission ---
    start_time = datetime.now()

    result = run_hack_mission(player_ship, selected)

    # --- Final Status ---
    texttime("\n" + "═" * 25+" 📊 GENERATING END OF MISSION REPORT "+"═" * 25 + "\n")
    
    if result:
        # mission_duration = datetime.now() - startTime
        # texttime(f"  Mission Duration: {mission_duration:.2f} seconds\n")
        texttime(f"\n  🎉 '{selected.name}' has been added to the Gone in 60 Parsecs fleet!\n")
        fleet.add_ship(selected)
        targets.remove(selected)  # Remove the captured ship from the target list
        fleet.summary()
        texttime(f"\n Would you like to attempt another mission? (y/n)")
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        print(f"\nElapsed time: {elapsed_time}")
        again = input("  > ").strip().lower()
        if again == 'y':
            main()  # Restart the game loop
        else:
            texttime("\n  🚀 Thanks for playing Gone in 60 Parsecs! Safe travels, space pirate! 🌌\n")
    else:
        texttime(f"\n\n  💀 Mission Failed. '{selected.name}' remains out of reach.")
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        print(f"\nElapsed time: {elapsed_time}\n")
        texttime(f"\n\nCurrent fleet status:\n")
        fleet.summary()
        texttime(f"\n  🔧 Return to Dottie for repairs and try again.\n")
        

if __name__ == "__main__":
    main()