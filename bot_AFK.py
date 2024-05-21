import win32api
import win32con
import pydirectinput
import time
import random

def mover_mouse():
    # Obter as dimensões da telas
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(180)
    # Gerar posições aleatórias
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)

    # Mover o mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, random_x, random_y, 0, 100)

letra = ['w', 'd', 's', 'a']

if __name__ == "__main__":
    try:
        while True:
            time.sleep(3)
            pydirectinput.press(random.choice(letra))
            pydirectinput.press(random.choice(letra))
            pydirectinput.press(random.choice(letra))
            pydirectinput.press(random.choice(letra))
            pydirectinput.click()
            mover_mouse()
    except KeyboardInterrupt:
        print("Bot interrompido pelo usuário.")