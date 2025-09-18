# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        when traversing a path, just track the maximum value of that path 

        if the next node we visit is greater than this maxima,
            then its not a good node 

        else good node 

        if we find a larger value, then we update 



        1. now the probelm is that for the right subtree from the root, it does not have the same max val, el
            Note that this is implictyl handled from the natural backtracking 
        """

        sol = [0]

        def dfs(root, path_max): 

            if not root: 
                return 

            if root.val >= path_max: 
                sol[0] += 1
            
            path_max = max(path_max, root.val)

            dfs(root.left, path_max)
            dfs(root.right, path_max)
        
        dfs(root, float('-inf'))
        return sol[0]


        