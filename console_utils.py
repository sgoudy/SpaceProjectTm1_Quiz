"""@Authors: Charles, Jordan, Jon, Robert, Shelby
Date: April Cohort 2026
"""

# ─────────────────────────────────────────────
#  Display Prettifier
# ─────────────────────────────────────────────

"""Utilities for consistent console banners and headers."""

BANNER_WIDTH = 70

def centered_line(text: str, sep_char: str, width: int = BANNER_WIDTH) -> str:
    """Returns a string with the text centered and padded by the specified separator character."""
    content = f" {text} "
    full_width = max(width, len(content) + 2)
    remaining = full_width - len(content)
    left = remaining // 2
    right = remaining - left
    return "\n" + sep_char * left + content + sep_char * right + "\n"

def banner(text: str, width: int = BANNER_WIDTH) -> str:
    """Returns a banner string with the text centered and padded by '═' characters."""
    return centered_line(text, "═", width)

def section_header(text: str, width: int = BANNER_WIDTH) -> str:
    """Returns a section header string with the text centered and padded by '─' characters."""
    return centered_line(text, "─", width)