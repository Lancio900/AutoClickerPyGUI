import pyautogui
import keyboard
import threading
import time

print("Benvenuto su AutoClickerPy.")
print("Per avviare i clic con il tasto sinistro, premere 'K', per stoppare premere 'L'")
print("Per avviare i clic con il tasto destro, premere 'N', per stoppare premere 'M'")

# Imposta il CPS desiderato
cps = 100  # Clic al secondo desiderati
interval = 1.0 / cps  # Intervallo di tempo tra i clic per ottenere cps clic al secondo

# Variabili di controllo per i cicli
left_clicking = False
right_clicking = False

def auto_clicker(button):
    global left_clicking, right_clicking
    if button == 'left':
        clicking = left_clicking
        print("AutoClicker per tasto sinistro avviato. Premere 'L' per stoppare.")
    else:
        clicking = right_clicking
        print("AutoClicker per tasto destro avviato. Premere 'M' per stoppare.")

    next_click = time.time()
    while (left_clicking if button == 'left' else right_clicking):
        pyautogui.click(button=button)
        next_click += interval
        sleep_time = next_click - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
    if button == 'left':
        print("AutoClicker per tasto sinistro fermato.")
    else:
        print("AutoClicker per tasto destro fermato.")

def start_left_clicking():
    global left_clicking
    if not left_clicking:  # Evita di avviare più thread
        left_clicking = True
        thread = threading.Thread(target=auto_clicker, args=('left',))
        thread.start()

def stop_left_clicking():
    global left_clicking
    left_clicking = False

def start_right_clicking():
    global right_clicking
    if not right_clicking:  # Evita di avviare più thread
        right_clicking = True
        thread = threading.Thread(target=auto_clicker, args=('right',))
        thread.start()

def stop_right_clicking():
    global right_clicking
    right_clicking = False

# Configurazione di pyautogui per migliorare la velocità
pyautogui.PAUSE = 0  # Disabilita il ritardo tra le chiamate di pyautogui
pyautogui.MINIMUM_DURATION = 0  # Disabilita la durata minima del movimento del mouse

# Binding degli eventi di tastiera
keyboard.add_hotkey('K', start_left_clicking)
keyboard.add_hotkey('L', stop_left_clicking)
keyboard.add_hotkey('N', start_right_clicking)
keyboard.add_hotkey('M', stop_right_clicking)

# Manteniamo lo script in esecuzione
keyboard.wait('esc')
print("Script terminato.")
