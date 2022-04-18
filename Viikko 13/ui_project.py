"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

The function of the program may be quite simple, but the user interface is
in my opinion advanced. The UI also allows for scalability (ie. no magic
numbers, the number of inventory items is "not set in stone". )
"""

from tkinter import *
import random

DEFAULTS = [("Hand", "hand.gif"), ("Body", "body.gif"), ("Bare", "bare.gif")]

WEAPONS = [("Sword", "sword.gif"), ("Gun", "gun.gif"),
           ("Light saber", "ls.gif")]
ARMOR = [("Heavy armor", "heavy.gif"), ("Light armor", "light.gif")]
FOOTWEAR = [("Boots", "boots.gif"), ("Rollerskates", "rollerskates.gif")]


class CharMod:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.geometry("680x500")
        self.__mainwindow.title("Character customization")

        # Initialize a dictionary for objects of type PhotoImage.
        # This dictionary is used to access the images.

        self.__images = {}

        # Add the images of each hard coded type to the dictionary. The Images
        # are stored in separate lists so that they are easier to handle.

        for (pic, filename) in ARMOR:
            self.__images[pic] = PhotoImage(file=filename)
        for (pic, filename) in WEAPONS:
            self.__images[pic] = PhotoImage(file=filename)
        for (pic, filename) in FOOTWEAR:
            self.__images[pic] = PhotoImage(file=filename)
        for (pic, filename) in DEFAULTS:
            self.__images[pic] = PhotoImage(file=filename)

        # Set string variables for each group of items to be turned into
        # groups of radio buttons. Set the default value of the string
        # variable to "None".

        self.__var1 = StringVar()
        self.__var1.set("None")
        self.__var2 = StringVar()
        self.__var2.set("None")
        self.__var3 = StringVar()
        self.__var3.set("None")

        # Add components to the user interface and place them accordingly
        # using the grid method.

        self.__armor = Label(self.__mainwindow, image=self.__images["Body"])
        self.__armor.grid(row=0, column=1)

        self.__weapon = Label(self.__mainwindow, image=self.__images["Hand"])
        self.__weapon.grid(row=0, column=0, sticky=E)

        self.__footwear = Label(self.__mainwindow, image=self.__images["Bare"])
        self.__footwear.grid(row=1, column=1)

        self.__info = Label(self.__mainwindow, text="Select your gear!"
                                                    "\n\nClick confirm"
                                                    " when ready.")
        self.__info.grid(row=0, column=4, pady=10)

        self.__confirm_button = Button(self.__mainwindow, text="Confirm",
                                       command=self.confirm,
                                       background="green", width=8)
        self.__confirm_button.grid(column=4)

        self.__random_button = Button(self.__mainwindow, text="Random",
                                      command=self.random,
                                      background="yellow", width=8)
        self.__random_button.grid(column=4)

        self.__reset_button = Button(self.__mainwindow, text="Reset",
                                     command=self.reset,
                                     background="orange", width=8)
        self.__reset_button.grid(column=4)

        self.__quit_button = Button(self.__mainwindow, text="Quit",
                                    command=self.stop,
                                    background="red", width=8)
        self.__quit_button.grid(column=4)

        # Initialize a dictionary to add radio buttons into. The dictionary is
        # used to loop through all buttons. Use of dictionary enables the
        # search of a button by its text.

        self.button_list = {}

        # The use of for-loops to create radio buttons out of the inventory
        # items makes it easier for the developer to add more items to the
        # program. This way the developer doesn't need to manually create more
        # buttons. The Hard coded lists could for example be derived from
        # a text file instead. The use of indexing allows for the placement
        # of undetermined number of buttons.

        index = 2

        for (text, weapon) in WEAPONS:
            button = Radiobutton(self.__mainwindow, text=text,
                                 variable=self.__var1,
                                 value=text, indicator=0, width=15,
                                 command=self.change_weapon)
            button.grid(ipady=3, row=index)
            index += 1
            self.button_list[text] = button

        index = 2

        for (text, armor) in ARMOR:
            button = Radiobutton(self.__mainwindow, text=text,
                                 variable=self.__var2,
                                 value=text, indicator=0, width=15,
                                 command=self.change_armor)
            button.grid(ipady=3, row=index, column=1)

            index += 1
            self.button_list[text] = button

        index = 2

        for (text, footwear) in FOOTWEAR:
            button = Radiobutton(self.__mainwindow, text=text,
                                 variable=self.__var3,
                                 value=text, indicator=0, width=15,
                                 command=self.change_footwear)
            button.grid(ipady=3, row=index, column=2)
            index += 1
            self.button_list[text] = button



    def change_weapon(self):
        """
        Changes the weapon image according to the value of the first string
        variable.
        """
        value = self.__var1.get()
        self.__weapon.configure(image=self.__images[value])
        self.set_default_message()

    def change_armor(self):
        """
        Changes the armor image according to the value of the second string
        variable.
        """
        value = self.__var2.get()
        self.__armor.configure(image=self.__images[value])
        self.set_default_message()

    def change_footwear(self):
        """
        Changes the footwear image according to the value of the third string
        variable.
        """
        value = self.__var3.get()
        self.__footwear.configure(image=self.__images[value])
        self.set_default_message()

    def confirm(self):
        """
        Confirms the chosen set of items. Doing that, disables all buttons
        except for the reset button. Also displays a confirmation message
        on the info label.
        """
        weapon = self.__var1.get()
        if weapon == "None":
            weapon = "bare hands"
        armor = self.__var2.get()
        if armor == "None":
            armor = "no armor"
        footwear = self.__var3.get()
        if footwear == "None":
            footwear = "bare feet"

        self.__confirm_button.configure(state=DISABLED)
        self.__random_button.configure(state=DISABLED)

        for name in self.button_list:
            self.button_list[name].configure(state=DISABLED)
            self.button_list[name].deselect()

        self.__info.configure(text=f"You selected {weapon}, {armor} and "
                                   f"{footwear}. \n\n Go get 'em! ")

    def reset(self):
        """
        Resets the buttons, images and the info label to the original state.
        """
        self.set_default_message()

        for name in self.button_list:
            self.button_list[name].configure(state=NORMAL)

        self.__confirm_button.configure(state=NORMAL)
        self.__random_button.configure(state=NORMAL)

        # Set the images back to default

        self.__weapon.configure(image=self.__images["Hand"])
        self.__armor.configure(image=self.__images["Body"])
        self.__footwear.configure(image=self.__images["Bare"])

        # Set the values of the three string variables back to default, "None"

        self.__var1.set("None")
        self.__var2.set("None")
        self.__var3.set("None")

    def random(self):
        """
        Selects random items from each category and displays information on
        the info label. Also selects (pushes down) the buttons accordingly.
        """

        # Get random equipment from each category.

        weapon, _ = WEAPONS[random_index(WEAPONS)]
        armor, _ = ARMOR[random_index(ARMOR)]
        footwear, _ = FOOTWEAR[random_index(FOOTWEAR)]

        # Add the selected items into a list for further use.

        lst = [weapon, armor, footwear]

        # Update the images accordingly using the self.__images dict.

        self.__weapon.configure(image=self.__images[weapon])
        self.__armor.configure(image=self.__images[armor])
        self.__footwear.configure(image=self.__images[footwear])

        # Select the appropriate buttons so that they are pushed down.

        for button in lst:
            self.button_list[button].select()

        # Update the info label to display information about the
        # randomization

        self.__info.configure(text=f"You randomized {weapon}, {armor} and "
                                   f"{footwear}.")

    def set_default_message(self):
        """
        This method is used to restore the info label to its default state.
        """
        self.__info.configure(text="Select your gear!"
                                   "\n\nClick confirm"
                                   " when ready.")

    # def random_reply(self):

        # I like the way this looks!
        # Hope you know what you're doing.


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

    # def read_file(self):


def random_index(array):
    return random.randint(0, len(array) - 1)


def main():
    ui = CharMod()
    ui.start()


if __name__ == "__main__":
    main()
