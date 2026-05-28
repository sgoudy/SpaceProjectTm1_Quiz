
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

    print("\n" + "═" * 55)
    print(f"  🔓 HACK MISSION: {target.name} [{target.codename}]")
    print("═" * 55)
    print(f"  Location : {target.location}")
    print(f"  Distance : {target.distance} parsecs")
    print(f"  Topic    : {target.cyber_topic}")
    print(f"\n  Your Hull    : {player_ship.hull}%")
    print(f"  Ship Defenses: {target.defenses}%")
    print("\n  Answer 4 questions correctly to steal the ship!")
    print("  But beware — wrong answers damage YOUR hull.\n")

    questions = random.sample(QUESTION_BANK[target.cyber_topic], 6)

    correct = 0
    wrong = 0

    for i, (question, answer, choices) in enumerate(questions, 1):
        print(f"─── Question {i} of 6 ───────────────────────────────")
        print(f"  {question}\n")
        for choice in choices:
            print(f"    {choice}")

        response = input("\n  Your answer (a/b/c/d): ").strip().lower()

        if response == answer:
            correct += 1
            target.breach(25)
            print(f"\n  ✅ CORRECT! Defense breached → Ship defenses now at {target.defenses}%")
        else:
            wrong += 1
            player_ship.take_damage(25)
            print(f"\n  ❌ WRONG!  Hull damaged → Your hull now at {player_ship.hull}%")

        print(f"  [Score: {correct} correct / {wrong} wrong]\n")

        # Check win condition
        if correct >= 4:
            print("═" * 55)
            print(f"  🏆 MISSION SUCCESS!")
            print(f"  You hacked through {target.name}'s defenses!")
            print(f"  The {target.name} is YOURS. Welcome to the fleet. 🚀")
            print("═" * 55)
            return True

        # Check lose condition
        if player_ship.is_destroyed():
            print("═" * 55)
            print(f"  💥 MISSION FAILED!")
            print(f"  {player_ship.name} has been destroyed!")
            print(f"  {target.name}'s security systems overwhelmed you.")
            print("═" * 55)
            return False

    # Ran out of questions without winning
    print("═" * 55)
    print(f"  ❌ MISSION FAILED — Not enough correct answers.")
    print(f"  {target.name} remains out of reach... for now.")
    print("═" * 55)
    return False
