"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  Animation
# ─────────────────────────────────────────────

import sys
import time

# Typing effect for the welcome message
def texttime(words):
    """Prints text with a typing animation effect."""
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)


# Progress bar animation for loading the game
def slow_progress_bar():
    """ Displays a progress bar animation to simulate loading time."""
    animation = ["[■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■□□□]","[■■■■■■■■■■■□□□□]",
                 "[■■■■■■■■■■□□□□□]","[■■■■■■■■■□□□□□□]","[■■■■■■■■□□□□□□□]", "[■■■■■■■□□□□□□□□]", "[■■■■■■□□□□□□□□□]",  
                 "[■■■■■□□□□□□□□□□]", "[■■■■□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□]", "[■■□□□□□□□□□□□□□]", "[■□□□□□□□□□□□□□□]"
                 ]
    delay = 1.0 
    for item in animation:
        sys.stdout.write(f"\rCountdown: {item}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\rTime's Up!      \n")
