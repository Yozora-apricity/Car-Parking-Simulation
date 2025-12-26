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

if __name__ == "__main__":
    tree = BinaryTreeOrder()

    # Example level-order values
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    tree.tree_level_order(values)

    print("In-order (LTR):", ltr(tree.root))
    print("Pre-order (TLR):", tlr(tree.root))
    print("Post-order (LRT):", lrt(tree.root))