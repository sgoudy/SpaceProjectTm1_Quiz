"""@Authors: Charles, Jordan, Shelby, Robert, Jon"""
# The user has a 15 second time limit to answer each question in the hack mission. 
# If they fail to answer within the time limit, it counts as a wrong answer and damages their hull by 25%. 
# The timer resets for each new question, giving them a fresh 15 seconds to respond. This adds an extra layer of challenge and urgency to the game, 
# simulating the high-stakes environment of a space heist.

# ─────────────────────────────────────────────
#  TIMED INPUT — 15 second live countdown
# ─────────────────────────────────────────────
from pytimedinput import timedInput
from datetime import datetime
from animation import slow_progress_bar, texttime
import time
from pytimedinput import timedInput

def get_strict_timed_choice():
    """
        Sets a 15 second time limit. Checks to make sure the input is valid
        and returns a correction if not.
        Returns: User Answer
    """
    valid_options = ['a', 'b', 'c', 'd']
    total_timeout = 15
    start_time = time.time()
    
    while True:
        # Calculate how much time is left
        elapsed = time.time() - start_time
        remaining = total_timeout - elapsed
        
        if remaining <= 0:
            print("\n⏰ Time's up!")
            return None

        prompt = f"Choose wisely (a-d) [{int(remaining)}s left]: "
        
        # Pass the *remaining* time, not the full 15s
        user_text, timed_out = timedInput(prompt, timeout=remaining, resetOnInput=False)
        
        if timed_out:
            print("\n⏰ Time's up!")
            return None
        
        choice = user_text.strip().lower()
        
        if choice in valid_options:
            return choice
        else:
            print(f"❌ Invalid '{choice}'. Try again quickly!")
            # Loop continues, but next timedInput will have less time    


def missionTimer(start_time):
    end_time = datetime.now() 
    duration = end_time - start_time
   
    # Extract total seconds and calculate minutes/seconds
    total_seconds = int(duration.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return(f"  Mission Duration: {minutes:02d}:{seconds:02d}\n")