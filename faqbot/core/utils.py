"""Just some random helpers."""

from faqbot.core.store import load_config, save_config


def start_trigger(s, triggers):
    for t in triggers:
        if s.startswith(t):
            return t
    return None


MENU = None


def get_menu():
    global MENU

    if MENU:
        return MENU

    MENU = load_config("menu")
    return MENU
