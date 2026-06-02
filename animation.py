"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  TEXT ANIMATION
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