class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class CircularLinkedListQueue:
    def __init__(self):
        self.rear = None 
        self.size = 0 
    
    def enqueue(self, item):
        new_node = ListNode(item)
        
        if self.is_empty():
            # First node in circular list points to itself
            new_node.next = new_node
            self.rear = new_node
        else:
            # Insert new node between rear and front
            new_node.next = self.rear.next  # Point to current front
            self.rear.next = new_node       # Current rear points to new node
            self.rear = new_node            # Update rear to new node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # Front is always rear.next in circular list
        front = self.rear.next
        item = front.val
        
        if self.size == 1:
            self.rear = None
        else:
            self.rear.next = front.next
        
        self.size -= 1
        return item
    
    def is_empty(self):
        return self.rear is None
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.rear.next.val


def is_palindrome_using_stack(s: str) -> bool:
    stack = [] 
    queue = CircularLinkedListQueue()
    
    for char in s:
        stack.append(char)   # Push onto stack (add to end of list)
        queue.enqueue(char)  # Enqueue into queue (add to rear of circular list)
    
    while stack and not queue.is_empty():
        stack_char = stack.pop()  # Remove from end of list
        queue_char = queue.dequeue()  # Remove from front of circular list
    
        if stack_char != queue_char:
            return False
    
   
    return True

if __name__ == "__main__":
    test_strings = ["racecar", "hello", "deified", "python", "madam"]
    
    for test_string in test_strings:
        result = is_palindrome_using_stack(test_string)
        print(f"'{test_string}' is{' ' if result else ' not '}a palindrome")