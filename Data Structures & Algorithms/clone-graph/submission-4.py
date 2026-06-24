class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Use DFS with a hash map to clone the graph.

        TC: O(V + E), where V is the number of nodes and E is the number of edges
        SC: O(V), because we store one clone per original node
        '''
        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node(node.val)
            old_to_new[node] = new_node

            for neighbour in node.neighbors:
                new_node.neighbors.append(dfs(neighbour))
            
            return new_node
        
        return dfs(node)