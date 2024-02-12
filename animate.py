
import cv2
import numpy as np
import pyautogui
import time
import os

# Список слайдов
slides = [
r"""
🤍
🤍
🤍
""", r"""
🤍🤍
🤍🤍
🤍🤍
🤍🤍
""", r"""
🤍🤍🤍
🤍🤍🤍
🤍🤍🤍
🤍🤍🤍
🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍🤍💖💖💖🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
🤍💖💖💖💖💖🤍
🤍🤍💖💖💖🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
🤍💖💖💖💖💖🤍
🤍🤍💖💖💖🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
🤍💖💖💖💖💖🤍
🤍🤍💖💖💖🤍🤍
🤍🤍🤍💖🤍🤍🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
🤍💖💖💖💖💖🤍
🤍🤍💖💖💖🤍🤍
""", r"""
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
🤍💖💖💖💖💖🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
🤍💖💖💖💖💖🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🤍💖🤍🤍
""", r"""
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍

""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍💕💕🤍
🤍💕🤍🤍💕💕🤍
🤍💕🤍💕🤍💕🤍
🤍💕🤍💕🤍💕🤍
🤍💕💕🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍💕🤍🤍
🤍💕🤍💕🤍🤍🤍
🤍💕💕🤍🤍🤍🤍
🤍💕🤍💕🤍🤍🤍
🤍💕🤍🤍💕🤍🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💕🤍🤍🤍
🤍🤍💕🤍💕🤍🤍
🤍🤍💕🤍💕🤍🤍
🤍💕🤍🤍🤍💕🤍
🤍💕💕💕💕💕🤍
🤍💕🤍🤍🤍💕🤍
🤍💕🤍🤍🤍💕🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖💖💖🤍
🤍💖🤍🤍🤍💖🤍
🤍💖🤍🤍🤍💖🤍
🤍🤍💖💖💖💖🤍
🤍🤍🤍💖🤍💖🤍
🤍🤍💖🤍🤍💖🤍
🤍💖🤍🤍🤍💖🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💖💖💖💖💖🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍💖🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💖💖💖💖💖🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖💖💖💖🤍🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖💖💖💖💖🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💖💖💖💖💖🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖🤍🤍🤍🤍🤍
🤍💖💖💖💖🤍🤍
🤍💖🤍🤍🤍💖🤍
🤍💖🤍🤍🤍💖🤍
🤍💖💖💖💖🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖💖💖🤍
🤍💖🤍🤍🤍💖🤍
🤍💖🤍🤍🤍💖🤍
🤍🤍💖💖💖💖🤍
🤍🤍🤍💖🤍💖🤍
🤍🤍💖🤍🤍💖🤍
🤍💖🤍🤍🤍💖🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💗💗💗🤍🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍🤍💗💗💗🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💗💗💗💗💗🤍
🤍💗🤍🤍🤍🤍🤍
🤍💗🤍🤍🤍🤍🤍
🤍💗💗💗💗🤍🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗💗💗💗🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💗💗💗🤍🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍🤍💗💗💗🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍🤍💗💗💗🤍🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍💗🤍💗🤍🤍
🤍🤍💗🤍💗🤍🤍
🤍💗🤍🤍🤍💗🤍
🤍💗💗💗💗💗🤍
🤍💗🤍🤍🤍💗🤍
🤍💗🤍🤍🤍💗🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💗🤍💗💗💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗💗💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗🤍💗🤍
🤍💗🤍💗💗💗🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍💖🤍🤍🤍💖🤍
💖💕💕💕💕💕💖
💕💕💗💕💗💕💕
💕💗💗💗💗💗💕
💕💗💗💗💗💗💕
💕💕💗💗💗💕💕
💖💕💕💗💕💕💖
🤍💖💕💕💕💖🤍
🤍🤍💖💕💖🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍💕💕💕💕💕🤍
💕💕💗💕💗💕💕
💕💗💗💗💗💗💕
💕💗💗💗💗💗💕
💕💕💗💗💗💕💕
🤍💕💕💗💕💕🤍
🤍🤍💕💕💕🤍🤍
🤍🤍🤍💕🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💗🤍💗🤍🤍
🤍💗💗💗💗💗🤍
🤍💗💗💗💗💗🤍
🤍🤍💗💗💗🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍💗🤍💗🤍🤍
🤍🤍💗💗💗🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍💗🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍
""", r"""
🤍🤍🤍🤍🤍🤍🤍
""", r"""
Н
""", r"""
Ни
""", r"""
Ник
""", r"""
Ника
""", r"""
Ника, т
""", r"""
Ника, ты
""", r"""
Ника, ты м
""", r"""
Ника, ты мн
""", r"""
Ника, ты мне
""", r"""
Ника, ты мне о
""", r"""
Ника, ты мне оч
""", r"""
Ника, ты мне оче
""", r"""
Ника, ты мне очен
""", r"""
Ника, ты мне очень
""", r"""
Ника, ты мне очень н
""", r"""
Ника, ты мне очень нр
""", r"""
Ника, ты мне очень нра
""", r"""
Ника, ты мне очень нрав
""", r"""
Ника, ты мне очень нрави
""", r"""
Ника, ты мне очень нравиш
""", r"""
Ника, ты мне очень нравишь
""", r"""
Ника, ты мне очень нравишьс
""", r"""
Ника, ты мне очень нравишься
""", r"""
Ника, ты мне очень нравишься 💕
""", r"""
Ника, ты мне очень нравишься 💕💖
""", r"""
Ника, ты мне очень нравишься 💕💖💗
""", r"""
Ника, ты мне очень нравишься 💕💖💗

- Сеня
"""
]

# Время задержки между слайдами в секундах
delay = 0.5

def clear_screen():
    # Очистка экрана (работает на большинстве систем)
    os.system('cls' if os.name == 'nt' else 'clear')

def display_slide(slide):
    # Вывод слайда в консоль
    print(slide)

# Проигрывание анимации
for slide in slides:
    clear_screen()
    display_slide(slide)
    time.sleep(delay)