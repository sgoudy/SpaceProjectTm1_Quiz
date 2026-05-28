"""@Authors: Charles, Jordan, Shelby, Robert, Jon"""
# The user has a 15 second time limit to answer each question in the hack mission. 
# If they fail to answer within the time limit, it counts as a wrong answer and damages their hull by 25%. 
# The timer resets for each new question, giving them a fresh 15 seconds to respond. This adds an extra layer of challenge and urgency to the game, 
# simulating the high-stakes environment of a space heist.

# ─────────────────────────────────────────────
#  TIMED INPUT — 15 second live countdown
# ─────────────────────────────────────────────

from pytimedinput import timedInput

from animation import texttime
def countdown():
    texttime("\n⏳ Time remaining: 15 seconds\nChoose wisely (a/b/c/d): \n")
    
    user_text, timed_out = timedInput("", timeout=15)

    if timed_out:
        texttime("\n⏰ Time's up! No input received.")
        answer = None
    else:
        answer = user_text.lower() 
    return answer