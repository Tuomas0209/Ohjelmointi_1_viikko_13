"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self, count=0):
        self.__main_window = Tk()

        self.__count = count

        self.__current_value = Label(self.__main_window, text=self.__count)
        self.__current_value.pack()

        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset)
        self.__reset_button.pack(side=BOTTOM)

        self.__increase_button = Button(self.__main_window, text="Increase",
                                        command=self.increase)
        self.__increase_button.pack(side=BOTTOM)

        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command = self.decrease)
        self.__decrease_button.pack()


        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.terminate)
        self.__quit_button.pack()
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.
        self.__main_window.mainloop()

    def reset(self):
        self.__count = 0
        self.__current_value.configure(text=self.__count)

    def increase(self):
        self.__count += 1
        self.__current_value.configure(text=self.__count)

    def decrease(self):
        self.__count -= 1
        self.__current_value.configure(text=self.__count)

    def terminate(self):
        self.__main_window.destroy()




def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
