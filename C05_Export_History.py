"""
Temperature Converter
Component 05 - Export History
Version 2.0
Finn Wescombe
6/07/21
"""

from tkinter import *
from functools import partial  # To Prevent Unwanted Windows
import re

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
        self.recent_history = ""
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
                self.recent_history += entry + "\n\n"
        else:
            for i in range(0, 5):
                # Calculation History format [[input, result], [input, result]].
                # For most recent, use [-1]
                entry = self.calculation_history[
                    len(self.calculation_history) - i - 1][0] + " is " + \
                        self.calculation_history[
                            len(self.calculation_history) - i - 1][1]
                self.recent_history += entry + "\n\n"

        # Create class and configure history.
        get_history = History(self)
        get_history.txt_history.configure(text=self.recent_history)

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
        self.frame_history = Frame(self.window_history, width=300, height=200, padx=60,
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
                                 width=50, height=11,
                                 bg=bg_colour)
        self.txt_history.grid(row=2)

        # Button Frame
        self.frame_btns = Frame(self.window_history, width=300, height=200, padx=60,
                                   bg=bg_colour)
        self.frame_btns.grid()

        # Export Button (Row 3)
        self.btn_export = Button(self.frame_btns,
                                  text="Export",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  width=10,
                                  command=partial(self.export, partner))
        self.btn_export.grid(row=3, column=0, pady=10)

        # Dismiss Button (Row 3)
        self.btn_dismiss = Button(self.frame_btns,
                                  text="Dismiss",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  width=10,
                                  command=partial(self.dismiss_history,
                                                  partner))
        self.btn_dismiss.grid(row=3, column=1, pady=10)

    # Get Export Function
    def export(self, main):
        # Define Format Variables
        get_export = Export(self, main.calculation_history)

    # Dismiss History Function
    def dismiss_history(self, partner):
        # Re-enable Help Button
        partner.btn_history.configure(state=NORMAL)
        # Close Window
        self.window_history.destroy()


# Help GUI Class
class Export:
    # Initialize Function
    def __init__(self, partner, calculation_history):
        # Define Format Variables
        bg_colour = "grey"

        # Disable Export Button
        partner.btn_export.configure(state=DISABLED)

        # Create Window
        self.window_export = Toplevel()

        self.window_export.protocol('WM_DELETE_WINDOW',
                                     partial(self.dismiss_export, partner))

        # History Screen GUI
        self.frame_export = Frame(self.window_export, width=300, height=200, padx=50,
                                   bg=bg_colour)
        self.frame_export.grid()

        # History Heading (Row 0)
        self.lbl_heading_history = Label(self.frame_export,
                                         text="Export History",
                                         font=("Arial", "16", "bold"),
                                         bg=bg_colour,
                                         padx=10, pady=5)
        self.lbl_heading_history.grid(row=0)

        # Instruction Label (Row 1)
        self.lbl_instructions = Label(self.frame_export,
                                      text="Enter the name of the .txt file then press"
                                           "Save to export it. If the file name is the"
                                           "same as a file already in this location, that"
                                           "file will be replaced.",
                                      font=("Arial", "10", "italic"),
                                      wrap=250,
                                      justify=CENTER,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_instructions.grid(row=1)

        # Warning Label (Row 2)
        self.lbl_warning = Label(self.frame_export,
                                      text="",
                                      font=("Arial", "10", "italic"),
                                      wrap=250,
                                      justify=CENTER,
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.lbl_warning.grid(row=2)

        # Name Entry (Row 3)
        self.entry_name = Entry(self.frame_export,
                                      width=30,
                                      font=("Arial", "14", "bold"),
                                      justify=CENTER)
        self.entry_name.grid(row=3)

        # Button Frame
        self.frame_btns = Frame(self.window_export, width=300, height=200, padx=60,
                                   bg=bg_colour)
        self.frame_btns.grid()

        # Save Button (Row 0 - Button Frame)
        self.btn_save = Button(self.frame_btns,
                                  text="Save",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  width=10,
                                  command=partial(self.save_history,
                                                  calculation_history))
        self.btn_save.grid(row=0, column=0, pady=10)

        # Dismiss Button (Row 3 - Button Frame)
        self.btn_dismiss = Button(self.frame_btns,
                                  text="Dismiss",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  width=10,
                                  command=partial(self.dismiss_export,
                                                  partner))
        self.btn_dismiss.grid(row=0, column=1, pady=10)

    # Save History Function
    def save_history(self, calculation_history):

        # Export File
        filename = self.entry_name.get()
        valid_char = "[A-Za-z0-9_]"

        error = False

        # Check validity
        for letter in filename:
            if not re.match(valid_char, letter):
                self.lbl_warning.configure(text="{}'s are not allowed".format(letter), bg="red")
                error = True
                break
            elif letter == " ":
                self.lbl_warning.configure(text="Spaces are not allowed", bg="red")
                error = True
                break

        if not filename:
            self.lbl_warning.configure(text="Enter a file name", bg="red")
            error = True

        if not error:
            # Add suffix
            filename = filename + ".txt"

            # Open / Create file
            file = open(filename, "w+")

            # Write to File
            for i in calculation_history:
                file.write(i[0] + " is " + i[1] + "\n")

            # Close file
            file.close()

            # Give message
            self.lbl_warning.configure(text="File {} Saved".format(filename), bg="green")

    # Dismiss Export Function
    def dismiss_export(self, partner):
        # Re-enable Help Button
        partner.btn_export.configure(state=NORMAL)
        # Close Window
        self.window_export.destroy()


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
