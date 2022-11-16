import sys
import time
from threading import Thread

from pynput.mouse import Button, Controller as MController
from pynput.keyboard import Key, Controller as KController, Listener as KListener

from bot_scripts.fay import fay_1
from bot_scripts.tamer import tamer_1
from bot_scripts.monk import monk_1
from screen_scan.template_match import match_template

keyboard_ = KController()
mouse = MController()


def brute_force_loot(res='1440p'):
    '''Looting function'''
    # TODO - get the latest coords from miluto pc
    if res == '1440p':
        left = 1000
        right = 1600
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

    # Check for loot box and pick up if there is one
    pick_up_btn = match_template()
    if pick_up_btn is not None:
        mouse.position = pick_up_btn
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.05)


def listen(key):
    '''Listener for key presses'''
    if key == Key.f4:
        print('exiting')
        sys.exit()


def bot():
    '''Start the bot and the key listener'''
    bot = Thread(target=tamer_1, args=(keyboard_, Key, brute_force_loot), daemon=True)
    bot.start()

    with KListener(on_press=listen) as listener:
        listener.join()
