import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from udt_convert import UDTToJSON


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Variables
        self.files = None
        self.destination = None

        ### GUI
        self.title("PillinTools")
        self.config(padx=20, pady=20)

        # Elements
        self.source_label = ttk.Label(text="Files:")
        self.source_entry = ttk.Entry(width=20)
        self.source_button = ttk.Button(text="...", command=self.get_files)
        self.destination_label = ttk.Label(text="Destination:")
        self.destination_button = ttk.Button(text="...", command=self.get_destination)
        self.destination_entry = ttk.Entry(width=20)
        self.submit_button = ttk.Button(text="Submit", command=self.convert_udt_to_json)

        # Layout
        self.source_label.grid(row=0, column=0, sticky="w")
        self.source_entry.grid(row=0, column=1)
        self.source_button.grid(row=0, column=2)
        self.destination_label.grid(row=1, column=0, sticky="w")
        self.destination_entry.grid(row=1, column=1)
        self.destination_button.grid(row=1, column=2)
        self.submit_button.grid(row=2, column=0, columnspan=3, sticky="ew")

        # Global Properties
        for child in self.winfo_children():
            child.grid_configure(padx=2, pady=2)

    def get_files(self):
        self.files = filedialog.askopenfilenames(title="Select Files",
                                                 initialdir="C:/",
                                                 filetypes=[(".L5X", ".L5X")])
        self.source_entry.delete(0, "end")
        self.source_entry.insert(0, self.files)

    def get_destination(self):
        self.destination = filedialog.askdirectory(title="Select Destination",
                                                   initialdir="C:/")
        self.destination_entry.delete(0, "end")
        self.destination_entry.insert(0, self.destination)

    def convert_udt_to_json(self):
        try:
            for file in self.files:
                udt = UDTToJSON(file, self.destination)
                udt.main_command()
        except Exception as e:
            messagebox.showerror(title="Error", message=e)
        else:
            messagebox.showinfo(title="Execution Done", message="JSON files were created.")
            self.source_entry.delete(0, "end")
            self.destination_entry.delete(0, "end")
