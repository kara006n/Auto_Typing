import pyautogui
import time

delay = 10 
time.sleep(delay)


name = r"C:\Users\Lenovo\Desktop\VScode/code.txt"  
interval = 0.02   # In Seconds

with open(name) as f:
	data = f.read()
	pyautogui.write(data, interval=interval)
    