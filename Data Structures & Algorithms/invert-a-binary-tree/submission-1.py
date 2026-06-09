# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Use DFS because we need to visit every node in the tree.

        The idea is:
        - at each node, swap its left and right child
        - then recursively do the same thing for its children

        This works because inverting a tree is a local operation:
        every node just needs its own children swapped.

        TC: O(n), where n is the number of nodes
        SC: O(h), where h is the height of the tree due to the recursion stack
        '''
        if not root:
            return None
        
        # Swap the left and right child of the current node.
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root