"""
Temperature Converter
Component 01 - Help GUI
Version 1.0
Finn Wescombe
21/06/21
"""

from tkinter import *

# Main Converter GUI Class
class Converter:
    # Initialize Function
    def __init__(self):

        # Define Format Variables
        bg_colour = "grey"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=bg_colour)
        self.converter_frame.grid()

        # Temperature Converter Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=bg_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame,
                                  text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        

