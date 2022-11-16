import time


def press(kbd, key, wait=0):
    kbd.press(key)
    kbd.release(key)
    time.sleep(wait)


def heal(kbd, key):
    kbd.press(key.f1)
    kbd.release(key.f1)
    kbd.press('r')
    kbd.release('r')
    time.sleep(1.5)


def buff(kbd):
    kbd.press('w')
    kbd.release('w')
    time.sleep(1.5)


def tamer_1(kbd, key, loot, rebuff_after=15, rest_for=None, counter=1):
    buff(kbd)

    while True:
        press(kbd, key.tab, 1)
        press(kbd, '`', 1)
        press(kbd, '1', 1.5)

        # Rest
        kbd.press('x')
        kbd.release('x')

        # Loot
        loot(res='1080p')

        # Rebuff
        if counter % rebuff_after == 0:
            buff(kbd)

        heal(kbd, key)

        print(f'Loop nr {counter}')
        counter += 1
