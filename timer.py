"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  TIMED FUNCTIONS
# ─────────────────────────────────────────────

from pytimedinput import timedInput
from datetime import datetime
import time
from sound import play_warning

# ─────────────────────────────────────────────
#  TIMED INPUT — 15 second live countdown
# ─────────────────────────────────────────────

def get_strict_timed_choice():
    """Sets a 15 second time limit. Checks to make sure the input is valid
        and returns a correction if not.
       Returns: User Answer (or None if timed out)
    """
    valid_options = ['a', 'b', 'c', 'd']
    total_timeout = 15
    start_time = time.time()
    warning_played = False   # ensure the 5-second warning fires only once

    # Loop until valid input or timeout
    while True:

        # Calculate remaining time for this input attempt
        elapsed   = time.time() - start_time
        remaining = total_timeout - elapsed

        # If time has run out, return None to indicate timeout
        if remaining <= 0:
            print("\n⏰ Time's up!")
            return None

        # ── 5-second warning ──────────────────────────────
        if remaining <= 5 and not warning_played:
            play_warning()
            warning_played = True

        prompt = f"Choose wisely (a-d) [{int(remaining)}s left]: "

        # Get user input with remaining time as timeout
        user_text, timed_out = timedInput(prompt, timeout=remaining, resetOnInput=False)

        if timed_out:
            print("\n⏰ Time's up!")
            return None

        # Change to lower case and strip whitespace for validation
        choice = user_text.strip().lower()

        # Validate input and return if valid, otherwise prompt again
        if choice in valid_options:
            return choice
        else:
            print(f"❌ Invalid '{choice}'. Try again quickly!")

# ─────────────────────────────────────────────
# Mission Timer
# ─────────────────────────────────────────────
def missionTimer(start_time):
    '''Calculates and formats the duration of a mission based on the start time.
    Attributes:    
     start_time (datetime): The time when the mission started.
    Returns a string in the format "MM:SS".
    '''
    # Calculate elapsed time
    end_time = datetime.now() 
    duration = end_time - start_time
   
    # Extract total seconds and calculate minutes/seconds
    total_seconds = int(duration.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return(f"  Mission Duration: {minutes:02d}:{seconds:02d}\n")