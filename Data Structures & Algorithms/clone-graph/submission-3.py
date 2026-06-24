"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
old to new dict - map original node to new node - so if node already exist in dict then we just call it rather than create a new node
Recursively go through the nodes
if it exists in dict then compare it and see if its correct 
if it doesn't exist, create it
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        old_to_new = defaultdict(list)

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node()
            old_to_new[node] = new_node

            new_node.val = node.val
            
            for neighbour in node.neighbors:
                dfs(neighbour)
                new_node.neighbors.append(old_to_new[neighbour])
                
            
            return new_node
        
        dfs(node)
        return old_to_new[node]

            

        

        