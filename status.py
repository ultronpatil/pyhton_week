from tkinter import *

def upload():
    stavar.set("busy....")
    sbar.update()
    import time
    time.sleep(2)
    stavar.set("ready...")


root=Tk()
root.geometry("455x677")
root.title("stabar tut")

stavar = StringVar()
stavar.set("ready")
sbar = Label(root, textvariable=stavar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="update", command=upload).pack()

root.mainloop()