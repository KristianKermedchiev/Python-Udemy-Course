from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 500)


# Label

my_label = Label(text="My Label", font=("Helvetica", 15, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label.config(text=input.get())


# Button
button = Button(text="Click me", command=button_clicked)
new_button = Button(text="New Button")

button.grid(column=2, row=0)
new_button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()