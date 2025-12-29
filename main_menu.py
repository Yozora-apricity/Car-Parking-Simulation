import tkinter as tk
from tkinter import messagebox
import os
import sys
import subprocess

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("500x500")
        self.root.configure(bg="black")
        
        self.center_window(500, 500)
        
        title_label = tk.Label(
            self.root,
            text="Main Menu",
            font=("Arial", 23, "bold"),
            fg="white",
            bg="black"
        )
        title_label.pack(pady=(50, 10))

        subtitle_label = tk.Label(
            self.root, 
            text="Select a program to launch:", 
            font=("Arial", 12), 
            bg="black", 
            fg="white"
        )
        subtitle_label.pack(pady=(0, 40))