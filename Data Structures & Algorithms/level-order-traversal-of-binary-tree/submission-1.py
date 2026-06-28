from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Use BFS because we want to process the tree level by level.

        The idea is:
        - use a queue to store nodes we still need to visit
        - for each loop, process exactly the nodes currently in the queue
        - those nodes represent one full level of the tree
        - collect their values, then add their children for the next level

        This works because BFS naturally explores nodes in level order.

        TC: O(n), where n is the number of nodes
        SC: O(n), because the queue/result can store up to n nodes/values
        '''
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            # This stores all values for the current level.
            level = []

            # len(q) is the number of nodes in the current level.
            # We only process these nodes before moving to the next level.
            for _ in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                # Add children to the queue so they are processed in the next level.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # After processing one full level, add it to the result.
            res.append(level)
        
        return res