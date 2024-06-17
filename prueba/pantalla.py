
import pyautogui
import time


def maximize_and_minimize():
    # Maximizar la ventana del navegador
    pyautogui.hotkey('win', 'up')
    time.sleep(1)  # Esperar un segundo


while True:
    maximize_and_minimize()
    time.sleep(60)  # Esperar 30 segundos antes de repetir
