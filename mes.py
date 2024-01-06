from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("radio tut")

def order():

    tmsg.showinfo("order received", f"wehave received the {var.get()}")

var = StringVar()
var.set("radio")
Label(root, text="what would you like?",justify=LEFT,font="lucida 19 bold", padx=14).pack()
radio=Radiobutton(root, text="Dosa", padx=14, variable=var,value="Dosa").pack()
radio=Radiobutton(root, text="vada", padx=14, variable=var,value="vada").pack()
radio=Radiobutton(root, text="panner", padx=14, variable=var,value="panner").pack()
radio=Radiobutton(root, text="idali", padx=14, variable=var,value="idali").pack()


Button(text="order now", command=order).pack()
root.mainloop()