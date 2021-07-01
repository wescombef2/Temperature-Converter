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

    # Calculation History Variable
    calculation_history = []

    # Initialize Function
    def __init__(self):
        # Define Format Variables
        bg_colour = "grey"

        # Define History List
        self.calculation_history = []

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
                                      justify=CENTER,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_instructions.grid(row=1)

        # Entry Box (Row 2)
        self.entry_to_convert = Entry(self.frame_converter,
                                      width=30,
                                      font=("Arial", "14", "bold"),
                                      justify=CENTER)
        self.entry_to_convert.grid(row=2)

        # Conversion Buttons Frame (Row 3)
        self.frame_convert_btns = Frame(self.frame_converter)
        self.frame_convert_btns.grid(row=3)

        # Centigrade and Fahrenheit Buttons (CBF - Row 0)
        self.btn_centigrade = Button(self.frame_convert_btns,
                                     text="Centigrade",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=partial(self.convert, False))
        self.btn_centigrade.grid(row=0, column=1)

        self.btn_fahrenheit = Button(self.frame_convert_btns,
                                     text="Fahrenheit",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=partial(self.convert, True))
        self.btn_fahrenheit.grid(row=0, column=2)

        # Conversion Result (Row 4)
        self.lbl_convert_result = Label(self.frame_converter,
                                        text="Conversion goes here...",
                                        font=("Arial", "10", "bold"),
                                        bg=bg_colour,
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

        # Text for Recent History
        recent_history = ""
        for i in range(-1,-7):
            # Calculation History has
            recent_history += self.calculation_history[-1][0]

        get_help = History(self)
        get_help.txt_history.configure(text=self.calculation_history)

    # Convert Function
    def convert(self, centigrade):

        # Conversion Constant
        CONVERSION = 9/5

        # Get Input and Determine Validity
        input = 0
        try:
            input = float(self.entry_to_convert.get())
        except ValueError:
            print("Error")

        # Determine Conversion Type
        if input:
            if centigrade:

                # Conversion to Fahrenheit from Centigrade
                result = input * CONVERSION + 32

                # Save for Calculation History
                self.calculation_history.append([str(input) + "C", str(result) + "F"])
            else:

                # Conversion to Centigrade from Fahrenheit
                result = (input - 32) * (1/CONVERSION)

                # Save for Calculation History
                self.calculation_history.append([str(input) + "F", str(result) + "C"])

            # Configure Result Label Text to Display Result Rounded to 1 Decimal Point
            self.lbl_convert_result.configure(text="{:.1f}".format(result))
        else:
            print("Something has gone wrong.")

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

# Help GUI Class
class History:
    # Initialize Function
    def __init__(self, partner):
        # Define Format Variables
        bg_colour = "grey"

        # Disable History Button
        partner.btn_history.configure(state=DISABLED)

        # Create Window
        self.window_history = Toplevel()

        self.window_history.protocol('WM_DELETE_WINDOW', partial(self.dismiss_history, partner))

        # History Screen GUI
        self.frame_history = Frame(self.window_history, width=300, height=200, bg=bg_colour)
        self.frame_history.grid()

        # History Heading (Row 0)
        self.lbl_heading_history = Label(self.frame_history,
                                        text="Calculation History",
                                        font=("Arial", "16", "bold"),
                                        bg=bg_colour,
                                        padx=10, pady=10)
        self.lbl_heading_history.grid(row=0)

        # Help Text (Row 1)
        self.txt_history = Label(self.frame_history,
                               text="",
                               justify=LEFT,
                               width=40,
                               bg=bg_colour,
                               wrap=250)
        self.txt_history.grid(row=1)

        # Dismiss Button (Row 2)
        self.btn_dismiss = Button(self.frame_history,
                                     text="Dismiss",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     width=10,
                                     command=partial(self.dismiss_history, partner))
        self.btn_dismiss.grid(row=2, pady=10)

    # Dismiss History Function
    def dismiss_history(self, partner):
        # Re-enable Help Button
        partner.btn_history.configure(state=NORMAL)
        # Close Window
        self.window_history.destroy()


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
