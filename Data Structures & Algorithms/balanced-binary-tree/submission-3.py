# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Use DFS because balance depends on the height of each subtree.

        The idea is:
        - for every node, check if its left and right subtrees are balanced
        - also get the height of each subtree
        - a node is balanced if both subtrees are balanced and their heights differ by at most 1

        So each DFS call returns two things:
        - whether this subtree is balanced
        - the height of this subtree

        TC: O(n), where n is the number of nodes
        SC: O(h), where h is the height of the tree due to the recursion stack
        '''
        
        def dfs(root):
            # Base case: an empty subtree is balanced and has height 0.
            if not root:
                return [True, 0]
            
            # Get balance status and height from both subtrees.
            left = dfs(root.left)
            right = dfs(root.right)

            # Current subtree is balanced only if:
            # both children are balanced and their heights differ by at most 1.
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

            # Return whether this subtree is balanced, plus its height.
            return [balanced, 1 + max(left[1], right[1])]
        
        result = dfs(root)
        return result[0]