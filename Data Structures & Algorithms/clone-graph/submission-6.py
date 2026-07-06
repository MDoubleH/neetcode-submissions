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
        Have a dictionary that's a defaultdict list
        This will store the new to cloned node - that way we can keep track of cloned node and call it back

        we want to go through each node, and clone it -> passing in its neighbours and value
        We want to add this to our dict and call dfs on its neighbours so we do not recreate nodes but also so we can visit all nodes
        then just simply return the node at the end
        '''

        if not node:
            return None

        old_to_new = defaultdict(list)

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node()
            new_node.val = node.val
            old_to_new[node] = new_node

            for neighbour in node.neighbors:
                new_node.neighbors.append(dfs(neighbour))
            
            return new_node
        
        dfs(node)
        return old_to_new[node]


