import pyautogui


def find_window(name):
    all_windows = pyautogui.getAllWindows()
    talisman_windows = []

    for win in all_windows:
        if name.lower() in win.title.lower():
            talisman_windows.append(win)

    if talisman_windows:
        talisman_windows.sort(key=lambda x: x._hWnd, reverse=True)
        talisman_windows[0].activate()
        talisman_windows[0].restore()
        return talisman_windows[0]

    return None
