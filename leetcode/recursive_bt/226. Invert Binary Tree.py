# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: 
            return None


        # traverse the left sub tree 
        self.invertTree(root.left)
        self.invertTree(root.right) # note that we must do in post traversal left,right,root 

        # once we reach the end, then we would swap 
        tmp = root.left 
        root.left = root.right 
        root.right = tmp 

        return root 
        