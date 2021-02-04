import tkinter as tk
from tkinter import *

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.title = tk.Label(text = "Enter the Address into the box below", bg = "white", fg = "black", font = "none 12 bold")
        self.title.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.address = tk.Entry(width = 100)
        self.address.pack()
        self.button = tk.Button(text = "Submit", width = 30, command = self.retrieve_input).pack()

    def say_hi(self):
        print("hi there, everyone!")

    def retrieve_input(self):
        self.save_address = self.address.get()
        self.validate_input()

    def validate_input(self):
        if self.save_address == "":
            self.all_input_selected = False
            print("Please input an address")
        else:
            self.all_input_selected = True


'''class PDFReaderGui:
    def __intit__(self):
        self.window = tk.Tk()
        self.window.title("PDF Reader")
        self.window.configure(background = "lightgrey")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.save_address = ""

        self.create_widgets()

    def retrieve_input(self):
        self.save_address = self.address.get()
        self.validate_input()

    def validate_input(self):
        if self.save_address == "":
            self.all_input_selected = False
            print("Please input an address")
        else:
            self.all_input_selected = True

    def create_widgets(self):
        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.title = tk.Label(text = "Enter the Address into the box below", bg = "white", fg = "black", font = "none 12 bold")
        self.title.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.emptyspace = tk.Label(text = " ", bg = "lightgrey")
        self.emptyspace.pack()

        self.address = tk.Entry(width = 100)
        self.address.pack()
        self.button = tk.Button(text = "Submit", width = 30, command = self.retrieve_input).pack()
        '''
