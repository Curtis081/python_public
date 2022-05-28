import pyautogui
import time


def mouse_left_click_demo():
    delay_time = 4 * 60
    # current_mouse_X, current_mouse_Y = pyautogui.position()
    target_mouse_X, target_mouse_Y = pyautogui.position()

    key = input('press key \'p\', move the mouse and press ENTER to set the position:')
    if key == 'p':
        target_mouse_X, target_mouse_Y = pyautogui.position()
        print(target_mouse_X, target_mouse_Y)

    while True:
        current_mouse_X, current_mouse_Y = pyautogui.position()
        pyautogui.click(target_mouse_X, target_mouse_Y)
        print("%s" % time.ctime())
        print('mouse left click')
        pyautogui.moveTo(current_mouse_X, current_mouse_Y)
        time.sleep(delay_time)


if __name__ == '__main__':
    mouse_left_click_demo()
