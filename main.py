import webbrowser
import tkinter as tk
from tkinter import *
import random
import linecache
import time


root = tk.Tk()
root.title("Alarm")
root.geometry("500x150")

label1 = tk.Label(root, text="Enter the time in the format HH:MM")
label1.pack()

global entry1
entry1 = tk.Entry(root)
entry1.pack()

def addZeros(time):
    try:
        hour = int(time[0:2])
    except:
        hour = int(time[0:1].zfill(2))
        try:
            minute = int(time[2:4])
            return minute,hour
        except:
            minute = int(time[2:3].zfill(2))
            return minute, hour


    try:
        minute = int(time[3:5])
    except:
        minute = int(time[3:4].zfill(2))

    return minute,hour

def getDifference():

    global entry1

    alarmTime = str(entry1.get())

    alarmMin,alarmHour = addZeros(alarmTime)
    secTill = int(time.strftime("%S"))

    if secTill == 0:
        minTill = alarmMin - (int(time.strftime("%M")) + 1)
    else:
        minTill = alarmMin - int(time.strftime("%M"))

    if minTill != 0:
        if (alarmHour - int(time.strftime("%H"))) > 0:
            hourTill = alarmHour - int(time.strftime("%H"))
        else:
            hourTill = alarmHour - (int(time.strftime("%H")) + 1)
    else:
        hourTill = alarmHour - int(time.strftime("%H"))

    if hourTill < 0:
        hourTill = hourTill + 24
    if minTill < 0:
        minTill = minTill + 60
    if secTill < 0:
        secTill = secTill + 60

    timeTill = str(hourTill) + ":" + str(minTill) + ":" + str(secTill)

    entry1 = timeTill

    findTime()

def findTime():

    global entry1

    timeLeft = entry1
    print(entry1)

    minLeft,hourLeft = addZeros(timeLeft)

    if len(timeLeft) > 6:
            secLeft = (timeLeft[6:].zfill(2))
    elif len(timeLeft) < 7:
        try:
            secLeft = int(timeLeft[4:].zfill(2))
        except:
            secLeft = int(timeLeft[5:].zfill(2))

    secLeft = int(secLeft)


    if secLeft != 0:
        secLeft = secLeft - 1
    else:
        secLeft = 59
        minLeft = minLeft - 1

    if minLeft == 0 and hourLeft != 0:
        hourLeft = hourLeft - 1
        minLeft = 59


    timeTill = str(hourLeft) + ":" + str(minLeft) + ":" + str(secLeft)
    entry1 = timeTill

    label2.config(text=timeLeft)

    if hourLeft == 0 and minLeft == 0 and secLeft == 0:
        randomLine = random.randint(0,2)
        randomUrl = linecache.getline("links", randomLine)
        webbrowser.open_new(randomUrl)
        root.destroy()


    label1.after(1000,findTime)

enterButton = Button(root, text="Enter", width=10,command=getDifference)
enterButton.pack()

label2 = tk.Label(root, text="Time Until alarm",font=("Ariel",40),fg="green",bg ="black")
label2.pack()

root.mainloop()


