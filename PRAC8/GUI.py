import heapq
import tkinter as tk
from tkinter import messagebox, scrolledtext


class AVLNode:
    def __init__(self, key):
        self.key, self.height, self.left, self.right = key, 1, None, None


class AVLTree:
    def h(self, n): return n.height if n else 0
    def b(self, n): return self.h(n.left) - self.h(n.right) if n else 0

    def left(self, z):
        y, z.right = z.right, z.right.left
        y.left = z
        z.height = 1 + max(self.h(z.left), self.h(z.right))
        y.height = 1 + max(self.h(y.left), self.h(y.right))
        return y

    def right(self, z):
        y, z.left = z.left, z.left.right
        y.right = z
        z.height = 1 + max(self.h(z.left), self.h(z.right))
        y.height = 1 + max(self.h(y.left), self.h(y.right))
        return y

    def insert(self, r, k):
        if not r: return AVLNode(k)
        if k < r.key: r.left = self.insert(r.left, k)
        else: r.right = self.insert(r.right, k)

        r.height = 1 + max(self.h(r.left), self.h(r.right))
        bal = self.b(r)

        if bal > 1 and k < r.left.key: return self.right(r)
        if bal < -1 and k > r.right.key: return self.left(r)
        if bal > 1 and k > r.left.key:
            r.left = self.left(r.left)
            return self.right(r)
        if bal < -1 and k < r.right.key:
            r.right = self.right(r.right)
            return self.left(r)
        return r

    def preorder(self, r):
        return [] if not r else [r.key] + self.preorder(r.left) + self.preorder(r.right)


class App:
    def __init__(self, root):
        self.avl, self.rootnode, self.tasks = AVLTree(), None, []

        root.title("AVL, Heap & Priority Queue")
        root.geometry("700x550")

        tk.Label(root, text="AVL Tree").pack()
        self.avlE = tk.Entry(root)
        self.avlE.pack()
        tk.Button(root, text="Insert", command=self.insert).pack()
        tk.Button(root, text="Show AVL", command=self.show).pack()

        tk.Label(root, text="Heap Data (1,2,3)").pack()
        self.heapE = tk.Entry(root)
        self.heapE.pack()
        tk.Button(root, text="Min Heap", command=self.minheap).pack()
        tk.Button(root, text="Max Heap", command=self.maxheap).pack()

        tk.Label(root, text="Priority").pack()
        self.p = tk.Entry(root)
        self.p.pack()

        tk.Label(root, text="Task").pack()
        self.t = tk.Entry(root)
        self.t.pack()

        tk.Button(root, text="Add Task", command=self.add).pack()
        tk.Button(root, text="Run Tasks", command=self.run).pack()

        self.out = scrolledtext.ScrolledText(root, width=80, height=15)
        self.out.pack()

    def insert(self):
        try:
            self.rootnode = self.avl.insert(self.rootnode, int(self.avlE.get()))
            self.out.insert(tk.END, "Inserted\n")
            self.avlE.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Enter Integer")

    def show(self):
        self.out.insert(tk.END, "AVL: " + str(self.avl.preorder(self.rootnode)) + "\n")

    def minheap(self):
        d = list(map(int, self.heapE.get().split(",")))
        heapq.heapify(d)
        self.out.insert(tk.END, "Min Heap: " + str(d) + "\n")

    def maxheap(self):
        d = [-int(x) for x in self.heapE.get().split(",")]
        heapq.heapify(d)
        self.out.insert(tk.END, "Max Heap: " + str([-i for i in d]) + "\n")

    def add(self):
        heapq.heappush(self.tasks, (int(self.p.get()), self.t.get()))
        self.out.insert(tk.END, "Task Added\n")
        self.p.delete(0, tk.END)
        self.t.delete(0, tk.END)

    def run(self):
        self.out.insert(tk.END, "\nTasks:\n")
        while self.tasks:
            p, t = heapq.heappop(self.tasks)
            self.out.insert(tk.END, f"{p} -> {t}\n")


root = tk.Tk()
App(root)
root.mainloop()
