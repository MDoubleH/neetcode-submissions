from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Use BFS because we want to process the tree level by level.

        The idea is:
        - the right side view contains the first node we would see at each level
          if we look from the right
        - so for each level, process the right child before the left child
        - then the first node we pop at each level is the visible node

        This works because BFS separates the tree into levels, and adding right children
        before left children means the rightmost node is processed first.

        TC: O(n), where n is the number of nodes
        SC: O(n), because the queue can store nodes from a level
        '''

        res = []
        q = deque()

        # If the tree is not empty, start BFS from the root.
        if root:
            q.append(root)

        while q:
            # We only want to add one node per level.
            isAdded = False

            # Process exactly one level at a time.
            for _ in range(len(q)):
                node = q.popleft()

                # Since we add right children first, the first node in this level
                # is the one visible from the right side.
                if not isAdded:
                    res.append(node.val)
                    isAdded = True
                
                # Add right before left so the next level is also processed right-first.
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return res