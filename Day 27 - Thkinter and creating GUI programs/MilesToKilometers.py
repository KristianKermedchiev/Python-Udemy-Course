from tkinter import *

window = Tk()
window.title("Mile to kilometers converter")
window.minsize(200, 200)
window.config(padx=100, pady=100)
# Entry

entry = Entry(width=10)
entry.grid(column=1, row=0)


# Label

label = Label(text="miles")
label.grid(column=2, row=0)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

km_label = Label(text="kilometers")
km_label.grid(column=2, row=1)

result_label = Label(text="")
result_label.grid(column=1, row=1)

# Button


def calculate():
    x = entry.get()
    result_label.config(text=(int(x) * 1.609344))


button = Button(text="calculate", command=calculate)
button.grid(column=1, row=3)




window.mainloop()