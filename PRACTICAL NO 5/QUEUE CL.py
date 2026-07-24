import time
import os
from colorama import Fore, Style, init
from collections import deque

class Queue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def enqueue(self, item):
        if len(self.queue) == self.size:
            print("Queue Overflow! Queue is full.")
        else:
            self.queue.append(item)
            print(f"{item} inserted into the queue.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow! Queue is empty.")
        else:
            item = self.queue.popleft()
            print(f"{item} deleted from the queue.")

    def traverse(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:")
            for item in self.queue:
                print(item, end=" ")
            print()

    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


# Main Program
size = int(input("Enter the maximum size of the queue: "))
q = Queue(size)

while True:
    print("\n====== Queue Operations ======")
    print("1. Insert (Enqueue)")
    print("2. Delete (Dequeue)")
    print("3. Traverse")
    print("4. View Front Element")
    print("5. Check if Queue is Empty")
    print("6. Check if Queue is Full")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter the element: ")
        q.enqueue(value)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        q.traverse()

    elif choice == "4":
        q.front()

    elif choice == "5":
        if q.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == "6":
        if q.is_full():
            print("Queue is full.")
        else:
            print("Queue is not full.")

    elif choice == "7":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")
