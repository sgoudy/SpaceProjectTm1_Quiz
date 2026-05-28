"""@Authors: Charles, Jordan, Shelby, Robert, Jon"""
import sys
import time


# Typing effect for the welcome message
def texttime(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)


# Progress bar animation for loading the game
def slow_progress_bar():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", 
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    delay = 0.50 
    for item in animation:
        sys.stdout.write(f"\rLoading: {item}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\rLoading: Complete!      \n")
