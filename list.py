from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root =Tk()
root.geometry("455x233")
root.title("Listbox tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"first item of list box")

Button(root, text="Add", command=add).pack()

root.mainloop()