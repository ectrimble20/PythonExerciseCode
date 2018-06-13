import tkinter


def click():
    entered_text = text_entry.get()
    # output.delete(0, 0)  # this clears the text
    output.insert(tkinter.END, entered_text)


def clear_text():
    output.delete(0.0, tkinter.END)


window = tkinter.Tk()
window.title("This is a test GUI thing")
window.configure(background="black")

tkinter.Label(window, text="This is some text I'd like to appear on the screen", bg="black", fg="white",
              font="none 12 bold").grid(row=1, column=1, sticky=tkinter.W)

text_entry = tkinter.Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=1, sticky=tkinter.W)

tkinter.Button(window, text="Submit", width="8", command=click).grid(row=3, column=0)  # , sticky=tkinter.W)
tkinter.Button(window, text="Clear", width="8", command=clear_text).grid(row=3, column=1)  # , sticky=tkinter.W)
tkinter.Button(window, text="Exit", width="8", command=quit).grid(row=3, column=2)  # , sticky=tkinter.W)

output = tkinter.Text(window, width=90, height=4, wrap=tkinter.WORD, background="white")
output.grid(row=4, rowspan=2, column=0, columnspan=3, sticky=tkinter.W)

window.mainloop()
