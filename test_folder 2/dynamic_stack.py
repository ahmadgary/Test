class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None  # Return None if stack is empty

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top item:", stack.peek())  # Output: 30
print("Popped item:", stack.pop())  # Output: 30
print("Stack size:", stack.size())  # Output: 2