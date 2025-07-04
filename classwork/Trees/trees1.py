class TreeNode:
    def __init__(self, value,left=None, right=None):
       self.value = value
       self.left = left 
       self.right = right 
       
    def __str__(self):
        return str(self.value)   
    
    def pre_order(node):
        if not node:
            return
        
        print(node)
        pre_order(node.left)
        pre_order(node.right)
        
      
        
if __name__ == "__main__":
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4) 
    E = TreeNode(5)
    F = TreeNode(10)
    
    A.left = B
    A.right = C
    B.left = D
    B.right = E   
    C.right = F
    
   