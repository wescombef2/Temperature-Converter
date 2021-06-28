"""
Temperature Converter
Component 02 - Converter GUI
Version 1.0
Finn Wescombe
28/06/21
"""

from tkinter import *
from functools import partial  # To Prevent Unwanted Windows


# Main Converter GUI Class
class Converter:
    # Initialize Function
    def __init__(self):
        # Define Format Variables
        bg_colour = "grey"

        # Converter Main Screen GUI
        self.frame_converter = Frame(width=300, height=300,
                                     bg=bg_colour,
                                     padx=10, pady=10)
        self.frame_converter.grid()

        # Temperature Converter Heading (Row 0)
        self.lbl_converter_heading = Label(self.frame_converter,
                                           text="Temperature Converter",
                                           font=("Arial", "16", "bold"),
                                           bg=bg_colour,
                                           padx=10, pady=10)
        self.lbl_converter_heading.grid(row=0)

        # Instruction Label (Row 1)
        self.lbl_instructions = Label(self.frame_converter,
                                      text="Type in the amount to be converted "
                                           "then push one of the buttons below "
                                           "to convert.",
                                      font=("Arial", "10", "italics"),
                                      wrap=250,
                                      justify=LEFT,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_instructions.grid(row=1)

        # Entry Box (Row 2)

        # Conversion Buttons Frame (Row 3)
        self.frame_convert_btns = Frame(width=300, height=50,
                                        bg="light red",
                                        padx=10, pady=10)
        self.frame_convert_btns.grid(row=3)

        # Centigrade and Fahrenheit Buttons (CBF - Row 0)

        # Conversion Result (Row 4)

        # Help/History Buttons Frame (Row 5)
        self.frame_help_history = Frame(width=300, height=50,
                                        bg="blue",
                                        padx=10, pady=10)
        self.frame_help_history.grid(row=3)

        # Help Button (HHBF - Row 0)
        self.help_button = Button(self.frame_help_history,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

        # History Button (HHBF - Row 0)

    # Get Help Function
    def help(self):
        # Define Format Variables
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
