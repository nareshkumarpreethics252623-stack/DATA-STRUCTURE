import tkinter as tk
from tkinter import messagebox, simpledialog

class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedListGUI:
    def __init__(self, root):
        self.head = None
        self.root = root
        root.title("Singly Linked List Operations")
        root.geometry("500x420")
        root.configure(bg="#f4f4f9")

        tk.Label(root, text="Singly Linked List Operations", font=("Arial", 14, "bold"), bg="#f4f4f9").pack(pady=10)
        self.lbl = tk.Label(root, text="Linked List is empty.", font=("Courier New", 12, "bold"), bg="white", fg="#d9534f", width=45, height=3, relief="groove")
        self.lbl.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#f4f4f9")
        btn_frame.pack()

        # Menu configurations mapped as: (Button Text, Hex Color, Execution Method)
        menu = [
            ("1. Insert at Beginning", "#0275d8", lambda: self.run(self.ins_beg)),
            ("2. Insert at End", "#0275d8", lambda: self.run(self.ins_end)),
            ("3. Insert at Position", "#0275d8", lambda: self.run(self.ins_pos)),
            ("4. Delete Node by Value", "#f0ad4e", lambda: self.run(self.del_val)),
            ("5. Delete Node by Index", "#f0ad4e", lambda: self.run(self.del_idx)),
            ("6. Refresh List", "#5cb85c", self.update)
        ]
        
        for i, (txt, col, cmd) in enumerate(menu):
            tk.Button(btn_frame, text=txt, bg=col, fg="white", font=("Arial", 10, "bold"), width=22, pady=5, bd=0, cursor="hand2", command=cmd).grid(row=i//2, column=i%2, padx=5, pady=5)

        tk.Button(root, text="7. Exit Program", bg="#d9534f", fg="white", font=("Arial", 10, "bold"), width=15, pady=5, bd=0, command=root.quit).pack(pady=15)

    def update(self):
        res, temp = [], self.head
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        self.lbl.config(text=" -> ".join(res) + " -> None" if res else "Linked List is empty.", fg="#5cb85c" if res else "#d9534f")

    def run(self, action):
        try:
            action()
            self.update()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ins_beg(self):
        val = simpledialog.askinteger("Input", "Enter data:")
        if val is not None:
            n = Node(val)
            n.next, self.head = self.head, n

    def ins_end(self):
        val = simpledialog.askinteger("Input", "Enter data:")
        if val is not None:
            if not self.head: self.head = Node(val)
            else:
                t = self.head
                while t.next: t = t.next
                t.next = Node(val)

    def ins_pos(self):
        val = simpledialog.askinteger("Input", "Enter data:")
        pos = simpledialog.askinteger("Input", "Enter position (0-indexed):") if val is not None else None
        if pos is not None:
            if pos == 0:
                self.ins_beg()
                return
            t = self.head
            for _ in range(pos - 1):
                if not t: raise IndexError("Position out of bounds.")
                t = t.next
            if not t: raise IndexError("Position out of bounds.")
            n = Node(val)
            n.next, t.next = t.next, n

    def del_val(self):
        val = simpledialog.askinteger("Input", "Enter value to delete:")
        if val is not None:
            t, p = self.head, None
            while t and t.data != val:
                p, t = t, t.next
            if not t: messagebox.showwarning("Not Found", "Value not found.")
            elif p: p.next = t.next
            else: self.head = t.next

    def del_idx(self):
        pos = simpledialog.askinteger("Input", "Enter index to delete:")
        if pos is not None:
            if not self.head: raise IndexError("List is empty.")
            if pos == 0:
                self.head = self.head.next
                return
            t, p = self.head, None
            for _ in range(pos):
                if not t: raise IndexError("Position out of bounds.")
                p, t = t, t.next
            if not t: raise IndexError("Position out of bounds.")
            p.next = t.next

if __name__ == "__main__":
    root = tk.Tk()
    LinkedListGUI(root)
    root.mainloop()

