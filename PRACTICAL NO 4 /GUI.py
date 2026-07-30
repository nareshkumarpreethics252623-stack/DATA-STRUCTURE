import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data, self.next, self.prev = data, None, None

class DoublyLinkedList:
    def __init__(self): self.head = None

    def insert_at_beginning(self, data):
        n = Node(data)
        if self.head: n.next, self.head.prev = self.head, n
        self.head = n

    def insert_at_end(self, data):
        if not self.head: return self.insert_at_beginning(data)
        t = self.head
        while t.next: t = t.next
        t.next, n = Node(data), Node(data)
        t.next.prev = t

    def _get_to_pos(self, pos):
        t = self.head
        for _ in range(pos):
            if not t: raise IndexError("Position out of bounds.")
            t = t.next
        if not t: raise IndexError("Position out of bounds.")
        return t

    def insert_at_position(self, data, pos):
        if pos == 0: return self.insert_at_beginning(data)
        t, n = self._get_to_pos(pos), Node(data)
        n.next, n.prev = t, t.prev
        if t.prev: t.prev.next = n
        t.prev = n

    def delete_node_at_beginning(self):
        if self.head: self.head = self.head.next
        if self.head: self.head.prev = None

    def delete_node_at_end(self):
        if not self.head or not self.head.next: self.head = None; return
        t = self.head
        while t.next: t = t.next
        t.prev.next = None

    def delete_node_at_position(self, pos):
        if not self.head: return
        t = self._get_to_pos(pos)
        if t.prev: t.prev.next = t.next
        if t.next: t.next.prev = t.prev
        if t == self.head: self.head = t.next

    def get_elements(self):
        t, el = self.head, []
        while t: el.append(str(t.data)); t = t.next
        return el

    def search_node(self, k):
        t = self.head
        while t:
            if t.data == k: return True
            t = t.next
        return False

    def length_of_list(self):
        t, count = self.head, 0
        while t: count += 1; t = t.next
        return count

class DLLGui:
    def __init__(self, root):
        self.dll, self.root = DoublyLinkedList(), root
        root.title("DLL Operations")
        root.geometry("500x380")
        
        frm = tk.Frame(root)
        frm.pack(pady=10)
        tk.Label(frm, text="Data:").grid(row=0, column=0)
        self.e_data = tk.Entry(frm, width=8)
        self.e_data.grid(row=0, column=1, padx=5)
        tk.Label(frm, text="Pos:").grid(row=0, column=2)
        self.e_pos = tk.Entry(frm, width=8)
        self.e_pos.grid(row=0, column=3, padx=5)

        self.lbl = tk.Label(root, text="List Empty", fg="red", font=("Arial", 12, "bold"), width=40, bd=2, relief="sunken")
        self.lbl.pack(pady=10)

        bf = tk.Frame(root)
        bf.pack()
        
        opts = [
            ("Ins Beg", lambda: self.op(1), "#0275d8", 0, 0), ("Ins End", lambda: self.op(2), "#0275d8", 0, 1), ("Ins Pos", lambda: self.op(3), "#0275d8", 0, 2),
            ("Del Beg", lambda: self.op(4), "#d9534f", 1, 0), ("Del End", lambda: self.op(5), "#d9534f", 1, 1), ("Del Pos", lambda: self.op(6), "#d9534f", 1, 2),
            ("Search", lambda: self.op(7), "#f0ad4e", 2, 0),  ("Length", lambda: self.op(8), "#5cb85c", 2, 1),  ("Clear", self.clr, "#6c757d", 2, 2)
        ]
        for t, cmd, c, r, col in opts:
            tk.Button(bf, text=t, command=cmd, bg=c, fg="white", width=12).grid(row=r, column=col, padx=4, py=4)

    def view(self):
        el = self.dll.get_elements()
        self.lbl.config(text=" <-> ".join(el) if el else "List Empty", fg="green" if el else "red")

    def get_val(self, e):
        try: return int(e.get())
        except ValueError: messagebox.showerror("Error", "Invalid Integer Input."); return None

    def op(self, choice):
        try:
            if choice in (1, 2, 3, 7) and (d := self.get_val(self.e_data)) is None: return
            if choice in (3, 6) and (p := self.get_val(self.e_pos)) is None: return
            
            if choice == 1: self.dll.insert_at_beginning(d)
            elif choice == 2: self.dll.insert_at_end(d)
            elif choice == 3: self.dll.insert_at_position(d, p)
            elif choice == 4: self.dll.delete_node_at_beginning()
            elif choice == 5: self.dll.delete_node_at_end()
            elif choice == 6: self.dll.delete_node_at_position(p)
            elif choice == 7: messagebox.showinfo("Result", "Found" if self.dll.search_node(d) else "Not Found")
            elif choice == 8: messagebox.showinfo("Length", f"Size: {self.dll.length_of_list()}")
            self.view()
        except IndexError as e: messagebox.showerror("Error", str(e))

    def clr(self):
        self.e_data.delete(0, tk.END); self.e_pos.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    DLLGui(root)
    root.mainloop()
