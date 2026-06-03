"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  MISSION: HACK A SHIP
# ─────────────────────────────────────────────

import random
import time
from hackship import HackShip
from questions import QUESTION_BANK
from enemySS import EnemySpaceShip
from timer import get_strict_timed_choice
from animation import texttime
from console_utils import banner, section_header
from sound import play_correct, play_wrong, play_timeout

def run_hack_mission(player_ship: HackShip, target: EnemySpaceShip):
    """
    Run the hacking mission against a target ship.
    - 6 questions from the target's cybersecurity topic
    - Correct answer: -25% off target's defenses
    - Wrong answer: -25% off player's hull
    - Win condition: 4 correct answers (defenses reach 0%)
    - Lose condition: player ship hull reaches 0%
    """
    missionBrief = [f"\n  Location : {target.location}",
                    f"  Distance : {target.distance} parsecs",
                    f"  Topic    : {target.cyber_topic}",
                    f"  Your Hull: {player_ship.hull}%"]
    
    for line in missionBrief:
        print(line)
        time.sleep(0.2)  

    texttime(f"\n  Answer 4 questions correctly to steal the ship!\n")
    texttime(f"  But beware — wrong answers damage YOUR hull.\n")

    # Select 6 random questions from the target's cyber topic
    questions = random.sample(QUESTION_BANK[target.cyber_topic], 6)

    correct = 0
    wrong = 0

    # Quiz flow
    for i, (question, answer, choices) in enumerate(questions, 1):
        texttime(section_header(f"Question {i} of 6"))
        texttime(f"\n  {question}\n\n")
        for choice in choices:
            print(f"    {choice}")
            time.sleep(0.5)

        # Validates input and enforces time limit
        response = get_strict_timed_choice()
        
        # No response means timeout, which counts as wrong
        if response is None:
            play_timeout()
            wrong += 1
            player_ship.take_damage(25)
            texttime(f"\n  ⏰ TIME'S UP!  Hull damaged → {player_ship.name}'s hull now at {player_ship.hull}%\n")
        
        # Correct answer and damage target's defenses
        elif response == answer:
            play_correct()
            correct += 1
            target.breach(25)
            texttime(f"\n  ✅ CORRECT! Defense breached → {target.name}'s defenses now at {target.defenses}%\n")
        
        # Wrong answer and damage player's hull
        else:
            play_wrong()
            wrong += 1
            player_ship.take_damage(25)
            texttime(f"\n  ❌ WRONG!  Hull damaged → {player_ship.name}'s hull now at {player_ship.hull}%\n")
            texttime(f"\n  💡 The correct answer was: {answer.upper()}\n\n")

        texttime(f"  [Score: {correct} correct / {wrong} wrong]\n")

        # Check win condition
        if correct >= 4:
            texttime(banner("🏆 MISSION SUCCESS!"))
            print(f"\n  You hacked through {target.name}'s defenses!\n")
            time.sleep(0.5)
            print(f"  The {target.name} is YOURS. I will add it to your fleet. 🚀")
            return True

        # Check lose condition
        if player_ship.is_destroyed():
            texttime(banner("💥 MISSION FAILED!"))
            print(f"\n  {player_ship.name} has been destroyed!\n")
            time.sleep(0.5)
            print(f"  {target.name}'s security systems overwhelmed you.")
            return False

    # Ran out of questions without winning
    texttime(banner(f"❌ MISSION FAILED: {target.name} remains out of reach... for now."))
    return False
