from tkinter import *

def click(event):
    text= event.widget.cget("text")
    print(text)
    

root = Tk()
root.geometry("400x600")
root.title("calculator using Tkinter")
root.wm_iconbitmap("calculator.ico")

scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=8, padx=10)


f1 = Frame(root, bg="grey")
b1=Button(f1, text="9", font="lucida 25 bold",padx=15, pady=10)
b1.pack(side=LEFT,padx=15,pady=10)
b1.bind("<Button-1>", click)
b1=Button(f1, text="8", font="lucida 25 bold",padx=15, pady=10)
b1.pack(side=LEFT,padx=15,pady=10)
b1.bind("<Button-1>", click)
b1=Button(f1, text="7", font="lucida 25 bold",padx=15, pady=10)
b1.pack(side=LEFT,padx=15,pady=10)
b1.bind("<Button-1>", click)
f1.pack()

root.mainloop()