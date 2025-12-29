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
        
        # Buttons Configuration
        btn_style = {
            "font": ("Arial", 12, "bold"),
            "bg": "#333333",  # Dark gray button
            "fg": "white",    # White text
            "activebackground": "#555555",
            "activeforeground": "white",
            "width": 25,
            "height": 2,
            "bd": 0
        }

        # --- Button Definitions ---
        # 1. Car Parking Simulation (CLI - Needs Terminal for now)
        self.btn_parking = tk.Button(
            self.root, 
            text="Car Parking Simulation", 
            command=self.launch_parking_sim,
            **btn_style
        )
        self.btn_parking.pack(pady=10)

        # 2. Tower of Hanoi (Pygame)
        self.btn_hanoi = tk.Button(
            self.root, 
            text="Tower of Hanoi (Pygame)", 
            command=lambda: self.launch_script("recursion.py"),
            **btn_style
        )
        self.btn_hanoi.pack(pady=10)

        # 3. Binary Tree Visualizer (Tkinter)
        self.btn_btree = tk.Button(
            self.root, 
            text="Binary Tree Visualizer", 
            command=lambda: self.launch_script("binary_tree.py"),
            **btn_style
        )
        self.btn_btree.pack(pady=10)

        # 4. BST Visualizer (Tkinter)
        self.btn_bst = tk.Button(
            self.root, 
            text="BST Visualizer", 
            command=lambda: self.launch_script("binary_search_tree.py"),
            **btn_style
        )
        self.btn_bst.pack(pady=10)

        # Exit Button
        self.btn_exit = tk.Button(
            self.root, 
            text="EXIT", 
            command=self.root.quit,
            font=("Arial", 12, "bold"),
            bg="#800000", # Dark red
            fg="white",
            width=25,
            height=2,
            bd=0
        )
        self.btn_exit.pack(pady=30)

        # Footer
        footer = tk.Label(
            self.root,
            text="System Ready...",
            font=("Consolas", 10),
            bg="black",
            fg="gray"
        )
        footer.pack(side=tk.BOTTOM, pady=10)