import time
from tkinter import Tk, Label, Button, Entry, StringVar
import datetime
import pygame


root = Tk()
root.title("Simple Clock")
root.configure(bg="black")


pygame.mixer.init()


def start():
    text = time.strftime("%I:%M:%S %p")
    label.config(text=text)
    label.after(1000, start)


label = Label(root, font=("Helvetica", 24), bg="black", fg="cyan")
label.grid(row=0, column=1)


def play_sound():
    try:
        pygame.mixer.music.load("sunflower.mp3")
        print("Sound loaded successfully")
        pygame.mixer.music.play()
        print("Playing sound...")
    except pygame.error as e:
        print(f"Error: {e}")


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to coding Now")
            play_sound()
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)


Label(root, text="Hour", font="Helvetica 8 bold", bg="black",
      fg="White").grid(row=1, column=1)
Label(root, text="Minute", font="Helvetica 8 bold", bg="black",
      fg="White").grid(row=2, column=1)
Label(root, text="Second", font="Helvetica 8 bold", bg="black",
      fg="White").grid(row=3, column=1)


hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(root, textvariable=hour, bg="white", fg="black",).grid(row=1, column=2)
Entry(root, textvariable=minute, bg="white", fg="black",).grid(row=2, column=2)
Entry(root, textvariable=second, bg="white", fg="black",).grid(row=3, column=2)


Button(root, text='Set Alarm',
       command=actual_time, bg="green", fg="black",).grid(row=4, column=3)


start()


root.mainloop()
