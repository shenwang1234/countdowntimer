from tkinter import *
import time
import winsound
import tkinter as tk
from tkinter import ttk
paused = False
running = False
def validate(P):
    global paused
    if len(P) == 0 and not paused:
        # empty Entry is ok
        return True
    elif len(P) == 1 and P.isdigit() and not paused:
        # Entry with 1 digit is ok
        return True
    elif len(P) == 2 and P.isdigit() and not paused:
        # Entry with 1 digit is ok
        return True
    else:
        # Anything else, reject it
        return False


root =Tk()
root.title('countdown timer')
root.geometry("420x250") # window size
vcmd = (root.register(validate), '%P')

hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set('00')
minute.set('00')
second.set('00')


def countdown():
    global paused
    global done
    global running
    running = True
    paused = False
    hours=int(hourEntry.get())
    minutes=int(minuteEntry.get())
    secs=int(secondEntry.get())
    if (secs==0 and minutes==0 and hours==0):
        return
    done = False
    while not done and not paused :

        if secs<=0 and minutes>0:
            minutes -=1
            secs = 60
        elif secs<=0 and minutes<=0 and hours>0:
            hours -= 1
            minutes += 59
            secs = 60

        time.sleep(0.001)
        secs -= 1
        hour.set('{0:2d}'.format(hours))
        minute.set('{0:2d}'.format(minutes))
        second.set('{0:2d}'.format(secs))
        root.update()

        if secs == 0 and minutes == 0 and hours == 0:    # used to fix counter ending at 01 secs
            winsound.Beep(440,500)
            done = True
            hour.set('00')
            minute.set('00')
            second.set('00')
            running = False

#https://www.tutorialspoint.com/how-do-i-create-an-automatically-updating-gui-using-tkinter-in-python


hourEntry = Entry(root, width = 3, font = 'Garamond',validate="key", validatecommand=vcmd, textvariable=hour)
minuteEntry = Entry(root, width = 3, font = 'Garamond',validate="key", validatecommand=vcmd, textvariable=minute)
secondEntry = Entry(root, width = 3, font = 'Garamond',validate="key", validatecommand=vcmd, textvariable=second)
hourEntry.grid(row=1, column=1, padx=10, pady=10)
minuteEntry.grid(row=1, column=2, padx=10, pady=10)
secondEntry.grid(row=1, column=3, padx=10, pady=10)


def reset():
    global done
    global running
    running = False
    done=True
    hour.set('00')
    minute.set('00')
    second.set('00')



def update(hours,minutes,secs):
    # actions to perform
    hour.set('{0:2d}'.format(hours))
    minute.set('{0:2d}'.format(minutes))
    second.set('{0:2d}'.format(secs))
    root.after(10, update) #iterative


def pause():
    global  paused
    global running
    if not paused and running:
        paused=True
        button_pause.config(text="resume")
        root.update()
    elif paused and running:
        paused = False
        button_pause.config(text="pause")
        countdown()


button_start = Button(root, text = "start", padx=40, pady = 20, command = countdown)
button_reset = Button(root, text = "reset", padx=40, pady = 20, command = reset)
button_pause = Button(root, text = "pause", padx=40, pady = 20, command = pause)


button_start.grid(row=7, column=1, padx=10, pady=10)
button_reset.grid(row=7, column=2, padx=10, pady=10)
button_pause.grid(row=7, column=3, padx=10, pady=10)
root.mainloop()
