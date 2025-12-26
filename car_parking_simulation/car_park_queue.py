class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Create a queue
myQueue = Queue()
while True:
    try:
        queue_count = int(input("How many values would you like to input? (1-10): "))
        if 1 <= queue_count <= 10:
            break
        else:
            print("Please limit your input to 10 only.")
    except ValueError:
        print("Error: Invalid input. Please enter a number")

for i in range(queue_count):
    value = input(f"Enter value for Node {i+1} of {queue_count}: ")
    myQueue.enqueue(value)

print("\n")
print("Queue Results")
print("Queue: ", myQueue.queue)
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

# Comments:
    # 1. Add a code that ask user which value are to be dequeue; If they want to dequeue all
    #    elements until the queue is empty
    # 2. Add random to generate values if user doesn't want to manually input values