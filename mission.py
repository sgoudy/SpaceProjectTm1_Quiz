import random
from hackship import HackShip
from quiz import QUESTION_BANK
from enemySS import EnemySpaceShip
from homebase import Homebase
from timer import countdown
from animation import texttime
# ─────────────────────────────────────────────
#  MISSION: HACK A SHIP
# ─────────────────────────────────────────────
def run_hack_mission(player_ship: HackShip, target: EnemySpaceShip):
    """
    Run the hacking mission against a target ship.
    - 6 questions from the target's cybersecurity topic
    - Correct answer: -25% off target's defenses
    - Wrong answer: -25% off player's hull
    - Win condition: 4 correct answers (defenses reach 0%)
    - Lose condition: player ship hull reaches 0%
    """

    texttime("\n" + "═" * 25)
    texttime(f"  🔓 HACK MISSION: TARGET = {target.name} [{target.codename}] ")
    texttime("═" * 25+"\n")
    texttime(f"  Location : {target.location}\n")
    texttime(f"  Distance : {target.distance} parsecs\n")
    texttime(f"  Topic    : {target.cyber_topic}\n")
    texttime(f"  Your Hull    : {player_ship.hull}%\n")
    texttime(f"  Ship Defenses: {target.defenses}%\n")
    texttime(f"  Answer 4 questions correctly to steal the ship!\n")
    texttime(f"  But beware — wrong answers damage YOUR hull.\n")

    questions = random.sample(QUESTION_BANK[target.cyber_topic], 6)

    correct = 0
    wrong = 0

    for i, (question, answer, choices) in enumerate(questions, 1):
        print(f"\n────────────────────────────────────────────────────────────")
        texttime(f"──────────── Question {i} of 6 ───────────────────────────────\n")
        texttime(f"  {question}\n")
        for choice in choices:
            texttime(f"    {choice}\n")

        response = countdown()

        if response == answer:
            correct += 1
            target.breach(25)
            texttime(f"\n  ✅ CORRECT! Defense breached → {target.name}'s defenses now at {target.defenses}%\n")
            
        else:
            wrong += 1
            player_ship.take_damage(25)
            texttime(f"\n  ❌ WRONG!  Hull damaged → {player_ship.name}'s hull now at {player_ship.hull}%\n")

        texttime(f"  [Score: {correct} correct / {wrong} wrong]\n")

        # Check win condition
        if correct >= 4:
            texttime("\n" + "═" * 25)
            texttime(" 🏆 MISSION SUCCESS! ")
            texttime("═" * 25 + "\n")
            texttime(f"  You hacked through {target.name}'s defenses!\n")
            texttime(f"  The {target.name} is YOURS. I will add it to your fleet. 🚀\n")
            return True

        # Check lose condition
        if player_ship.is_destroyed():
            texttime("═" * 25)
            texttime("  💥 MISSION FAILED!\n")
            texttime(f"  {player_ship.name} has been destroyed!\n")
            texttime(f"  {target.name}'s security systems overwhelmed you.\n")
            texttime("═" * 25 + "\n")
            return False

    # Ran out of questions without winning
    texttime("═" * 25)
    texttime("  ❌ MISSION FAILED — Not enough correct answers.\n")
    texttime(f"  {target.name} remains out of reach... for now.\n")
    texttime("═" * 25 + "\n")
    return False
