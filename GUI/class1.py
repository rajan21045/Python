from tkinter import *


root = Tk()
# creating a label, widget
mylabel1 = Label(root, text="Hey I Am Fine")
mylabel2 = Label(root,text="How Are You?")
mylabel3 = Label(root, text="As Your Wish")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)
mylabel3.grid(row=1,column=1)

def myclick():
    lbl = Label(root,text="Look! I Clicked A Button!")
    lbl.grid(row=2, column=2)

mybutton = Button(root, text="Click Me", padx=20, pady=20, fg="blue", bg="red", command=myclick)
mybutton.grid(row=1, column=3)

root.mainloop()