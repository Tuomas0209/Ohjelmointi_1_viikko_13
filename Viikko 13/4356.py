from tkinter import *
import functools

class practice:
    def __init__(self):
        self.__mw = Tk()
        self.__buttons = {}

        for i in range(4):
            button = Label(self.__mw, text="")
            button.pack()
            self.__buttons[i] = button

        print(self.__buttons)
        self.__mw.mainloop()

a = practice()

