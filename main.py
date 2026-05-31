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
from timer import missionTimer


# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────


def main():

    # texttime("\n" + "★" * 25+"       GONE IN 60 PARSECS >> Space Heist | Hack or Be Hacked       "+"★" * 25+"\n\n")

    # intro_scroll()

    # --- Setup Homebase ---
    texttime("\n\n   ...Initializing Dottie's Homebase...\n")
    time.sleep(1.5)
    # Instantiating the homebase with specific attributes
    dottie = Homebase("Dottie", "Asteroid near Pluto, Milky Way", 12)
    # for line in dottie.summary():
    #     print(line)
    #     time.sleep(0.3)

    # --- Setup Player Ship ---
    texttime("\n\n   ...Initializing Your Hack Ship on Dottie...\n")
    time.sleep(1.5)
    # Instantiating the player's hack ship with specific attributes
    player_ship = HackShip(name="The Phantom Byte",speed=4.2,capacity=6,weapons=["EMP Cannon", "Cyber Spike", "Signal Jammer"]    )
    # for line in player_ship.summary():
    #     print(line)
    #     time.sleep(0.3)

   
    # --- Display Targets ---
    # Instantiating the target ships with specific attributes
    targets = [
            EnemySpaceShip("Enterprise",  "Top Gun",   "Planet Vulcan",       2.3,  "Network Security"),
            EnemySpaceShip("Eleanor",     "ANDROMEDA", "Planet Vega",         5.1,  "Encryption"),
            EnemySpaceShip("Tardis",      "Tesla",     "Jupiter's Moon: Io",  1.8,  "Social Engineering"),
            EnemySpaceShip("Serenity",    "Firefly",   "Saturn's Moon: Titan",1.2,  "Malware & Intrusion"),
        ]

    game = True
    while game and len(targets) > 0: 
        texttime("\n" + "─" * 25 +" 📋 ACTIVE TARGETS  "+"─" * 25 +"\n")
       
        # start=1 makes the index begin at 1 instead of the default 0
        # for i, t in enumerate(targets, start=1):
        #     print(f"{i}: ", end='', flush=True)
        #     t.summary()
        #     time.sleep(0.3)

        number_list = list(range(len(targets)))
        numberListPlusOne = [item + 1 for item in number_list]  # More concise list comprehension

        # Have the player choose which ship based on number of ships in list
        while True:
            choice = input(f"\n  Select your target {numberListPlusOne}: ")
            
            try:
                # Convert input to integer immediately
                choice_int = int(choice)
                
                if choice_int in numberListPlusOne:
                    selected = targets[choice_int - 1]
                    print("\n" + "═" * 25+ f"  🔓 HACK MISSION: TARGET = {selected.name} [{selected.codename}] "+"═" * 25+"\n\n")
                    break
                else:
                    print("Invalid choic2e: Number not in the list.")
                    
            except ValueError:
                print("Invalid input: Please enter a valid number.")

        # --- Run the Mission ---
        start_time = datetime.now()

        result = run_hack_mission(player_ship, selected)

        # --- Final Status ---
        texttime("\n" + "═" * 25+"      📊 GENERATING END OF MISSION REPORT       "+"═" * 25 + "\n")
        result = True
        if result:
            
            # Mission duration
            time_for_mission = missionTimer(start_time)
            texttime(time_for_mission)
            
            # Add ship to fleet
            texttime(f"\n  🎉 '{selected.name}' has been added to the Gone in 60 Parsecs fleet!\n")
            fleet.add_ship(selected)

            # Remove ship from target list
            targets.remove(selected)  # Remove the captured ship from the target list
            
            fleet.summary()
            
        else:
            texttime(f"\n\n  💀 Mission Failed. '{selected.name}' remains out of reach.")
            
            # Mission duration
            time_for_mission = missionTimer(start_time)
            texttime(time_for_mission)

            # Print fleet status and send RTB message
            texttime(f"\n\nCurrent fleet status:\n")
            fleet.summary()
            texttime(f"\n  🔧 Return to Dottie for repairs and try again.\n")

        if len(targets) > 0:
            print(len(targets))
            # Reset Game?
            texttime(f"\n Would you like to attempt another mission? (y/n)")
            again = input("  > ").strip().lower()

            # Reset game logic
            if again == 'y':
                game = True
            else:
                texttime("\n  🚀 Thanks for playing Gone in 60 Parsecs! Safe travels, space pirate! 🌌\n")
                game = False
                break
        else:
            texttime("\n  🚀 You've captured the entire fleet! Carry on with your day, space pirate. 🌌\n")

if __name__ == "__main__":
    main()