import time


def buff():
    pass


def heal(kbd, key):
    kbd.press(key.f1)
    kbd.release(key.f1)
    kbd.press('r')
    kbd.release('r')
    time.sleep(1.5)


def fay_1(kbd, key, brute_force_loot, heal_after=1, rest_for=5, counter=1):
    while True:
        kbd.press(key.tab)
        kbd.release(key.tab)
        time.sleep(1)
        kbd.press('3')
        kbd.release('3')
        time.sleep(3)
        kbd.press('3')
        kbd.release('3')
        time.sleep(3)
        kbd.press('3')
        kbd.release('3')

        time.sleep(4)

        # Loot
        # brute_force_loot(res='1080p')
        brute_force_loot()

        # Heal
        if counter % heal_after == 0:
            heal(kbd, key)

        # Rest
        kbd.press('x')
        kbd.release('x')
        time.sleep(rest_for)
        print(f'Loop nr {counter}')
        counter += 1
