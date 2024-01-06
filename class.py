from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry ("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN,anchor="w").pack(fill=X,side=BOTTOM)

    def craeteButton(self,intext):
        Button(text=intext, command=self.click).pack()

    def click(self):
        print("Button has clicked")

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.craeteButton("click here")
    window.mainloop()