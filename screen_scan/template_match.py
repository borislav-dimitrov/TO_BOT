import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab


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


def match_template(source=None, needle=None, perc_match=0.98):
    '''Look for needle image in source image, if found return its center coordinates'''
    if not source:
        source = take_screenshot()
    if not needle:
        needle = cv2.imread(r'screenshots/match/match_5.png')

    match = cv2.matchTemplate(source, needle, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    if max_val > perc_match:
        w = needle.shape[1] // 2
        h = needle.shape[0] // 2

        cv2.rectangle(source, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
        return max_loc[0] + w, max_loc[1] + h


def take_screenshot(x1=0, y1=0, w=2550, h=1200):
    time.sleep(2)
    image = pyautogui.screenshot(region=(x1, y1, w, h))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image


def save_img(img, path):
    """Save given image to the given path"""
    cv2.imwrite(path, img)
    return img


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


def get_point_color(x, y):
    """Get the color at specific point"""
    image = ImageGrab.grab()
    return image.getpixel((x, y))


def check_hp():
    healthy_color = (157, 0, 1)
    current = get_point_color(200, 72)
    if healthy_color == current:
        return True
    return False


def check_mp():
    mp_color = (0, 43, 82)
    current = get_point_color(200, 81)
    if mp_color == current:
        return True
    return False


def check_resources(hp=True, mp=True):
    result = {}
    if hp:
        result['HP'] = check_hp()
    if mp:
        result['MP'] = check_mp()

    return result


def debug_():
    """Function for testing stuff in it"""
    pass
