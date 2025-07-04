class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 
        
class doublyQueue:
    def __init__(self):
        self.front = None
        self.last = None
        
    def is_empty(self):
        if self.front is None:
            return None
        
    def enqueue(self,value):
        if self.front is None:
            self.front = Node(value)
            self.last = self.front
            
        else:
            self.last.next = Node(value)
            self.last.next.prev = self.last
            self.last =self.last.next    
                       
                       
    def dequeue(self,value):
        if self.front is None:
          
         return None
         
        else:
            temp = self.front.value
            self.front = self.front.next
            
            if self.front:
                self.front.prev = None
            
            return temp    
            
    def first(self):
     return self.front.value
 
    def size(self):
     temp = self.front
     count = 0
     while temp is not None:
         count += 1
         temp = temp.next
     return count

    
    def isEmpty(self):
        return self.head is None
                  
                  
    def printqueue(self):
        print("queue elements are:")
        temp = self.front
    while temp is not None:
        print(temp.front, end="->")
        temp = temp.next
             