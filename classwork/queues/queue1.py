class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.rear=self.front = new_node
            self.printQueue()
        else:
         self.rear.next = new_node
         self.rear = new_node
         self.printQueue()    
     
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.printQueue()

    def printQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        queue_string = "Current Queue: "
        while temp is not None:
            queue_string += str(temp.value) + " "
            temp = temp.next
        print(queue_string.strip())
        

q = Queue()

# Enqueue elements into the queue
q.enqueue(10)
q.enqueue(20)

# Dequeue elements from the queue
q.dequeue()
q.dequeue()

# Enqueue more elements into the queue
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Dequeue an element from the queue
q.dequeue        