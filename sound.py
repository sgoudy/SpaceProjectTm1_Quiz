"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  SOUND ENGINE
#  Generates .wav files on first run (no assets needed).
#  Plays them cross-platform: Windows → winsound,
#  macOS → afplay,  Linux → aplay.
# ─────────────────────────────────────────────

import wave
import struct
import math
import os
import sys
import threading

SR = 44100  # sample rate

# Sounds are stored next to this file
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

# ─────────────────────────────────────────────
#  INTERNAL WAV BUILDER
# ─────────────────────────────────────────────

def _make_wav(filepath: str, notes: list):
    """
    Build a mono 16-bit WAV from a list of note tuples.
    Each note: (freq_hz, duration_sec, volume_0_to_1, wave_type)
      wave_type: 'sine' | 'square' | 'sawtooth'
      freq_hz=0  → silence
    """
    samples = []
    for freq, duration, volume, wtype in notes:
        n = int(SR * duration)
        for i in range(n):
            t = i / SR
            if freq == 0:
                s = 0.0
            elif wtype == "square":
                s = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
            elif wtype == "sawtooth":
                s = 2.0 * (t * freq - math.floor(0.5 + t * freq))
            else:                                       # sine (default)
                s = math.sin(2 * math.pi * freq * t)

            fade   = min(1.0, (n - i) / max(1, n * 0.15))  # fade out last 15 %
            attack = min(1.0, i        / max(1, n * 0.05))  # attack first  5 %
            samples.append(int(s * volume * fade * attack * 32767))

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with wave.open(filepath, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes(struct.pack("<" + "h" * len(samples), *samples))


# ─────────────────────────────────────────────
#  SOUND DEFINITIONS
# ─────────────────────────────────────────────

def _build_all():
    """Generate all WAV files into the sounds/ folder."""

    # startup.wav — dramatic ascending sci-fi fanfare
    _make_wav(os.path.join(_DIR, "startup.wav"), [
        (220,  0.12, 0.45, "square"),
        (0,    0.04, 0.00, "sine"),
        (330,  0.12, 0.45, "square"),
        (0,    0.04, 0.00, "sine"),
        (440,  0.12, 0.45, "square"),
        (0,    0.04, 0.00, "sine"),
        (660,  0.22, 0.50, "square"),
        (0,    0.06, 0.00, "sine"),
        (880,  0.35, 0.55, "sine"),
        (0,    0.05, 0.00, "sine"),
        (1100, 0.20, 0.50, "sine"),
        (0,    0.05, 0.00, "sine"),
        (880,  0.50, 0.45, "sine"),
    ])

    # correct.wav — bright ascending chime (C5 → E5 → G5 → C6)
    _make_wav(os.path.join(_DIR, "correct.wav"), [
        (523,  0.10, 0.50, "sine"),
        (659,  0.10, 0.50, "sine"),
        (784,  0.10, 0.50, "sine"),
        (1047, 0.28, 0.55, "sine"),
    ])

    # wrong.wav — descending square-wave buzz
    _make_wav(os.path.join(_DIR, "wrong.wav"), [
        (220, 0.15, 0.60, "square"),
        (180, 0.15, 0.60, "square"),
        (140, 0.25, 0.55, "square"),
    ])

    # warning.wav — urgent triple-pulse (fires at 5 s remaining)
    _make_wav(os.path.join(_DIR, "warning.wav"), [
        (880, 0.10, 0.65, "square"),
        (0,   0.08, 0.00, "sine"),
        (880, 0.10, 0.65, "square"),
        (0,   0.08, 0.00, "sine"),
        (880, 0.10, 0.65, "square"),
    ])

    # timeout.wav — deep sawtooth descending alarm
    _make_wav(os.path.join(_DIR, "timeout.wav"), [
        (440, 0.12, 0.60, "sawtooth"),
        (0,   0.04, 0.00, "sine"),
        (370, 0.12, 0.60, "sawtooth"),
        (0,   0.04, 0.00, "sine"),
        (300, 0.14, 0.60, "sawtooth"),
        (0,   0.04, 0.00, "sine"),
        (220, 0.30, 0.55, "sawtooth"),
    ])


# ─────────────────────────────────────────────
#  CROSS-PLATFORM PLAYER
# ─────────────────────────────────────────────

def _play_wav(filepath: str, block: bool = False):
    """Play a WAV file. Runs in a daemon thread unless block=True."""

    def _play():
        try:
            if sys.platform == "win32":
                import winsound
                winsound.PlaySound(filepath, winsound.SND_FILENAME)
            elif sys.platform == "darwin":
                os.system(f'afplay "{filepath}" &' if not block else f'afplay "{filepath}"')
            else:
                # Linux — try aplay, fall back silently
                flag = "" if block else " &"
                os.system(f'aplay -q "{filepath}"{flag} 2>/dev/null')
        except Exception:
            pass  # Audio failure should never crash the game

    if block:
        _play()
    else:
        t = threading.Thread(target=_play, daemon=True)
        t.start()


# ─────────────────────────────────────────────
#  ONE-TIME INIT
# ─────────────────────────────────────────────

def init_sounds():
    """Call once at program startup. Generates WAVs if missing."""
    sounds = ["startup.wav", "correct.wav", "wrong.wav", "warning.wav", "timeout.wav"]
    missing = [s for s in sounds if not os.path.exists(os.path.join(_DIR, s))]
    if missing:
        _build_all()


# ─────────────────────────────────────────────
#  PUBLIC API
# ─────────────────────────────────────────────

def play_startup():
    """Fanfare that plays as the program launches."""
    _play_wav(os.path.join(_DIR, "startup.wav"), block=False)

def play_correct():
    """Ascending chime for a correct answer."""
    _play_wav(os.path.join(_DIR, "correct.wav"), block=False)

def play_wrong():
    """Descending buzz for a wrong answer."""
    _play_wav(os.path.join(_DIR, "wrong.wav"), block=False)

def play_warning():
    """Urgent triple-beep when 5 seconds remain on the timer."""
    _play_wav(os.path.join(_DIR, "warning.wav"), block=False)

def play_timeout():
    """Descending alarm when time runs out."""
    _play_wav(os.path.join(_DIR, "timeout.wav"), block=False)
