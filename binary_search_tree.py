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
        