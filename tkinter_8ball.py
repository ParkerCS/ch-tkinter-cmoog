# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)

'''I changed the font, the border of the title, and the foregroud/background colors.  '''
from tkinter import *
from tkinter import font
import random
class App():
    def __init__(self, master):
        # fonts
        self.title_font = font.Font(family="Times", size=20, weight=font.BOLD)
        self.entry_text = DoubleVar()
        self.entry_text.set("")

        self.answer_text = DoubleVar()
        self.answer_text.set("Your Fortune Here")

        self.answer_text_options = ["Yes!", "Not a change", "No way!", "Most likely", "Probably?", "I wouldn't be surprised...", "Maybe", 'Without a doubt', 'I wouldn\'t count on it', 'Ask again later']

        self.instructions = Label(master, text="Enter a \"yes or no\" question below:")
        self.instructions.grid(column=1, row=2)

        self.entry = Entry(master, textvariable=self.entry_text)
        self.entry.grid(column=1, row=3)

        self.answer = Button(master, text="Shake the ball!", command=lambda: self.button_hit())
        self.answer.grid(column=4, row=3)

        self.title = Label(master, text="Magic 8-ball", font=self.title_font, bg="black", relief='raised', borderwidth=4, fg="white")

        self.title.grid(column=1, row=1, columnspan=10, sticky='e'+'w')

        self.answer_label = Label(master, textvariable=self.answer_text)
        self.answer_label.grid(column=1, row=4)

    def button_hit(self):
        self.entry_text.set("")
        self.answer_text.set(self.answer_text_options[random.randrange(len(self.answer_text_options))])
if __name__ == "__main__":
    root = Tk()
    my_app = App(root)
    root.mainloop()