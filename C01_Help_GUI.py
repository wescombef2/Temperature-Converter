"""
Temperature Converter
Component 01 - Help GUI
Version 1.0
Finn Wescombe
21/06/21
"""

from tkinter import *
from functools import partial # To Prevent Unwanted Windows

# Main Converter GUI Class
class Converter:
    # Initialize Function
    def __init__(self):
        # Define Format Variables
        bg_colour = "grey"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=bg_colour,
                                     padx=10, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (Row 0)
        self.temp_converter_heading_label = Label(self.converter_frame,
                                                text="Temperature Converter",
                                                  font=("Arial", "16", "bold"),
                                                  bg=bg_colour,
                                                  padx=10, pady=10)
        self.temp_converter_heading_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    # Help Function
    def help(self):
        # Define Format Variables
        bg_colour = "grey"
        self.help = Label(self.converter_frame,
                          text="You have the Charisma of a Damp Rag, and the Appearance of a Low-Grade Bank Clark!",
                          font=("Times New Roman", "10", "bold"),
                          bg=bg_colour,
                          padx=20, pady=200)
        self.help.grid(row=2)
        get_help = Help(self)
        get_help.help_text.configure(text="Help Text Goes Here")


# Help GUI Class
class Help:
    # Initialize Function
    def __init__(self, partner):
        # Define Format Variables
        bg_colour = "grey"

        # Disable Help Button
        partner.help_button.configure(state=DISABLED)

        # Create Window
        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss_help, partner))

        # Help Screen GUI
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=bg_colour)
        self.help_frame.grid()

        # Help Heading (Row 0)
        self.help_heading_label = Label(self.help_frame,
                                        text="Help/Instructions",
                                        font=("Arial", "16", "bold"),
                                        bg=bg_colour,
                                        padx=10, pady=10)
        self.help_heading_label.grid(row=0)

        # Help Text (Label, Row 1)
        self.help_text = Label(self.help_frame,
                               text="",
                               justify=LEFT,
                               width=40,
                               bg=bg_colour,
                               wrap=250)
        self.help_text.grid(row=1)
        # Help Button (Row 1)
        self.dismiss_button = Button(self.help_frame,
                                     text="Dismiss",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     width=10,
                                     command=partial(self.dismiss_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    # Dismiss Help Function
    def dismiss_help(self, partner):
        # Re-enable Help Button
        partner.help_button.configure(state=NORMAL)
        # Close Window
        self.help_box.destroy()

# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
