import pyautogui
import time

message1 = input("La Touche\n")
message2 = input("Vitesse de clique\")
message3 = input("Nombre de fois à répéter\n")
temps = float(message2)
time.sleep(1)
for i in range(message3):
    time.sleep(temps)
    pyautogui.typewrite(message1)
