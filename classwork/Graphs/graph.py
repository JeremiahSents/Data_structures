class Graph:
    def __init__(self,directed = False):
        self.directed = directed
        self.adj_list = dict()
    
    
    def __repr__(self):
       str_graph = ""
       
       for key,value in self.adj_list.items():
           str_graph += f"{key} -> {value}\n"
           
           return str_graph   
    
    
    def bfs(self):
        pass
    
    
    def dfs(self):
        pass
    
    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError(f"Node {node} already exists in the graph.")   
         
            
    def add_edge(self, from_node, to_node, weighted=None):
        
        self.add_node(to_node)
        
        if weighted is None:
              self.adj_list[from_node].add(to_node)
              
              if  self.directed:
                 self.adj_list[to_node].add(from_node)
        else:
             self.adj_list[from_node].add((to_node, weighted))
             
             if self.directed:
                    self.adj_list[to_node].add((from_node, weighted))
                    
                    
                    
    def obtain_nodes(self,key_node):
       return self.adj_list.get(key_node, set())                
    
    
    def adj_matrix(self):
        pass
    
if __name__ == "__main__":
    
    graph_obj = Graph() 
    
    print(graph_obj)         