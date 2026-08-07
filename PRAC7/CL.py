import heapq
from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded_data = "".join(codebook[ch] for ch in data)

    return encoded_data, codebook, frequencies


def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    code = ""

    for bit in encoded_data:
        code += bit
        if code in reverse:
            decoded += reverse[code]
            code = ""

    return decoded


class HuffmanGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding Visualizer")
        self.root.geometry("750x650")
        self.root.configure(bg="#E8F6F3")

        self.codebook = {}
        self.encoded = ""

        title = tk.Label(root,
                         text="Huffman Coding Compression",
                         font=("Arial", 18, "bold"),
                         bg="#E8F6F3",
                         fg="navy")
        title.pack(pady=10)

        tk.Label(root,
                 text="Enter Text:",
                 font=("Arial", 12),
                 bg="#E8F6F3").pack()

        self.input_entry = tk.Entry(root,
                                    font=("Arial", 12),
                                    width=60)
        self.input_entry.pack(pady=5)

        frame = tk.Frame(root, bg="#E8F6F3")
        frame.pack(pady=10)

        ttk.Button(frame,
                   text="Encode",
                   command=self.encode).grid(row=0,
                                             column=0,
                                             padx=10)

        ttk.Button(frame,
                   text="Decode",
                   command=self.decode).grid(row=0,
                                             column=1,
                                             padx=10)

        ttk.Button(frame,
                   text="Clear",
                   command=self.clear).grid(row=0,
                                            column=2,
                                            padx=10)

        self.output = scrolledtext.ScrolledText(root,
                                                width=85,
                                                height=25,
                                                font=("Courier", 10))
        self.output.pack(pady=10)

    def encode(self):

        text = self.input_entry.get()

        if text == "":
            messagebox.showerror("Error", "Please enter some text.")
            return

        self.output.delete(1.0, tk.END)

        encoded, self.codebook, freq = huffman_encoding(text)
        self.encoded = encoded

        self.output.insert(tk.END, "Character Frequencies\n")
        self.output.insert(tk.END, "----------------------\n")

        for k, v in freq.items():
            self.output.insert(tk.END, f"{k} : {v}\n")

        self.output.insert(tk.END, "\nHuffman Codebook\n")
        self.output.insert(tk.END, "----------------------\n")

        for k, v in self.codebook.items():
            self.output.insert(tk.END, f"{k} : {v}\n")

        self.output.insert(tk.END, "\nEncoded Data\n")
        self.output.insert(tk.END, "----------------------\n")
        self.output.insert(tk.END, encoded)

    def decode(self):

        if self.encoded == "":
            messagebox.showinfo("Info", "Please encode first.")
            return

        decoded = huffman_decoding(self.encoded,
                                   self.codebook)

        self.output.insert(tk.END, "\n\nDecoded Data\n")
        self.output.insert(tk.END, "----------------------\n")
        self.output.insert(tk.END, decoded)

    def clear(self):
        self.input_entry.delete(0, tk.END)
        self.output.delete(1.0, tk.END)
        self.codebook = {}
        self.encoded = ""


root = tk.Tk()
app = HuffmanGUI(root)
root.mainloop()
