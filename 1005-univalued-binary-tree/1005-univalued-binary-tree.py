# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs (root , val):
            if not root:
                return True
            return root.val == val and bfs(root.left , root.val) and bfs(root.right , root.val)
        return bfs(root , root.val)