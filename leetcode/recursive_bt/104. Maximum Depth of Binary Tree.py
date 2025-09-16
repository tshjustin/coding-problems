# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0 

        
        # search the left tree
        left_depth = self.maxDepth(root.left)

        right_depth = self.maxDepth(root.right)

        if left_depth > right_depth: 
            return left_depth + 1

        else: 
            return right_depth + 1

        return max(left_depth, right_depth)
        