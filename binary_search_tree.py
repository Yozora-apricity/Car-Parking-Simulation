import tkinter as tk
from tkinter import ttk

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
        elif value > node.value:
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
