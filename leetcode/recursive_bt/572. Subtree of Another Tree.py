# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        For each node inside the root tree, we just want to ask the question if this node 
        can be the root of the subtree 

        1. traverse each node of the root 

        2. if the val is the same --> then check the subtree, simply the same as previous code 
        """
        

        if not root: 
            return False  

        # we dont need this since same tree would check the values for us already 
        # if root.val == subRoot.val: 
            # check = isSameTree(root, subroot)
            # return check
        if self.isSameTree(root, subRoot):
            return True 

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
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


