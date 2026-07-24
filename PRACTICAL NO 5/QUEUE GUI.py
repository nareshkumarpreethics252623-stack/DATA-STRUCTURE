import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import deque

class Queue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def enqueue(self, item):
        if len(self.queue) == self.size:
            return "Queue Overflow! Queue is full."
        self.queue.append(item)
        return f"{item} inserted into the queue."

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue Underflow! Queue is empty."
        item = self.queue.popleft()
        return f"{item} deleted from the queue."

    def traverse(self):
        if len(self.queue) == 0:
            return "Queue is empty."
        return "Queue: " + " -> ".join(map(str, self.queue))

    def front(self):
        if len(self.queue) == 0:
            return "Queue is empty."
        return f"Front element: {self.queue[0]}"

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


# Create Queue
size = simpledialog.askinteger("Queue Size", "Enter maximum queue size:")
q = Queue(size)

# GUI Window
root = tk.Tk()
root.title("Queue Operations")
root.geometry("450x450")
root.config(bg="lightblue")

result = tk.StringVar()
result.set("Queue is empty.")

# Functions
def enqueue():
    item = simpledialog.askstring("Enqueue", "Enter element:")
    if item:
        result.set(q.enqueue(item))

def dequeue():
    result.set(q.dequeue())

def traverse():
    result.set(q.traverse())

def front():
    result.set(q.front())

def check_empty():
    if q.is_empty():
        result.set("Queue is empty.")
    else:
        result.set("Queue is not empty.")

def check_full():
    if q.is_full():
        result.set("Queue is full.")
    else:
        result.set("Queue is not full.")

# Heading
tk.Label(root, text="QUEUE OPERATIONS",
         font=("Arial", 18, "bold"),
         bg="lightblue").pack(pady=10)

# Buttons
tk.Button(root, text="Enqueue", width=20, command=enqueue).pack(pady=5)
tk.Button(root, text="Dequeue", width=20, command=dequeue).pack(pady=5)
tk.Button(root, text="Traverse", width=20, command=traverse).pack(pady=5)
tk.Button(root, text="View Front", width=20, command=front).pack(pady=5)
tk.Button(root, text="Check Empty", width=20, command=check_empty).pack(pady=5)
tk.Button(root, text="Check Full", width=20, command=check_full).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=10)

# Result Display
tk.Label(root, text="Output:",
         font=("Arial", 12, "bold"),
         bg="lightblue").pack()

tk.Label(root,
         textvariable=result,
         font=("Arial", 12),
         bg="white",
         width=40,
         height=5,
         relief="sunken",
         wraplength=350).pack(pady=10)

root.mainloop()
