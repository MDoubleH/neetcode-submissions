# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            isAdded = False
            for _ in range(len(q)):
                node = q.popleft()

                if not isAdded:
                    res.append(node.val)
                    isAdded = True
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return res
