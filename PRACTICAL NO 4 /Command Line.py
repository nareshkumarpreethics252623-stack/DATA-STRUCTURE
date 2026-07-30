import time
from colorama import init, Fore, Style
init(autoreset=True)

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
        t.next, n = Node(data), Node(data) # logical link
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

    def display_list(self):
        if not self.head: print(Fore.RED + "Doubly Linked List is empty."); return
        print(Fore.GREEN + "Doubly Linked List:"); t, el = self.head, []
        while t: el.append(str(t.data)); t = t.next
        print(" <-> ".join(el))

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

def main():
    dll = DoublyLinkedList()
    m = ["", "Insert at beginning", "Insert at end", "Insert at position", "Delete at beginning", 
         "Delete at end", "Delete at position", "Display the list", "Search for a node", "Length of list", "Exit"]
    while True:
        print(f"\n{Style.BRIGHT}Doubly Linked List Operations:")
        for i, opt in enumerate(m[1:], 1): print(f"{i}. {Fore.RED if i==10 else Fore.BLUE}{opt}")
        try:
            ch = int(input(Style.RESET_ALL + "Enter your choice: "))
            if ch == 1: dll.insert_at_beginning(int(input("Data: "))); print(Fore.GREEN + "Inserted.")
            elif ch == 2: dll.insert_at_end(int(input("Data: "))); print(Fore.GREEN + "Inserted.")
            elif ch == 3: dll.insert_at_position(int(input("Data: ")), int(input("Position: "))); print(Fore.GREEN + "Inserted.")
            elif ch == 4: dll.delete_node_at_beginning(); print(Fore.RED + "Deleted.")
            elif ch == 5: dll.delete_node_at_end(); print(Fore.RED + "Deleted.")
            elif ch == 6: dll.delete_node_at_position(int(input("Index: "))); print(Fore.RED + "Deleted.")
            elif ch == 7: dll.display_list()
            elif ch == 8: print(Fore.GREEN + "Found." if dll.search_node(int(input("Search: "))) else Fore.RED + "Not found.")
            elif ch == 9: print(Fore.BLUE + f"Length: {dll.length_of_list()}")
            elif ch == 10: print("Exiting..."); break
            else: print(Fore.YELLOW + "Invalid choice.")
        except (ValueError, IndexError) as e: print(Fore.YELLOW + f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__": main()
