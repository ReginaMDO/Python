import pyautogui
import time
import platform

def open_edge():
    system_platform = platform.system()

    if system_platform == "Windows":
        # Pressiona a tecla Win para abrir o menu Iniciar
        pyautogui.press("win")
        # Espera 1s para abrir o menu Iniciar
        time.sleep(1) 
        # Digita "chrome" e pressiona Enter para abrir o Chrome
        pyautogui.write("edge")
        pyautogui.press("enter")

open_edge()
