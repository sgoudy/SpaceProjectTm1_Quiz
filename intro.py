# --- Star Wars Style Scrolling Intro ---
import time

intro_lines = [
    "",
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "",
    "  [CLASSIFIED — EYES ONLY]",
    "  [TRANSMISSION SOURCE: ASTEROID DOTTIE | DEEP SPACE]",
    "",
    "  Somewhere out there, in the cold silence between",
    "  stars, four of the most legendary ships in the",
    "  galaxy drift through the dark — unaware that they",
    "  have already been chosen.",
    "",
    "  The Enterprise. The Eleanor.",
    "  The Tardis.    The Serenity.",
    "",
    "  You have tracked them.",
    "  You have studied them.",
    "  Now it is time to take them.",
    "",
    "  But these are not ordinary ships.",
    "  Each one is protected by layers of cybersecurity",
    "  so deep, so dangerous, that entire fleets have",
    "  tried — and failed — to breach them.",
    "",
    "  You will not use weapons.",
    "  You will not use force.",
    "  You will use your mind.",
    "",
    "  Every firewall has a crack.",
    "  Every cipher has a key.",
    "  Every system... has a weakness.",
    "",
    "  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─",
    "",
    "  You have 30 seconds per question.",
    "  4 correct answers breaches their defenses.",
    "  1 wrong move damages YOUR hull.",
    "",
    "  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─",
    "",
    "  The galaxy is watching.",
    "  Dottie is counting on you.",
    "",
    "  Don't.  Miss.",
    "",
    "  [END TRANSMISSION]",
    "",
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "",
]

def intro_scroll():
    for line in intro_lines:
        print(line)
        # Blank lines scroll faster, dramatic lines slower
        if line.strip() == "":
            time.sleep(0.3)
        elif line.strip().startswith("░"):
            time.sleep(0.4)
        elif line.strip().startswith("─"):
            time.sleep(0.3)
        elif line.strip() in ["Don't.  Miss.", "You will use your mind."]:
            time.sleep(1.2)  # extra pause on dramatic lines
        elif line.strip().startswith("["):
            time.sleep(0.6)
        else:
            time.sleep(0.5)

    input("  Press ENTER to begin your mission, Agent... ")
    print()