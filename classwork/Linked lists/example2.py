
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)   


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None        

current_node = node1

while True: 
        print(current_node.data,">>>", end=" ")
        if current_node.next is None:
            print(None)
            break
        current_node = current_node.next