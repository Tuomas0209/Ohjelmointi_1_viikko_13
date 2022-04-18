from tkinter import *
import functools

class practice:
    def __init__(self,root):
        self.button_list = {}
        self.entry_list = []
        for w in range(5):
            button = Radiobutton(root,text="submit",command=functools.partial(self.enabling, idx=w))
            button.grid(row=w,column=0)
            self.button_list[w] = button
            entry1=Entry(root, state="disabled")
            entry1.grid(row=w,column=1)
            self.entry_list.append(entry1)
        print(self.button_list)
    def enabling(self,idx):
            self.entry_list[idx].config(state="normal")


root = Tk()
a = practice(root)

root.mainloop()