import time
import pyautogui

print('Use ctrl+c to Quit')

try:
	while True:
		pyautogui.click()
		time.sleep(10)
		print('slept for 10 seconds')
except ValueError:
	Pass

