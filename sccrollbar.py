from tkinter import *

root=Tk()
root.geometry("455x677")
root.title("scrollbar tut")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT ,fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item {i}")

# listbox.pack(fill=BOTH)

text = Text(root, yscrollcommand = scrollbar.set)
scrollbar.config(command=text.yview)

root.mainloop()