
#Create a Node class to make node objects

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Create a LinkedList class to make linked list objects        
class LinkedList:
    def __init__(self):
        self.head = None   
        
#insert a new node at the start of the linked list   
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
         new_node.next = self.head
         self.head = new_node

    # def add_two_lists(self,l1,l2):
    #     if not l1 and not l2 :
    #         return None
        
    #     value1

#insert a new node at the end of the linked list
    def insert_at_end(self ,data):
        new_node = Node(data)
        if self.head == None: 
           self.head = new_node
           return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
         
#insert at a position in the linked list
    def insert_at_an_index(self,index,data):
        if (index == 0):
            self.insert_at_start(data)
            return
        
        current_node = self.head
        position = 0  
        while(current_node != None and position + 1 != index):
            current_node = current_node.next
            position += 1
        
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index is not found")
         
         
  #update a node in the linked list
    def update_node(self,index,data):
        current_node = self.head
        position = 0
        if(position == index):
            current_node.data = data
        else:
            while(current_node is not None and position is not index):
                position += 1
                current_node = current_node.next 
            if(current_node is not None):
                current_node.data = data
            else:
                print("Index not found")                          
 
#remove first node of linked list
    def remove_from_beginning(self):
        if(self.head is None):
            return
        self.head = self.head.next
 
 #remove from the end of the list
    def remove_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
         self.head = None
         return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None    
        
  #search for a specific value
    def search(self,data):
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == data:
                return f"Value '{data}' found at position {position}"
            current_node = current_node.next
            position += 1
        return f"Value '{data}' not found in the list"         
 
 
     #Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("\n")
        
        
ll = LinkedList()
ll2 = LinkedList()

ll.insert_at_start(4)
ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_start(5)

ll2.insert_at_start(1)
ll2.insert_at_start(4)
ll2.insert_at_start(6)
ll2.insert_at_start(2)


ll.print_list()
ll2.print_list()


# ll.insert_at_end('jumps')
# ll.print_list()

# ll.remove_from_beginning()
# print("List after deletion:")
# ll.print_list()

# print(ll.search('quick'))
# print(ll.search('lazy'))


# ll.print_list()
        
