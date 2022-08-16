import pyautogui


def find_window(name):
    all_windows = pyautogui.getAllWindows()

    for win in all_windows:
        if name.lower() in win.title.lower():
            win.activate()
            win.restore()
            # pyautogui.moveTo(50, 50)
            return win

    return None
