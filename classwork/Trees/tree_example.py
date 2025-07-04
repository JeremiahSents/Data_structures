class TreeNode:
    
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
          
    def insert(self,key_value):
        
        if key_value < self.value:
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)     
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)        
                
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
            
            
        print(self.value, end=' ')              
        
        
    def  preorder_traversal(self):
        print(self.value)
        
        if self.left:
            self.left.inorder_traversal()
            
        if self.right:
            self.right.inorder_traversal()    
            
            
            
if __name__ == "__main__":
    root = TreeNode(10)
    
    root.insert(5)
    root.insert(4)
    root.insert(3)
    
    root.insert(23)
    root.insert(20)
    root.insert(18)
    
    print("Inorder Traversal:")
    root.inorder_traversal()
    
    print("\nPreorder Traversal:")
    root.preorder_traversal()            