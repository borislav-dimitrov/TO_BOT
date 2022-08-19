import time


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
        kbd.press(key.tab)
        kbd.release(key.tab)
        time.sleep(1)
        kbd.press('`')
        kbd.release('`')
        time.sleep(1)
        kbd.press('1')
        kbd.release('1')
        time.sleep(4)
        kbd.press('2')
        kbd.release('2')
        time.sleep(4)
        kbd.press('2')
        kbd.release('2')
        time.sleep(5)

        # Rest
        kbd.press('x')
        kbd.release('x')

        # Loot
        loot()

        # Rebuff
        if counter % rebuff_after == 0:
            buff(kbd)

        heal(kbd, key)

        print(f'Loop nr {counter}')
        counter += 1
