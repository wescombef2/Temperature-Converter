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
        self.frame_converter = Frame(width=320, height=300,
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
                                      font=("Arial", "10", "italic"),
                                      wrap=250,
                                      justify=LEFT,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_instructions.grid(row=1)

        # Entry Box (Row 2)
        self.entry_to_convert = Entry(self.frame_converter,
                                      width=30,
                                      font=("Arial", "14", "bold"))
        self.entry_to_convert.grid(row=2)

        # Conversion Buttons Frame (Row 3)
        self.frame_convert_btns = Frame(self.frame_converter)
        self.frame_convert_btns.grid(row=3)

        # Centigrade and Fahrenheit Buttons (CBF - Row 0)
        self.btn_centigrade = Button(self.frame_convert_btns,
                                  text="Centigrade",
                                  font=("Arial", "14"),
                                  padx=10, pady=10)
        self.btn_centigrade.grid(row=0, column=1)

        self.btn_fahrenheit = Button(self.frame_convert_btns,
                                  text="Fahrenheit",
                                  font=("Arial", "14"),
                                  padx=10, pady=10)
        self.btn_fahrenheit.grid(row=0, column=2)

        # Conversion Result (Row 4)
        self.lbl_convert_result = Label(self.frame_converter,
                                        text="Conversion goes here...",
                                        font=("Arial", "10", "bold"),
                                        bg="white",
                                        pady=10)
        self.lbl_convert_result.grid(row=4)

        # Help/History Buttons Frame (Row 5)
        self.frame_help_history = Frame(self.frame_converter)
        self.frame_help_history.grid(row=5)

        # Help Button (HHBF - Row 0)
        self.btn_help = Button(self.frame_help_history,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.btn_help.grid(row=0, column=1)

        # History Button (HHBF - Row 0)
        self.btn_history = Button(self.frame_help_history,
                                  text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.history)
        self.btn_history.grid(row=0, column=2)

    # Get Help Function
    def help(self):
        # Define Format Variables
        get_help = Help(self)
        get_help.txt_help.configure(text="Help Text Goes Here")

    # Get History Function
    def history(self):
        # Define Format Variables
        get_help = Help(self)
        get_help.txt_help.configure(text="Help Text Goes Here")

# Help GUI Class
class Help:
    # Initialize Function
    def __init__(self, partner):
        # Define Format Variables
        bg_colour = "grey"

        # Disable Help Button
        partner.btn_help.configure(state=DISABLED)

        # Create Window
        self.window_help = Toplevel()

        self.window_help.protocol('WM_DELETE_WINDOW', partial(self.dismiss_help, partner))

        # Help Screen GUI
        self.frame_help = Frame(self.window_help, width=300, height=200, bg=bg_colour)
        self.frame_help.grid()

        # Help Heading (Row 0)
        self.lbl_heading_help = Label(self.frame_help,
                                        text="Help/Instructions",
                                        font=("Arial", "16", "bold"),
                                        bg=bg_colour,
                                        padx=10, pady=10)
        self.lbl_heading_help.grid(row=0)

        # Help Text (Label, Row 1)
        self.txt_help = Label(self.frame_help,
                               text="",
                               justify=LEFT,
                               width=40,
                               bg=bg_colour,
                               wrap=250)
        self.txt_help.grid(row=1)
        # Help Button (Row 1)
        self.btn_dismiss = Button(self.frame_help,
                                     text="Dismiss",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     width=10,
                                     command=partial(self.dismiss_help, partner))
        self.btn_dismiss.grid(row=2, pady=10)

    # Dismiss Help Function
    def dismiss_help(self, partner):
        # Re-enable Help Button
        partner.btn_help.configure(state=NORMAL)
        # Close Window
        self.window_help.destroy()


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
