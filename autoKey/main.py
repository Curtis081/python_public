import pyautogui
import time
import datetime


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def enable_click_time():
    morning_start = datetime.time(9, 0, 0, 0)
    morning_end = datetime.time(12, 0, 0, 0)
    afternoon_start = datetime.time(13, 0, 0, 0)
    afternoon_end = datetime.time(18, 0, 0, 0)

    now = datetime.datetime.now().time()
    enable = time_in_range(morning_start, morning_end, now) | time_in_range(afternoon_start, afternoon_end, now)

    return enable


def mouse_left_click_demo():
    delay_time = 4 * 60

    target_mouse_X, target_mouse_Y = pyautogui.position()

    key = input('press key \'p\', move the mouse and press ENTER to set the position:')
    if key == 'p':
        target_mouse_X, target_mouse_Y = pyautogui.position()
        print(target_mouse_X, target_mouse_Y)

    while True:
        if enable_click_time():
            current_mouse_X, current_mouse_Y = pyautogui.position()
            pyautogui.click(target_mouse_X, target_mouse_Y)
            print('mouse left click')
            pyautogui.moveTo(current_mouse_X, current_mouse_Y)
        else:
            pass
        print(time.ctime())
        time.sleep(delay_time)


if __name__ == '__main__':
    mouse_left_click_demo()
