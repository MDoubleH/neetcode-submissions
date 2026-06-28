# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Use the BST property to find the lowest common ancestor.

        The idea is:
        - if both p and q are smaller than root, their LCA must be in the left subtree
        - if both p and q are greater than root, their LCA must be in the right subtree
        - otherwise, root is the split point, so root is the lowest common ancestor

        This works because in a BST:
        - left subtree values are smaller than root
        - right subtree values are greater than root

        TC: O(h), where h is the height of the tree
        SC: O(h), due to the recursive call stack
        '''

        # If root is either p or q, then root is the lowest common ancestor.
        if q.val == root.val or p.val == root.val:
            return root

        # If both nodes are smaller than root, search left.
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both nodes are greater than root, search right.
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise, p and q are on different sides, so root is the split point.
        else:
            return root