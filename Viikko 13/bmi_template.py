"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_value = Entry(self.__mainwindow)
        self.__height_value = Entry(self.__mainwindow)

        self.__weight_label = Label(self.__mainwindow,
                                    text="Enter your weight")
        self.__height_label = Label(self.__mainwindow,
                                    text="Enter your height")
        self.__result_label = Label(self.__mainwindow,
                                    text="Your BMI is:")

        self.__empty_space_1 = Label(self.__mainwindow, text=" ")
        self.__empty_space_2 = Label(self.__mainwindow, text=" ")

        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate", background="Green",
                                         command=self.calculate_BMI)
        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                    command=self.stop)

        self.__result_text = Label(self.__mainwindow, text="Result")
        self.__explanation_text = Label(self.__mainwindow, text="Explanation")

        self.__weight_label.grid(row=0, column=0, columnspan=2, sticky=E + W)
        self.__height_label.grid(row=0, column=4, columnspan=2, sticky=E + W)
        self.__result_label.grid(row=3, column=0, columnspan=2, sticky=E + W)

        self.__empty_space_1.grid(row=0, column=3, columnspan=1, sticky=E + W)
        self.__empty_space_2.grid(row=0, column=5, columnspan=1, sticky=E + W)

        self.__weight_value.grid(row=1, column=0, columnspan=1)
        self.__height_value.grid(row=1, column=4, columnspan=1)

        self.__calculate_button.grid(row=1, column=6, columnspan=1,
                                     sticky=E + W)
        self.__stop_button.grid(row=3, column=6, columnspan=1, sticky=E + W)

        self.__result_text.grid()
        self.__explanation_text.grid(row=4, column=4, columnspan=1,
                                     sticky=E + W)


    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        # weight = float(self.__weight_value.get())
        # height_m = float(self.__height_value.get())/100

        values = self.starting_values()

        if values is None:
            return

        (weight, height) = values

        height_m = height / 100

        try:
            bmi = weight / (height_m * height_m)

        except:
            bmi = 0

        self.__explanation_text.configure(text=self.explanation(bmi))
        self.__result_text.configure(text=f"{bmi:.2f}")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()

    def starting_values(self):
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())
        except:
            self.reset_fields()
            self.__explanation_text.configure(text="Error: height and"
                                                   " weight must be numbers.")
            return

        weight = float(self.__weight_value.get())
        height = float(self.__height_value.get())

        try:
            if weight < 0 or height < 0:
                raise ValueError
        except:
            self.reset_fields()
            self.__explanation_text.configure(text="Error: height and"
                                                   " weight must be positive.")
            return

        return weight, height


def explanation(self, bmi):
    if bmi > 25:
        return "You are overweight."
    elif bmi < 18.5:
        return "You are underweight."
    else:
        return "Your weight is normal."


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
