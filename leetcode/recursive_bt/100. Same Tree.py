# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ 
        Now we are not too concerned about returning the height of the tree

        """

        # base cases for both 
        if not p and not q:
            return True 

        # check 1  -> if the nodes exist 
        if (p and not q) or (q and not p): 
            return False 

        # check 2 -> if the values are the same if both the nodes exist 
        if p.val != q.val:
            return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        