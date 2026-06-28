# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Use the BST property iteratively.

        The idea is:
        - if both p and q are smaller than root, move left
        - if both p and q are greater than root, move right
        - otherwise, root is the split point, so it is the LCA

        This works because in a BST:
        - left subtree values are smaller than root
        - right subtree values are greater than root

        TC: O(h), where h is the height of the tree
        SC: O(1), because we are not using recursion
        '''

        curr = root

        while curr:
            # If both nodes are smaller, the LCA must be in the left subtree.
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # If both nodes are greater, the LCA must be in the right subtree.
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                # Otherwise, this is the split point.
                # This also covers the case where curr is equal to p or q.
                return curr