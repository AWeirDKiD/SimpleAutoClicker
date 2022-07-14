import time
import keyboard
import win32api
import win32con


print("Welcome to SimpleClicker")
print("    -Made by A WeirD KiD#2737")
print("")

bind = input("What do you want to bind the clicker to? ")
print("The Clicker bind is: " + bind)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.003)


while True:
    if keyboard.is_pressed(bind):
        click()
    time.sleep(0.02)