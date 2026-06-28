# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Use DFS to check every node in root as a possible starting point for subRoot.

        The idea is:
        - if subRoot is empty, it is always a subtree
        - if root is empty but subRoot is not, then subRoot cannot exist inside root
        - otherwise, check whether the current root matches subRoot exactly
        - if not, recursively search the left and right subtrees

        The helper sameTree checks whether two trees are exactly identical.

        TC: O(n * m), where n is the number of nodes in root and m is the number of nodes in subRoot
        SC: O(h), where h is the height of root due to recursion stack
        '''
        if not subRoot:
            return True

        if not root:
            return False
        
        # If the tree starting at this node matches subRoot exactly, we found the subtree.
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, keep searching for subRoot in the left and right subtrees.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, root, subRoot):
        # If both nodes are empty, this part of both trees matches.
        if not root and not subRoot:
            return True
        
        # If only one node is empty, the structures are different.
        if not root or not subRoot:
            return False
        
        # Values must match for the trees to be identical.
        if root.val != subRoot.val:
            return False
        
        # Both left subtrees and right subtrees must match.
        return (
            self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right)
        )