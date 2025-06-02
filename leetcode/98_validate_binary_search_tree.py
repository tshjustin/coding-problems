# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST is one where all nodes follow the same rule: 

        left_val < mid_val < right_val 


        its a global constraint, hence if the current node is X, then all nodes to the left of it 
        must be < X 


        Top down or bottom up ? 

        top down => allows us to understand the global constraints 

        bottom up => would only allow us to check local left right

        """

        def check(root, left_val=float('-inf'), right_val=float('inf')): 

            # check violation 1 
            if not root: 
                return True 

            if not (left_val < root.val < right_val):
                return False 


            return check(root.left, left_val, root.val) and check(root.right, root.val, right_val)

        return check(root)




        