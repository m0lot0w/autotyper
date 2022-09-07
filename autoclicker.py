import pyautogui
import time

message1 = input("[ + ] * Phrase / lettre\n")
message2 = input("[ + ] * Rapidité de clique (temp d'interval)\n")
message3 = int(input("[ + ] * Nombre de fois à envoyer\n"))
temps = float(message2)
time.sleep(1)
for i in range(message3):
    time.sleep(temps)
    pyautogui.typewrite(message1)
    pyautogui.press('enter')
