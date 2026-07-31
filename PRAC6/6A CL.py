class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item, priority):
        if self.is_full():
            print("Priority Queue Overflow!")
        else:
            self.queue.append((priority, item))
            print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue Underflow!")
            return

        highest = min(self.queue, key=lambda x: x[0])
        self.queue.remove(highest)
        print(f"Dequeued: {highest[1]} with priority {highest[0]}")

    def traverse(self):
        if self.is_empty():
            print("Priority Queue is Empty.")
        else:
            print("\nPriority Queue:")
            for priority, item in self.queue:
                print(f"Item: {item}  Priority: {priority}")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def ascending(self):
        if self.is_empty():
            print("Priority Queue is Empty.")
        else:
            print("\nAscending Order:")
            for priority, item in sorted(self.queue):
                print(f"Item: {item}  Priority: {priority}")

    def descending(self):
        if self.is_empty():
            print("Priority Queue is Empty.")
        else:
            print("\nDescending Order:")
            for priority, item in sorted(self.queue, reverse=True):
                print(f"Item: {item}  Priority: {priority}")


#Main Program
def main():
    pq = PriorityQueue(5)

    while True:
        print("\nPriority Queue Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Traverse")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Show Ascending Order")
        print("7. Show Descending Order")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            priority = int(input("Enter priority: "))
            pq.enqueue(item, priority)

        elif choice == "2":
            pq.dequeue()

        elif choice == "3":
            pq.traverse()

        elif choice == "4":
            if pq.is_empty():
                print("Priority Queue is Empty.")
            else:
                print("Priority Queue is Not Empty.")

        elif choice == "5":
            if pq.is_full():
                print("Priority Queue is Full.")
            else:
                print("Priority Queue is Not Full.")

        elif choice == "6":
            pq.ascending()

        elif choice == "7":
            pq.descending()

        elif choice == "8":
            print("Program Ended.")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
