# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Use DFS because for each node, we need to know the height of its left
        and right subtrees.

        The idea is:
        - the longest path through a node is left height + right height
        - we update the global answer with that value at every node
        - then we return the height of the current subtree back to its parent

        This works because the diameter may or may not pass through the root,
        so we check every node as a possible "middle" of the longest path.

        TC: O(n), where n is the number of nodes
        SC: O(h), where h is the height of the tree due to the recursion stack
        '''
        self.res = 0

        def dfs(root):
            # Base case: an empty subtree has height 0.
            if not root:
                return 0

            # Get the height of the left and right subtrees.
            left = dfs(root.left)
            right = dfs(root.right)

            # If the longest path goes through this node,
            # it would use the deepest path on the left + deepest path on the right.
            self.res = max(self.res, left + right)

            # Return this subtree's height to the parent.
            # We add 1 to include the current node.
            return 1 + max(left, right)

        dfs(root)
        return self.res