from tkinter import *
import tkinter as tk 

import filetransferapp


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define max and min size of frame
        self.master = master
        self.master.minsize(500, 230)
        self.master.maxsize(500, 230)
        # gives the master frame a name
        self.master.title("Daily File Transfer")
        #background color
        self.master.configure(bg="lightpink")

        filetransferapp.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()