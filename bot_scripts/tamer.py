import signal
import time
import os


def press(kbd, key, wait: int | float = 0):
    """
    Press the given key

    :param kbd: Pynput keyboard controller
    :param key: Key to be pressed
    :param wait: Time to wait after the key was pressed
    :return: None
    """
    kbd.press(key)
    kbd.release(key)
    time.sleep(wait)


def heal(kbd):
    """Heal up the pet"""
    press(kbd, 'r', 1.5)
    time.sleep(1.5)


def buff(kbd, key):
    """Buff up self/pet"""
    press(kbd, key.f2, 1.5)
    press(kbd, 'q', 1.5)


def tamer_1(kbd, key, loot, check_window, check_resources, rebuff_after=15):
    """
    Bot script for tamer

    :param check_window: Method that checks if TO window is still open,
                            and stop bot if it isn't
    :param kbd: Pynput keyboard controller
    :param key: Pynput key class
    :param loot: Function for looting corpses
    :param rebuff_after: Rebuff after n loops
    :return: None
    """
    counter = 1
    buff(kbd, key)

    while True:
        press(kbd, key.tab, 1)
        press(kbd, '`', 1)
        press(kbd, '1', 2)
        press(kbd, '2', 3)
        press(kbd, '2', 2)

        # Heal
        heal(kbd)

        # Rest
        press(kbd, 'x', 3)

        # Check if TO window is still open, and stop bot if it isn't
        check_window()

        # Loot
        loot(res='1440p')

        # Rebuff
        if counter % rebuff_after == 0:
            buff(kbd, key)

        print(f'Loop nr {counter}')
        counter += 1
