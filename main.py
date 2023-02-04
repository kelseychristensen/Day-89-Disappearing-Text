from tkinter import *
from tkinter import ttk

window = Tk()

def countdown():
    window.after(20, countdown)
    time_remaining['value'] += 1
    if time_remaining['value'] < 70:
        s.configure("bar.Horizontal.TProgressbar", background='forest green')
    if time_remaining['value'] >= 70:
        s.configure("bar.Horizontal.TProgressbar", background='yellow green')
    if time_remaining['value'] >= 75:
        s.configure("bar.Horizontal.TProgressbar", background='gold')
    if time_remaining['value'] >= 80:
        s.configure("bar.Horizontal.TProgressbar", background='orange')
    if time_remaining['value'] >= 85:
        s.configure("bar.Horizontal.TProgressbar", background='dark orange')
    if time_remaining['value'] >= 90:
        s.configure("bar.Horizontal.TProgressbar", background='orange red')
    if time_remaining['value'] >= 95:
        s.configure("bar.Horizontal.TProgressbar", background='red')
    if time_remaining['value'] >= 100:
        typing.delete("1.0", END)

def stop_countdown(e):
    time_remaining.stop()


window.title("Writer Unblock")
window.geometry("1200x800")

s = ttk.Style()
s.theme_use('clam')
s.configure("bar.Horizontal.TProgressbar", foreground='white', troughcolor='white', background='forest green',
            bordercolor='white')
time_remaining = ttk.Progressbar(window, style="bar.Horizontal.TProgressbar", length=1200, maximum=99.9)
time_remaining.place(x=0, y=0, height=15)

typing = Text(width=95, height=780, pady=25, padx=25, font=('Microsoft YaHei Light', 16))
typing.place(x=0, y=20)
typing.focus()

countdown()
window.bind('<KeyPress>', stop_countdown)

window.mainloop()
