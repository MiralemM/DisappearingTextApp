from tkinter import *
import threading
import time


window = Tk()
window.title("Disappearing Text Writing App")
window.geometry("700x700+150+150")
window.config(padx=50, pady=50)
FLIP_TIMER = None
START_TIME = time.time()
CLOCK = f"0:0:5"
START_TIMER = False
print(START_TIME)


def end_game():
    global START_TIME
    text.delete(1.0, END)
    START_TIME = time.time()


def key_press(a):
    global FLIP_TIMER
    global START_TIME
    global START_TIMER

    if not START_TIMER:
        START_TIMER = True

    if FLIP_TIMER is not None:
        FLIP_TIMER.cancel()
    if a.char == "":
        text.delete("end-2c", END)
    else:
        text.insert(END, a.char)
    START_TIME = time.time()
    FLIP_TIMER = threading.Timer(5.0, end_game)
    FLIP_TIMER.start()


def time_string():
    return f"'0:0:%1.0f' % {5 - (time.time() - START_TIME)}"


def update_timer():
    global START_TIMER
    if START_TIMER:
        clock_label.config(text=time_string())
        clock_label.after(1000, update_timer)


canvas = Canvas(width=1000, height=1000)


text_label = Label(window, text="Once you start typing, if you stop for more than 5 seconds,"
                                "\n this program will delete everything you've written so far.")
text = Text(window, height=20, width=100, bg="white", font=("Arial", 14))
text_label.pack()
text.pack()

window.bind("<Key>", key_press)

clock_label = Label(window, text=f"Time: {CLOCK}", width=10, height=2, justify="center", fg="white", bg="blue",
                    font=("Arial", 16))
clock_label.pack()
clock_label.after(1000, update_timer)

canvas.pack()
window.mainloop()
