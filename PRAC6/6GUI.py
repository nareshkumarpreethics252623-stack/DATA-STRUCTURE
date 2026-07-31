import tkinter as tk
from tkinter import simpledialog, messagebox

#Priority Queue
class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item, priority):
        if len(self.queue) >= self.size:
            return "Priority Queue Overflow!"

        self.queue.append((priority, item))
        return f"Enqueued: {item} (Priority {priority})"

    def dequeue(self):
        if not self.queue:
            return "Priority Queue Underflow!"

        highest = min(self.queue, key=lambda x: x[0])
        self.queue.remove(highest)
        return f"Dequeued: {highest[1]} (Priority {highest[0]})"

    def traverse(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Priority Queue\n\n"

        for priority, item in self.queue:
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def ascending(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Ascending Order\n\n"

        for priority, item in sorted(self.queue):
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def descending(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Descending Order\n\n"

        for priority, item in sorted(self.queue, reverse=True):
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


#GUI

pq = PriorityQueue(5)

root = tk.Tk()
root.title("Priority Queue Simulator")
root.geometry("850x620")
root.configure(bg="#D5F5E3")


#Title

title = tk.Label(
    root,
    text="Priority Queue Simulator",
    font=("Segoe UI", 20, "bold"),
    bg="#D5F5E3",
    fg="#154360"
)

title.pack(pady=15)


#Output Box

output = tk.Text(
    root,
    width=85,
    height=18,
    font=("Consolas", 11),
    bg="white",
    fg="#2C3E50"
)

output.pack(pady=15)


def show(msg):
    output.insert(tk.END, msg + "\n\n")
    output.see(tk.END)


#Functions

def enqueue():
    item = simpledialog.askstring("Enqueue", "Enter Item")

    if item is None:
        return

    priority = simpledialog.askinteger("Enqueue", "Enter Priority")

    if priority is None:
        return

    show(pq.enqueue(item, priority))


def dequeue():
    show(pq.dequeue())


def traverse():
    show(pq.traverse())


def ascending():
    show(pq.ascending())


def descending():
    show(pq.descending())


def check_empty():
    if pq.is_empty():
        messagebox.showinfo("Status", "Priority Queue is Empty.")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Empty.")


def check_full():
    if pq.is_full():
        messagebox.showinfo("Status", "Priority Queue is Full.")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Full.")


def clear_output():
    output.delete(1.0, tk.END)


#Buttons

frame = tk.Frame(root, bg="#D5F5E3")
frame.pack(pady=10)


# Row 1

tk.Button(
    frame,
    text="Enqueue",
    width=18,
    bg="#2ECC71",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=enqueue
).grid(row=0, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Dequeue",
    width=18,
    bg="#E74C3C",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=dequeue
).grid(row=0, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Traverse",
    width=18,
    bg="#3498DB",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=traverse
).grid(row=0, column=2, padx=8, pady=8)


# Row 2

tk.Button(
    frame,
    text="Check Empty",
    width=18,
    bg="#F39C12",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=check_empty
).grid(row=1, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Check Full",
    width=18,
    bg="#9B59B6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=check_full
).grid(row=1, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Ascending",
    width=18,
    bg="#1ABC9C",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=ascending
).grid(row=1, column=2, padx=8, pady=8)


# Row 3

tk.Button(
    frame,
    text="Descending",
    width=18,
    bg="#D35400",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=descending
).grid(row=2, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Clear Output",
    width=18,
    bg="#5D6D7E",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=clear_output
).grid(row=2, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Exit",
    width=18,
    bg="#C0392B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=root.destroy
).grid(row=2, column=2, padx=8, pady=8)

root.mainloop()

#Priority Queue
class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item, priority):
        if len(self.queue) >= self.size:
            return "Priority Queue Overflow!"

        self.queue.append((priority, item))
        return f"Enqueued: {item} (Priority {priority})"

    def dequeue(self):
        if not self.queue:
            return "Priority Queue Underflow!"

        highest = min(self.queue, key=lambda x: x[0])
        self.queue.remove(highest)
        return f"Dequeued: {highest[1]} (Priority {highest[0]})"

    def traverse(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Priority Queue\n\n"

        for priority, item in self.queue:
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def ascending(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Ascending Order\n\n"

        for priority, item in sorted(self.queue):
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def descending(self):
        if not self.queue:
            return "Priority Queue is Empty."

        text = "Descending Order\n\n"

        for priority, item in sorted(self.queue, reverse=True):
            text += f"Item : {item}\tPriority : {priority}\n"

        return text

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


#GUI

pq = PriorityQueue(5)

root = tk.Tk()
root.title("Priority Queue Simulator")
root.geometry("850x620")
root.configure(bg="#D5F5E3")


#Title

title = tk.Label(
    root,
    text="Priority Queue Simulator",
    font=("Segoe UI", 20, "bold"),
    bg="#D5F5E3",
    fg="#154360"
)

title.pack(pady=15)


#Output Box

output = tk.Text(
    root,
    width=85,
    height=18,
    font=("Consolas", 11),
    bg="white",
    fg="#2C3E50"
)

output.pack(pady=15)


def show(msg):
    output.insert(tk.END, msg + "\n\n")
    output.see(tk.END)


# Functions

def enqueue():
    item = simpledialog.askstring("Enqueue", "Enter Item")

    if item is None:
        return

    priority = simpledialog.askinteger("Enqueue", "Enter Priority")

    if priority is None:
        return

    show(pq.enqueue(item, priority))


def dequeue():
    show(pq.dequeue())


def traverse():
    show(pq.traverse())


def ascending():
    show(pq.ascending())


def descending():
    show(pq.descending())


def check_empty():
    if pq.is_empty():
        messagebox.showinfo("Status", "Priority Queue is Empty.")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Empty.")


def check_full():
    if pq.is_full():
        messagebox.showinfo("Status", "Priority Queue is Full.")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Full.")


def clear_output():
    output.delete(1.0, tk.END)


#Buttons

frame = tk.Frame(root, bg="#D5F5E3")
frame.pack(pady=10)

# Row 1

tk.Button(
    frame,
    text="Enqueue",
    width=18,
    bg="#2ECC71",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=enqueue
).grid(row=0, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Dequeue",
    width=18,
    bg="#E74C3C",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=dequeue
).grid(row=0, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Traverse",
    width=18,
    bg="#3498DB",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=traverse
).grid(row=0, column=2, padx=8, pady=8)


# Row 2

tk.Button(
    frame,
    text="Check Empty",
    width=18,
    bg="#F39C12",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=check_empty
).grid(row=1, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Check Full",
    width=18,
    bg="#9B59B6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=check_full
).grid(row=1, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Ascending",
    width=18,
    bg="#1ABC9C",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=ascending
).grid(row=1, column=2, padx=8, pady=8)


# Row 3

tk.Button(
    frame,
    text="Descending",
    width=18,
    bg="#D35400",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=descending
).grid(row=2, column=0, padx=8, pady=8)


tk.Button(
    frame,
    text="Clear Output",
    width=18,
    bg="#5D6D7E",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=clear_output
).grid(row=2, column=1, padx=8, pady=8)


tk.Button(
    frame,
    text="Exit",
    width=18,
    bg="#C0392B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=root.destroy
).grid(row=2, column=2, padx=8, pady=8)


root.mainloop()
