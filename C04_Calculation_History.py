"""
Temperature Converter
Component 04 - Calculation History
Version 2.0
Finn Wescombe
1/07/21
"""

from tkinter import *
from functools import partial  # To Prevent Unwanted Windows


# Main Converter GUI Class
class Converter:

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
                                        font=("Arial", "14", "bold"),
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

        # Disable if no history
        if len(self.calculation_history) == 0:
            self.btn_history.configure(state=DISABLED)

    # Get Help Function
    def help(self):
        # Define Format Variables
        get_help = Help(self)
        get_help.txt_help.configure(text="Help Text Goes Here")

    # Get History Function
    def history(self):

        # Text for Recent History
        recent_history = ""
        # Reverse the list for most recent.
        # self.calculation_history.reverse()

        # Add to a string the five most recent entries.
        if len(self.calculation_history) < 5:
            for i in range(0, len(self.calculation_history)):
                # Calculation History format [[input, result], [input, result]].
                # For most recent, use [-1]
                entry = self.calculation_history[
                    len(self.calculation_history) - i - 1][0] + " is " + \
                        self.calculation_history[
                            len(self.calculation_history) - i - 1][1]
                recent_history += entry + "\n\n"
        else:
            for i in range(0, 5):
                # Calculation History format [[input, result], [input, result]].
                # For most recent, use [-1]
                entry = self.calculation_history[
                    len(self.calculation_history) - i - 1][0] + " is " + \
                        self.calculation_history[
                            len(self.calculation_history) - i - 1][1]
                recent_history += entry + "\n\n"

        # Create class and configure history.
        get_history = History(self)
        get_history.txt_history.configure(text=recent_history)

    # Convert Function
    def convert(self, centigrade):

        # Conversion Constant
        CONVERSION = 9 / 5

        # Get Input and Determine Validity
        # Set input to string so that float '0.0' can be considered valid.
        input = ""
        result = 0
        try:
            input = float(self.entry_to_convert.get())
        except ValueError:
            # Configure Result Label Text to Display Error Message
            self.lbl_convert_result.configure(
                text="This Input is Invalid. Please Enter a Number.", bg="red")

        if input or input == 0:
            # Determine Conversion Type
            if centigrade:

                # Ensure input is not less than absolute zero
                if input >= -273.13:

                    # Conversion to Fahrenheit from Centigrade
                    result = input * CONVERSION + 32

                    # Configure Result Label Text to Display Result Rounded to 1 Decimal Point with appropriate unit and green background.
                    self.lbl_convert_result.configure(
                        text="{:.1f} Degrees Fahrenheit".format(result),
                        bg="green")

                    # Save for Calculation History
                    self.calculation_history.append(
                        ["{:.1f} Degrees Centigrade".format(input),
                         "{:.1f} Degrees Fahrenheit".format(result)])
                    self.btn_history.configure(state=NORMAL)

                else:
                    self.lbl_convert_result.configure(
                        text="This Temperature is Less than Absolute Zero (-273.13 Centigrade).",
                        bg="red")



            else:
                if input >= -459.76:
                    # Conversion to Centigrade from Fahrenheit
                    result = (input - 32) * (1 / CONVERSION)

                    # Configure Result Label Text to Display Result Rounded to 1 Decimal Point with appropriate unit.
                    self.lbl_convert_result.configure(
                        text="{:.1f} Degrees Centigrade".format(result),
                        bg="green")

                    # Save for Calculation History and enable button
                    self.calculation_history.append(
                        ["{:.1f} Degrees Fahrenheit".format(input),
                         "{:.1f} Degrees Centigrade".format(result)])
                    self.btn_history.configure(state=NORMAL)

                else:
                    self.lbl_convert_result.configure(
                        text="This Temperature is Less than Absolute Zero (-459.76 Fahrenheit).",
                        bg="red")


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

        self.window_help.protocol('WM_DELETE_WINDOW',
                                  partial(self.dismiss_help, partner))

        # Help Screen GUI
        self.frame_help = Frame(self.window_help, width=300, height=200,
                                bg=bg_colour)
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

        self.window_history.protocol('WM_DELETE_WINDOW',
                                     partial(self.dismiss_history, partner))

        # History Screen GUI
        self.frame_history = Frame(self.window_history, width=300, height=200,
                                   bg=bg_colour)
        self.frame_history.grid()

        # History Heading (Row 0)
        self.lbl_heading_history = Label(self.frame_history,
                                         text="Calculation History",
                                         font=("Arial", "16", "bold"),
                                         bg=bg_colour,
                                         padx=10, pady=5)
        self.lbl_heading_history.grid(row=0)

        # Instruction Label (Row 1)
        self.lbl_instructions = Label(self.frame_history,
                                      text="Here are your five most recent "
                                           "calculations. You can export the "
                                           "entire history to a .txt file using "
                                           "the export button.",
                                      font=("Arial", "10", "italic"),
                                      wrap=250,
                                      justify=CENTER,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_instructions.grid(row=1)

        # Recent History (Row 2)
        self.txt_history = Label(self.frame_history,
                                 text="",
                                 font=("Arial", "10", "bold"),
                                 justify=CENTER,
                                 width=50,
                                 bg=bg_colour)
        self.txt_history.grid(row=2)

        # Dismiss Button (Row 3)
        self.btn_dismiss = Button(self.frame_history,
                                  text="Dismiss",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  width=10,
                                  command=partial(self.dismiss_history,
                                                  partner))
        self.btn_dismiss.grid(row=3, pady=10)

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
