from tkinter import *

root=Tk()

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

root.geometry(f"{width}x{height}")
root.title("code icon customize")
root.wm_iconbitmap("ic.ico")

root.mainloop()