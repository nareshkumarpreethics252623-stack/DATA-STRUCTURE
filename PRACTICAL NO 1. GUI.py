import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "<-".join(reversed(self.items)) if self.items else "Stack is empty."

class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Interactive Stack Operations")

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        tk.Button(root, text="Push", command=self.push_item, bg="lightgreen").pack(pady=2)
        tk.Button(root, text="Pop", command=self.pop_item, bg="lightcoral").pack(pady=2)
        tk.Button(root, text="Peek", command=self.peek_item, bg="lightblue").pack(pady=2)
        tk.Button(root, text="Is Empty?", command=self.check_empty, bg="khaki").pack(pady=2)
        tk.Button(root, text="Size", command=self.check_size, bg="plum").pack(pady=2)
        tk.Button(root, text="Quit", command=root.quit, bg="gray").pack(pady=2)

        self.stack_label = tk.Label(root, text="Stack is empty.", fg="blue", font=("Arial", 12))
        self.stack_label.pack(pady=10)

    def update_stack_display(self):
        self.stack_label.config(text=str(self.stack))

    def push_item(self):
        item = self.entry.get()
        if item:
            self.stack.push(item)
            messagebox.showinfo("Push", f"'{item}' has been pushed onto the stack.")
            self.entry.delete(0, tk.END)
            self.update_stack_display()
        else:
            messagebox.showwarning("Input Error", "Please enter an item to push.")

    def pop_item(self):
        try:
            item = self.stack.pop()
            messagebox.showinfo("Pop", f"'{item}' has been popped from the stack.")
            self.update_stack_display()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_item(self):
        try:
            item = self.stack.peek()
            messagebox.showinfo("Peek", f"Top item: {item}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def check_empty(self):
        empty = "Yes" if self.stack.is_empty() else "No"
        messagebox.showinfo("Is Empty?", f"Is the stack empty? {empty}")

    def check_size(self):
        size = self.stack.size()
        messagebox.showinfo("Size", f"Size of the stack: {size}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = StackGUI(root)
    root.mainloop()
