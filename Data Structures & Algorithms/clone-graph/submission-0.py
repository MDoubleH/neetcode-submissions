"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Keep track of a copy of the cloned nodes with an old to new dictionary
        Go through nodes in a recursive / dfs fashion
        If the node we look at already exists in our dictionary aka has a clone then return that
        Else we must create a new copy node with a new value 
        We must also populate the clone node's neighbours - go through original nodes neighbours
        and for the new copy node, append to its list of neighbours a call to the dfs with that node so we add a copy
        at the end return the cloned node
        '''

        original_to_copy = {}

        def clone(node):
            if node in original_to_copy:
                return original_to_copy[node]
            
            new_clone_node = Node(node.val)
            original_to_copy[node] = new_clone_node

            for neighbor in node.neighbors:
                new_clone_node.neighbors.append(clone(neighbor))
            
            return new_clone_node
        
        if node:
            return clone(node)
        else:
            return None

