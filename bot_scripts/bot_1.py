import sys
import time
from threading import Thread

from pynput.mouse import Button, Controller as MController
from pynput.keyboard import Key, Controller as KController, Listener as KListener

keyboard_ = KController()
mouse = MController()


def brute_force_loot(res='1440p'):
    if res == '1440p':
        left = 900
        right = 1700
        top = 500
        bottom = 1000
    elif res == '1080p':
        left = 700
        right = 1300
        top = 200
        bottom = 800
    else:
        return

    x_coords = []
    y_coords = []

    for x in range(0, right - left, 90):
        x_coords.append(left + x)

    for y in range(0, bottom - top, 80):
        y_coords.append(top + y)

    with keyboard_.pressed(Key.shift):
        for x in x_coords:
            for y in y_coords:
                mouse.position = x, y
                mouse.press(Button.right)
                mouse.release(Button.right)
                time.sleep(0.05)
    keyboard_.press(Key.f1)
    keyboard_.release(Key.f1)
    keyboard_.press(Key.esc)
    keyboard_.release(Key.esc)


def heal():
    keyboard_.press(Key.f1)
    keyboard_.release(Key.f1)
    keyboard_.press('r')
    keyboard_.release('r')
    time.sleep(1.5)


def buff():
    # pyautogui.press('q')
    # time.sleep(1.5)
    keyboard_.press('w')
    keyboard_.release('w')
    time.sleep(1.5)
    # pyautogui.press('e')
    # time.sleep(1.5)


def listen(key):
    if key == Key.f4:
        print('exiting')
        sys.exit()


# region Bots
def tamer_1(rebuff_after=15, rest_for=None, counter=1):
    buff()

    while True:
        keyboard_.press(Key.tab)
        keyboard_.release(Key.tab)
        time.sleep(1)
        keyboard_.press('`')
        keyboard_.release('`')
        time.sleep(1)
        keyboard_.press('1')
        keyboard_.release('1')
        time.sleep(4)
        keyboard_.press('2')
        keyboard_.release('2')
        time.sleep(4)
        keyboard_.press('2')
        keyboard_.release('2')
        time.sleep(5)

        # Rest
        keyboard_.press('x')
        keyboard_.release('x')

        # Loot
        brute_force_loot()

        # Rebuff
        if counter % rebuff_after == 0:
            buff()

        heal()

        print(f'Loop nr {counter}')
        counter += 1


def fay_1(heal_after=1, rest_for=5, counter=1):
    while True:
        keyboard_.press(Key.tab)
        keyboard_.release(Key.tab)
        time.sleep(1)
        keyboard_.press('3')
        keyboard_.release('3')
        time.sleep(3)
        keyboard_.press('3')
        keyboard_.release('3')
        time.sleep(3)
        keyboard_.press('3')
        keyboard_.release('3')

        time.sleep(4)

        # Loot
        brute_force_loot(res='1080p')

        # Heal
        if counter % heal_after == 0:
            heal()

        # Rest
        keyboard_.press('x')
        keyboard_.release('x')
        time.sleep(rest_for)
        print(f'Loop nr {counter}')
        counter += 1


# endregion


def bot():
    # set_listener()
    # listener = KListener(on_press=listen)
    # listener.start()

    bot = Thread(target=fay_1, args=(), daemon=True)
    bot.start()

    with KListener(on_press=listen) as listener:
        listener.join()
