import pyautogui as pg
from tkinter import *

root = Tk()
root.title("CLICKER")
root.geometry("300x200")
root.attributes('-topmost', True)

running = False  # Initialize running as False

def scanning():
    if running:
        pg.click()

    root.after(5, scanning)

def start():
    global running
    running = True
    print("Spam started...")

def stop():
    global running
    running = False
    print("Spam stopped.")

spaceLabel = Label(root)
spaceLabel.pack()

title = Label(root, text="CLICKER V1.2", font="italic")
title.pack()

spaceLabel = Label(root)
spaceLabel.pack()

buttonToStart = Button(root, text="START", command=start)
buttonToStart.pack()

spaceLabel = Label(root)
spaceLabel.pack()

buttonToStop = Button(root, text="STOP", command=stop)
buttonToStop.pack()

spaceLabel = Label(root)
spaceLabel.pack()

root.after(5, scanning)

root.mainloop()