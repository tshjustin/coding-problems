# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Notice that the solution can be found by: 

        1. Going to the smallest leaf node 
        2. invert the child 
        3. invert the parent of that child 
        4. invert the inverted parent of that child 
        ...

        so start from the leaf node first..
        """

        if not root: 
            return 

        # traverse all the way to the child node 
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        temp = root.right
        root.right = root.left
        root.left = temp

        return root
        