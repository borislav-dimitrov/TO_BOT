import cv2
import numpy as np
import pyautogui
import time

Y_OFFSET = 150


def _loot(coords):
    for coord in coords:
        pyautogui.moveTo(coord[0], coord[1])
        pyautogui.keyDown('shift')
        pyautogui.click(interval=0.5, button='right')
        pyautogui.keyUp('shift')
        pyautogui.moveTo(50, 50)


def _loot_at_coords(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.keyDown('shift')
    pyautogui.click(button='right')
    pyautogui.keyUp('shift')


def img_prev(img):
    cv2.imshow('Image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def match_template():
    '''Make screenshot, look for the needle image in it, if found return its center coordinates'''
    source_img = take_screenshot()
    needle_img = cv2.imread('.\\screenshots\\match\\match_5.png')
    match = cv2.matchTemplate(source_img, needle_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    if max_val > 0.98:
        w = needle_img.shape[1] // 2
        h = needle_img.shape[0] // 2

        cv2.rectangle(source_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
        return max_loc[0] + w, max_loc[1] + h + Y_OFFSET


def take_screenshot():
    time.sleep(2)
    image = pyautogui.screenshot(region=(0, Y_OFFSET, 2550, 1200))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image


def look_for_circles():
    source_img = take_screenshot()
    needle_img = cv2.imread('.\\screenshots\\match\\match_5.png')

    gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

    min_radius = 30
    max_radius = 35

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=30, param2=20,
                               minRadius=min_radius, maxRadius=max_radius)

    circles_xy = []  # (x, y)
    if circles is not None:
        for i in circles[0, :]:
            cv2.circle(source_img, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), int(2))
            circles_xy.append((int(i[0]), int(i[1]) + Y_OFFSET))

    img_prev(source_img)


def debug_():
    pass
