import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def myquit(self):
        self.master.destroy()

    def create_widgets(self):
        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.title = tk.Label(text = "Enter the Address into the box below", fg = "black", font = "none 12 bold")
        self.title.pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.numberheading = tk.Label(text = "Number")
        self.numberheading.pack()

        self.Number = tk.Entry(width = 100)
        self.Number.pack()

        self.streetheading = tk.Label(text = "Street")
        self.streetheading.pack()

        self.Street = tk.Entry(width = 100)
        self.Street.pack()

        #self.cityheading = tk.Label(text = "City")
        #self.cityheading.pack()

        #self.City = tk.Entry(width = 100)
        #self.City.pack()
        self.button = tk.Button(text = "Submit", width = 30, command = self.retrieve_input).pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ")
        self.emptyspace.pack()

    def retrieve_input(self):
        self.save_Street = self.Street.get()
        self.save_Number = self.Number.get()
        self.validate_input()
        self.master.destroy()

    def validate_input(self):
        if self.save_Street == "" or self.save_Number == "":
            self.all_input_selected = False
            print("Please input an address")
        else:
            self.all_input_selected = True
