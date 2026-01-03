import tkinter as tk
from tkinter import ttk
import random

# ---------------- BST LOGIC ---------------- #
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:  # allow duplicates on right
            node.right = self._insert(node.right, value)
        return node

    # LTR – Inorder
    def ltr(self, node, result):
        if node:
            self.ltr(node.left, result)
            result.append(node.value)
            self.ltr(node.right, result)

    # TLR – Preorder
    def tlr(self, node, result):
        if node:
            result.append(node.value)
            self.tlr(node.left, result)
            self.tlr(node.right, result)

    # LRT – Postorder
    def lrt(self, node, result):
        if node:
            self.lrt(node.left, result)
            self.lrt(node.right, result)
            result.append(node.value)
            
# ---------------- UI ---------------- #
class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("BST Visualizer – LTR / TLR / LRT")
        self.root.geometry("1000x650")

        self.bst = BST()

        # Controls
        control = tk.Frame(root)
        control.pack(pady=10)
        
         # Controls
        control = tk.Frame(root)
        control.pack(pady=10)

        self.entry = ttk.Entry(control, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Insert", command=self.insert_value).pack(side=tk.LEFT, padx=5)
        ttk.Button(control, text="LTR (Inorder)", command=self.show_ltr).pack(side=tk.LEFT, padx=5)
        ttk.Button(control, text="TLR (Preorder)", command=self.show_tlr).pack(side=tk.LEFT, padx=5)
        ttk.Button(control, text="LRT (Postorder)", command=self.show_lrt).pack(side=tk.LEFT, padx=5)

        # Canvas
        self.canvas = tk.Canvas(root, bg="white", height=450)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Traversal output
        self.output = tk.Label(root, text="Traversal: ", font=("Arial", 12))
        self.output.pack(pady=10)

    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.bst.insert(value)
            self.entry.delete(0, tk.END)
            self.redraw()
        except ValueError:
            pass

    def redraw(self):
        self.canvas.delete("all")
        self.draw_tree(self.bst.root, 500, 40, 220)

    def draw_tree(self, node, x, y, offset):
        if not node:
            return

        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#3b82f6")
        self.canvas.create_text(x, y, text=str(node.value), fill="white", font=("Arial", 12, "bold"))

        if node.left:
            self.canvas.create_line(x, y + r, x - offset, y + 80 - r)
            self.draw_tree(node.left, x - offset, y + 80, offset // 2)

        if node.right:
            self.canvas.create_line(x, y + r, x + offset, y + 80 - r)
            self.draw_tree(node.right, x + offset, y + 80, offset // 2)

    def show_ltr(self):
        result = []
        self.bst.ltr(self.bst.root, result)
        self.output.config(text="LTR (Inorder): " + str(result))

    def show_tlr(self):
        result = []
        self.bst.tlr(self.bst.root, result)
        self.output.config(text="TLR (Preorder): " + str(result))

    def show_lrt(self):
        result = []
        self.bst.lrt(self.bst.root, result)
        self.output.config(text="LRT (Postorder): " + str(result))

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    root.mainloop()