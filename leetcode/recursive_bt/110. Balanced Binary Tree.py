# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Note that for each node, we must ensure that the left and right height difference is by 1 only 

        The problem in this case is that we would need to return 

        1. Solution which is T / F 

        2. for each node, the height of the left and right tree 

        If we create another function to find the height, then for each node, perfrom DFS which is costly

        Hence we just need to be smart of what we return --> tuple format 

        ( 1 + height , violation) --> but hard to think lol 
        """

        sol = [True]

        def dfs(root): 

            if not root: 
                return 0

            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1: 
                sol[0] = False 

            
            return 1 + max(left_height, right_height)


        dfs(root)
        return sol[0]

        """
        A more optimzied solution with early termination and return values  


        """
        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
            
        #     # Early return if subtrees are already unbalanced
        #     if not left[0] or not right[0]:
        #         return [False, 0]
            
        #     balanced = abs(left[1] - right[1]) <= 1
        #     return [balanced, 1 + max(left[1], right[1])]
                    