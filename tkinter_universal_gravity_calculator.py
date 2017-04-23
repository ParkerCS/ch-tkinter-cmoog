# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

'''I added a border to the title -- changed the font to Times New Roman -- and chagned the color of the title'''
from tkinter import *
from tkinter import font
import random
class App():
    def __init__(self, master):
        self.title_font = font.Font(family="Times New Roman", size=15, weight=font.BOLD)
        self.m1 = DoubleVar()
        self.m1.set("5.972e24")
        self.m2 = DoubleVar()
        self.m2.set("50")
        self.radius = DoubleVar()
        self.radius.set("6.371e6")
        self.answer = DoubleVar()


        self.title = Label(master, text="Gravity Calculator", font=self.title_font, relief='raised', borderwidth=4, fg='red')
        self.title.grid(column=1, row=1, columnspan=2)

        self.m1_label = Label(master, text="Mass of 1st Obj (kg)")
        self.m1_label.grid(column=1, row=2)

        self.m1_entry = Entry(master, textvariable=self.m1)
        self.m1_entry.grid(column=2, row=2)

        self.m2_label = Label(master, text="Mass of 2nd Obj (kg)")
        self.m2_label.grid(column=1, row=3)

        self.m2_entry = Entry(master, textvariable=self.m2)
        self.m2_entry.grid(column=2, row=3)

        self.radius_label = Label(master, text="Radius (m)")
        self.radius_label.grid(column=1, row=4)

        self.radius_entry = Entry(master, textvariable=self.radius)
        self.radius_entry.grid(column=2, row=4)

        self.calc_button = Button(master, text="Calculate Force (N)",
                                  command=lambda: self.calculate())
        self.calc_button.grid(column=1, row=5, columnspan=2)

        #self.earth_mass = Button(master, text="Mass of Earth", command=lambda: master.focus_get().cget("textvariable").set(5.972e24))
        #self.earth_mass.grid(column=3, row=2)

        self.answer_label = Label(master, textvariable=self.answer)
        self.answer_label.grid(column=1, row=6, columnspan=2)

    def calculate(self):
        g = 6.67 * (10 ** -11)
        self.answer.set((g * self.m1.get() * self.m2.get()) / (self.radius.get() ** 2))


if __name__ == "__main__":
    root = Tk()
    root.title("Universal Gravity Calculator")
    my_app = App(root)
    root.mainloop()