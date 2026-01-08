import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox

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

        # ---------- MODE SELECTION ----------
        mode_frame = tk.Frame(root)
        mode_frame.pack(pady=5)

        self.mode = tk.StringVar(value="manual")

        ttk.Label(mode_frame, text="Input Mode:").pack(side=tk.LEFT, padx=5)

        ttk.Radiobutton(
            mode_frame, text="Manual",
            variable=self.mode, value="manual",
            command=self.update_mode
        ).pack(side=tk.LEFT)

        ttk.Radiobutton(
            mode_frame, text="Random Tree",
            variable=self.mode, value="random",
            command=self.update_mode
        ).pack(side=tk.LEFT)

        # ---------- CONTROLS ----------
        control = tk.Frame(root)
        control.pack(pady=10)

        self.entry = ttk.Entry(control, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.insert_btn = ttk.Button(control, text="Insert", command=self.insert_value)
        self.insert_btn.pack(side=tk.LEFT, padx=5)

        ttk.Label(control, text="Insert Amount of Nodes:").pack(side=tk.LEFT, padx=5)

        self.rand_count = ttk.Entry(control, width=5)
        self.rand_count.pack(side=tk.LEFT, padx=5)

        self.generate_btn = ttk.Button(
            control, text="Generate Random", command=self.generate_random
        )
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        ttk.Button(control, text="Clear Tree", command=self.clear_tree).pack(
            side=tk.LEFT, padx=5
        )

        ttk.Button(control, text="LTR (Inorder)", command=self.show_ltr).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(control, text="TLR (Preorder)", command=self.show_tlr).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(control, text="LRT (Postorder)", command=self.show_lrt).pack(
            side=tk.LEFT, padx=5
        )

        # ---------- CANVAS ----------
        canvas_frame = tk.Frame(root)
        canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(canvas_frame, bg="white", height=450)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        v_scroll = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        h_scroll = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        h_scroll.pack(fill=tk.X)

        self.canvas.configure(
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set
        )
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # ---------- OUTPUT ----------
        self.output = tk.Label(root, text="Traversal:", font=("Arial", 12))
        self.output.pack(pady=10)

        # Initialize mode
        self.update_mode()

    # ---------- MODE HANDLING ----------
    def update_mode(self):
        if self.mode.get() == "manual":
            self.entry.config(state="normal")
            self.insert_btn.config(state="normal")
            self.rand_count.config(state="disabled")
            self.generate_btn.config(state="disabled")
        else:
            self.entry.config(state="disabled")
            self.insert_btn.config(state="disabled")
            self.rand_count.config(state="normal")
            self.generate_btn.config(state="normal")

    # ---------- TREE ACTIONS ----------
    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.bst.insert(value)
            self.entry.delete(0, tk.END)
            self.redraw()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def generate_random(self):
        try:
            count = int(self.rand_count.get())

            if count < 10 or count > 30:
                messagebox.showerror(
                    "Invalid Node Count",
                    "Please enter a number between 10 and 30.",
                    parent=self.root
                )
                return

            for _ in range(count):
                self.bst.insert(random.randint(0, 200))

            self.redraw()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid integer.",
                parent=self.root
            )


    def clear_tree(self):
        self.bst.root = None
        self.canvas.delete("all")
        self.output.config(text="Traversal:")

    # ---------- DRAWING ----------
    def redraw(self):
        self.canvas.delete("all")
        self.draw_tree(self.bst.root, 500, 40, 220)

    def draw_tree(self, node, x, y, offset):
        if not node:
            return

        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#3b82f6")
        self.canvas.create_text(x, y, text=str(node.value), fill="white")

        if node.left:
            self.canvas.create_line(x, y + r, x - offset, y + 80 - r)
            self.draw_tree(node.left, x - offset, y + 80, offset // 2)

        if node.right:
            self.canvas.create_line(x, y + r, x + offset, y + 80 - r)
            self.draw_tree(node.right, x + offset, y + 80, offset // 2)

    # ---------- TRAVERSALS ----------
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