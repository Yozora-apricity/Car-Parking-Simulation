class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

# Create a stack
myStack = Stack()

while True:
    try:
        stack_count = int(input("How many values would you like to input? (1-10): "))
        if 1 <= stack_count <= 10:
            break
        else:
            print("Please limit your input to 10 only.")
    except ValueError:
        print("Error: Invalid input. Please enter a number")

for i in range(stack_count):
    value = input(f"Enter value for Node {i+1} of {stack_count}: ")
    myStack.push(value)

print("\n")
print("Stack Results")
print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

# Comments:
    # 1. Add a code that ask user which value are to be pop; If they want to pop all
    #    elements until the stack is empty
    # 2. Add random to generate values if user doesn't want to manually input values