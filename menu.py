from tkinter import *

def myfunc():
    print("kya be kya dekhta hai")

root = Tk()
root.title("Eventes of python")

root.geometry("600x600")

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)
yourmenu = Menu(root)

m1 = Menu(yourmenu, tearoff=0)
m1.add_command(label="save", command=myfunc)
m1.add_command(label="new", command=myfunc)
m1.add_separator()
m1.add_command(label="print", command=myfunc)
m1.add_command(label="save as", command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File", menu=m1)

root.mainloop()