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
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.025)


# Progress bar animation for loading the game
def slow_progress_bar():
    # i want 15 bars in the animation below, each representing 1 second of the 15 second countdown timer
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
