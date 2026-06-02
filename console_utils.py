"""Utilities for consistent console banners and headers."""

BANNER_WIDTH = 70


def centered_line(text: str, sep_char: str, width: int = BANNER_WIDTH) -> str:
    content = f" {text} "
    full_width = max(width, len(content) + 2)
    remaining = full_width - len(content)
    left = remaining // 2
    right = remaining - left
    return "\n" + sep_char * left + content + sep_char * right + "\n"


def banner(text: str, width: int = BANNER_WIDTH) -> str:
    return centered_line(text, "═", width)


def section_header(text: str, width: int = BANNER_WIDTH) -> str:
    return centered_line(text, "─", width)
