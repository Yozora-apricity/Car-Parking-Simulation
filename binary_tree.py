import tkinter as tk
from tkinter import ttk
import random
import string

# --- BINARY TREE LOGIC ---
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ltr(node): # In-order
    if node is None:
        return []
    else:
        left_node = ltr(node.left)
        current_node = [node.value] if node.value != " " else []
        right_node = ltr(node.right)
        return left_node + current_node + right_node

def tlr(node): # Pre-order
    if node is None:
        return []
    else:
        current_node = [node.value] if node.value != " " else []
        left_node = tlr(node.left)
        right_node = tlr(node.right)
        return current_node + left_node + right_node

def lrt(node): # Post-Order
    if node is None:
        return []
    else:
        left_node = lrt(node.left)
        right_node = lrt(node.right)
        current_node = [node.value] if node.value != " " else []
        return left_node + right_node + current_node

class BinaryTreeOrder:
    def __init__(self):
        self.root = None
        self.nodes_list = []

    def tree_level_value(self, char_val):
        self.nodes_list.append(char_val)
        self._level_order_insertion(self.nodes_list)

    def tree_level_order(self, values):
        if not values:
            self.root = None
            return
        nodes = [BinaryTreeNode(v) for v in values]
        for i in range(len(nodes)):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
        self.root = nodes[0]

# --- BINARY TREE  UI ---
class BinaryTreeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Tree")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f8fafc")

        self.main_frame = tk.Frame(self.root, bg="#f8fafc")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.root.bind("<Escape>", lambda e: self.root.quit())

        self.main_menu_screen()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def main_menu_screen(self):
        self.clear_screen()

        tk.Label(
            self.main_frame,
            text="BINARY TREE",
            font=("Arial", 40, "bold"),
            bg="#f8fafc",
            fg="#1e293b"
        ).pack(pady=200)

        tk.Label(
            self.main_frame,
            text="Press ENTER to Start",
            font=("Arial", 14),
            bg="#f8fafc",
            fg="#64748b"
        ).pack()

        self.root.bind("<Return>", lambda e: print("Start pressed"))

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryTreeUI(root)
    root.mainloop()