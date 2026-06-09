# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Use DFS because the depth of a tree depends on the depth of its subtrees.

        The idea is:
        - if the current node is None, its depth is 0
        - otherwise, the depth is 1 for the current node
          plus the maximum depth of its left or right subtree

        This works because the max depth is the longest path from the root
        down to any leaf node.

        TC: O(n), where n is the number of nodes
        SC: O(h), where h is the height of the tree due to the recursion stack
        '''
        
        # Base case: an empty tree has depth 0.
        if not root:
            return 0

        # Current node adds 1 level, then we take the deeper of the two subtrees.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))