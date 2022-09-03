import time


def press(kbd, key, wait=0):
    kbd.press(key)
    kbd.release(key)
    time.sleep(wait)


def buff(kbd, key):
    press(kbd, key.f2, 1)
    press(kbd, '7', 1)
    press(kbd, key.f3, 1)
    press(kbd, '8', 1)


def heal(kbd, key):
    pass


def monk_1(kbd, key, brute_force_loot, buff_after=10, rest_for=3, counter=1):
    buff(kbd, key)
    while True:
        press(kbd, key.tab, 1)
        press(kbd, '3', 3)
        press(kbd, '3', 3)
        press(kbd, '3', 3)
        press(kbd, '3', 3)
        press(kbd, '3', 3)

        # Loot
        # brute_force_loot(res='1080p')
        brute_force_loot()

        # Rebuff
        if counter % buff_after == 0:
            buff(kbd, key)

        # Rest
        kbd.press('x')
        kbd.release('x')
        time.sleep(rest_for)
        print(f'Loop nr {counter}')
        counter += 1
