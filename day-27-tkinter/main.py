from tkinter import *

from PIL.ImageOps import expand

window = Tk()

window.title(string="My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text, highlightcolor="yellow")

button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.grid(column=1, row=1)
button.grid(column=1, row=1)

# new Button
button_2 = Button(text="New Button")
button_2.grid(column=2, row=0)

# Entry

input = Entry(width=15)
# print(input.get())
# input.pack()
input.grid(column=3, row=2)



window.mainloop()
