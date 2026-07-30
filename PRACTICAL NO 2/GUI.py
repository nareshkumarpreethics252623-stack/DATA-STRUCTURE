import tkinter as tk
from tkinter import messagebox
import time

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")
        return self.items.pop(position)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is empty"
        return " <- ".join(self.items)

    def display(self):
        if self.is_empty():
            return "Stack is empty"
        return "\n".join(reversed(self.items))


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Interactive Stack Operations")
        self.root.geometry("600x600")
        self.root.configure(bg="#2c3e50")

        title = tk.Label(root,
                         text="Interactive Stack Operations",
                         font=("Arial", 18, "bold"),
                         bg="#2c3e50",
                         fg="white")
        title.pack(pady=10)

        # Item Entry
        tk.Label(root,
                 text="Item:",
                 bg="#2c3e50",
                 fg="white").pack()

        self.item_entry = tk.Entry(root, width=30)
        self.item_entry.pack(pady=5)

        # Position Entry
        tk.Label(root,
                 text="Position:",
                 bg="#2c3e50",
                 fg="white").pack()

        self.position_entry = tk.Entry(root, width=30)
        self.position_entry.pack(pady=5)

        # Buttons
        frame = tk.Frame(root, bg="#2c3e50")
        frame.pack(pady=15)

        tk.Button(frame, text="Insert",
                  width=12,
                  bg="green",
                  fg="white",
                  command=self.insert_item).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(frame, text="Delete",
                  width=12,
                  bg="red",
                  fg="white",
                  command=self.delete_item).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame, text="Peek",
                  width=12,
                  command=self.peek_item).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(frame, text="Is Empty?",
                  width=12,
                  command=self.check_empty).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame, text="Size",
                  width=12,
                  command=self.show_size).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(frame, text="Traverse",
                  width=12,
                  command=self.traverse).grid(row=2, column=1, padx=5, pady=5)

        # Status Label
        self.status = tk.Label(root,
                               text="Welcome!",
                               font=("Arial", 12),
                               bg="#2c3e50",
                               fg="yellow")
        self.status.pack(pady=10)

        # Stack Display
        tk.Label(root,
                 text="Current Stack (Top First)",
                 bg="#2c3e50",
                 fg="white",
                 font=("Arial", 12, "bold")).pack()

        self.stack_display = tk.Text(root,
                                     width=25,
                                     height=15,
                                     font=("Courier", 14))
        self.stack_display.pack()

        self.update_display()

    def animate(self, text):
        self.status.config(text=text)
        self.root.update()
        time.sleep(0.2)

        self.status.config(text=text + ".")
        self.root.update()
        time.sleep(0.2)

        self.status.config(text=text + "..")
        self.root.update()
        time.sleep(0.2)

        self.status.config(text=text + "...")
        self.root.update()
        time.sleep(0.2)

    def update_display(self):
        self.stack_display.delete(1.0, tk.END)
        self.stack_display.insert(tk.END, self.stack.display())

    def insert_item(self):
        item = self.item_entry.get()

        try:
            pos = int(self.position_entry.get())

            self.animate("Inserting")

            self.stack.insert(item, pos)

            self.status.config(text=f"'{item}' inserted at position {pos}",
                               fg="lightgreen")

            self.update_display()

        except ValueError:
            messagebox.showerror("Error", "Position must be an integer.")

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def delete_item(self):
        try:
            pos = int(self.position_entry.get())

            self.animate("Deleting")

            item = self.stack.delete(pos)

            self.status.config(text=f"'{item}' deleted from position {pos}",
                               fg="tomato")

            self.update_display()

        except ValueError:
            messagebox.showerror("Error", "Position must be an integer.")

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_item(self):
        try:
            item = self.stack.peek()
            messagebox.showinfo("Top Item", item)

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def check_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack", "Stack is Empty")
        else:
            messagebox.showinfo("Stack", "Stack is NOT Empty")

    def show_size(self):
        messagebox.showinfo("Size", f"Stack Size: {self.stack.size()}")

    def traverse(self):
        messagebox.showinfo("Traversal", self.stack.traverse())


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
