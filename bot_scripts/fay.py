import time


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


def buff(kbd, key):
    pass


def heal(kbd, key):
    press(kbd, key.f1)
    press(kbd, 'r', 1.5)


def fay_1(kbd, key, loot, check_window, check_resources):
    """
    Bot script for tamer

    :param check_window: Method that checks if TO window is still open,
                            and stop bot if it isn't
    :param kbd: Pynput keyboard controller
    :param key: Pynput key class
    :param loot: Function for looting corpses
    :return: None
    """
    rest_for = 10
    rebuff_after = 15

    counter = 1

    buff(kbd, key)

    while True:
        press(kbd, key.tab)
        press(kbd, '3', 3)
        press(kbd, '1', 1.5)
        press(kbd, '3', 3.5)
        press(kbd, '3', 3.5)
        press(kbd, '3', 1)

        # Loot
        check_window()
        loot(res='1440p')

        # Heal up and rest
        resources = check_resources()
        heal(kbd, key)
        if not resources['MP']:
            # Rest
            press(kbd, 'x', rest_for)

        # Rebuff
        if counter % rebuff_after == 0:
            buff(kbd, key)

        print(f'Loop nr {counter}')
        counter += 1
