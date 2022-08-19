from bot_scripts import bot_1
from window_handling import find_window


def main():
    window = find_window('Talisman')
    if window:
        bot_1.bot()


if __name__ == '__main__':
    main()
