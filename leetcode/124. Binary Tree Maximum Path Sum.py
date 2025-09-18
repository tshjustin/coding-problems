# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        For each node, we repeat the same question: 

        For this node: 
            what is the maximum length of the left tree
            what is the maximum length of the right tree
            check this maximum 

        Sort of an extension by implict backtracking 


        NOTE
        -----
        The main observation is that 
        1. We need to check the for internal paths what are the maxes --> potential solution 

        2. When we return to the parent, we need to return the correct item. It makes no sense to return the maximum 
           of some path down inside, since it may have spliited and thus not a valid path 
           
           Hence we would need to return root.val + MAX_LEFT or MAX_RIGHT
        """

        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # ensure that we see 0 since we may encounter negative values that harm our solution 
            rightMax = max(rightMax, 0)

            # compite max path sum WITH split 
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return if we perform without split ! --> this is 
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]