"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────

import time
from hackship import HackShip
from mission import run_hack_mission
from enemySS import EnemySpaceShip
from homebase import Homebase
from animation import texttime
from console_utils import banner, section_header
from fleet import fleet
from datetime import datetime
from intro import intro_scroll
from timer import missionTimer
from sound import init_sounds, play_startup

def main():

    # generate WAV files on first run (silent if already exist)
    init_sounds()    

    # fanfare plays while the title banner prints
    play_startup()   

    texttime("\n" + "★" * 25+"       GONE IN 60 PARSECS >> Space Heist | Hack or Be Hacked       "+"★" * 25+"\n\n")

    # Run the intro scroll animation
    intro_scroll() 

    # --- Setup Homebase ---
    texttime("\n\n   ...Initializing Dottie's Homebase...\n")
    time.sleep(1.5)
    # Instantiating the homebase with specific attributes
    dottie = Homebase("Dottie", "Asteroid near Pluto, Milky Way", 5)
    for line in dottie.summary():
        print(line)
        time.sleep(0.3)

    # --- Setup Player Ship ---
    texttime("\n\n   ...Initializing Your Hack Ship on Dottie...\n")
    time.sleep(1.5)

    # Instantiating the player's hack ship with specific attributes
    player_ship = HackShip(name="The Phantom Byte",speed=4.2,capacity=6,weapons=["EMP Cannon", "Cyber Spike", "Signal Jammer"]    )
    for line in player_ship.summary():
        print(line)
        time.sleep(0.3)
   
    # --- Display Targets ---
    # Instantiating the target ships with specific attributes
    targets = [
            EnemySpaceShip("Enterprise",  "Top Gun",   "Planet Vulcan",       2.3,  "Network Security"),
            EnemySpaceShip("Andromeda",     "Eleanor", "Planet Vega",         5.1,  "Encryption"),
            EnemySpaceShip("Tardis",      "Tesla",     "Jupiter's Moon: Io",  1.8,  "Social Engineering"),
            EnemySpaceShip("Serenity",    "Firefly",   "Saturn's Moon: Titan",1.2,  "Malware & Intrusion"),
        ]

    game = True

    # Run the game while there are still targets to hack and steal
    while game and len(targets) > 0: 
        texttime(section_header("📋 ACTIVE TARGETS"))
       
        # start=1 makes the index begin at 1 instead of the default 0
        for i, t in enumerate(targets, start=1):
            print(f"{i}: ", end='', flush=True)
            t.summary()
            time.sleep(0.3)

        # Logic for numbering enemy ships for user selection
        number_list = list(range(len(targets)))
        numberListPlusOne = [item + 1 for item in number_list]  

        # Have the player choose which ship based on number of ships in list
        while True:
            choice = input(f"\n  Select your target {numberListPlusOne}: ")
            
            try:
                # Convert input to integer immediately
                choice_int = int(choice)
                
                if choice_int in numberListPlusOne:
                    selectedTargetShip = targets[choice_int - 1]
                    texttime(banner(f"🔓 HACK MISSION: TARGET = {selectedTargetShip.name} [{selectedTargetShip.codename}]: Defenses = {selectedTargetShip.defenses}%") )
                    break
                else:
                    print("Invalid choice: number not in the list.")
                    
            except ValueError:
                print("Invalid input: Please enter a valid number.")
        
        # Target ship has been selected-----------------------------------------------------------------------        
        
        # Establish a start time so we can time the mission
        start_time = datetime.now()

        # --- Run the Mission/Quiz ---
        result = run_hack_mission(player_ship, selectedTargetShip)
        # ---------------------------------
        # If result is True, the player won the mission and captured the ship. 
        # If False, they lost and the ship remains free.

        # --- Final Status ---
        texttime(banner("📊 GENERATING END OF MISSION REPORT"))
        # fleet = [] # Create an empty fleet to store captured ships

        # Save mission duration
        time_for_mission = missionTimer(start_time)

        # True means player won the mission and captured the ship
        if result:
            
            # Print result to screen
            texttime(f"\n  🎉 '{selectedTargetShip.name}' has been added to the Gone in 60 Parsecs fleet!\n\n {time_for_mission}")
            
            # Add ship to fleet
            fleet.add_ship(selectedTargetShip)

            # Remove ship from available target list
            targets.remove(selectedTargetShip)  # Remove the captured ship from the target list
            
            # Print your hull status
            texttime(f"\n  🛠️  '{player_ship.name}' hull status: {player_ship.hull}%\n")

            # Print fleet status
            fleet.summary()
        
        # Player lost the mission, so the target ship remains free and their hull is damaged but they're still alive
        elif player_ship.hull >= 25:
            
            # Print result to screen
            texttime(f"\n  💀 Mission Failed. '{selectedTargetShip.name}' remains out of reach.\n\n {time_for_mission}")
            
            # Print fleet status and send RTB message
            if len(fleet.ships) > 0:
                texttime(f"\n\nCurrent fleet status:\n{fleet.summary()}\n  🔧 Return to Dottie for repairs and try again.\n")
            else:
                texttime(f"\n  🚀 Your fleet is empty. Return to Dottie for repairs and try again.\n")
        else:
            texttime("\n  🚀 Your ship is too damaged to continue. You should probably choose a different career, 'Space Pirate'. 🌌\n")
            game = False
            break
      
        if len(targets) > 0:

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