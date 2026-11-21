from tkinter import *
from datetime import datetime

root = Tk()
root.title("NekoTime")
root.resizable(False, False)
canvas = Canvas(bg="black", width=250, height=130, highlightthickness=0)
canvas.pack(anchor=CENTER, expand=1)
zero = PhotoImage(file="digits/0.gif")
one = PhotoImage(file="digits/1.gif")
two = PhotoImage(file="digits/2.gif")
three = PhotoImage(file="digits/3.gif")
four = PhotoImage(file="digits/4.gif")
five = PhotoImage(file="digits/5.gif")
six = PhotoImage(file="digits/6.gif")
seven = PhotoImage(file="digits/7.gif")
eight = PhotoImage(file="digits/8.gif")
nine = PhotoImage(file="digits/9.gif")
digits = [zero, one, two, three, four, five, six, seven, eight, nine]
def draw():
    canvas.delete("all")
    time = datetime.now().strftime("%H:%M")
    canvas.create_image(10,10, anchor=NW, image=digits[int(time[0])])
    canvas.create_image(60,10, anchor=NW, image=digits[int(time[1])])
    canvas.create_text(120, 50, text=":", fill="white", font=("Arial", 50, "bold"))
    canvas.create_image(140,10, anchor=NW, image=digits[int(time[3])])
    canvas.create_image(200,10, anchor=NW, image=digits[int(time[4])])
draw()

def update():
    draw()
    root.after(1000, update)

update()
root.mainloop()