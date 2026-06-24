from collections import defaultdict

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
        Use DFS with a hash map to clone the graph.

        The idea is:
        - old_to_new maps each original node to its cloned node
        - if we see a node that already exists in the map, return its clone
        - otherwise, create the clone, store it in the map, then clone its neighbours

        This works because graphs can have cycles.
        Without the map, we could keep revisiting the same nodes forever.

        TC: O(V + E), where V is the number of nodes and E is the number of edges
        SC: O(V), because we store one clone per original node
        '''
        if not node:
            return None

        # Maps original node -> cloned node.
        # This prevents duplicate clones and handles cycles.
        old_to_new = {}

        def dfs(node):
            # If this node has already been cloned, return the existing clone.
            if node in old_to_new:
                return old_to_new[node]
            
            # Create a clone of the current node.
            new_node = Node()
            old_to_new[node] = new_node

            # Copy the node value.
            new_node.val = node.val
            
            # Clone each neighbour and connect it to this cloned node.
            for neighbour in node.neighbors:
                new_node.neighbors.append(dfs(neighbour))
            
            return new_node
        
        
        return dfs(node)