# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        The kth smallest value

        If following the propery of BST, it tells use to go either left or right branch

        But how do we actaully know the value, since we dont reall know what is K 

        inorder traversal --> left, root, right 

        try
        -----
        traverse the tree inorder style --> 1 2 3 4 --> then take the kth, since we would get a sorted order 

        O(n) space + time 
        """

        nodes = []


        def dfs(root): 

            if root is None: 
                return 

            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
            return 

        dfs(root)
        return nodes[k-1]


"""
Optimized Approach 
------------------
If we need to keep querying, then could be costly with the above approach 

O(N) time and O(1) space 

A smarter way to note is that in-order --> always yields us the smallest element first, then the next smallest due to BST nature 


Hence we can control the number of traversals until we hit the kth smallest

"""
    # note that we cant do this since we cant modify a variable, but we can modify as LIST ! 
    # count = 0 

    # def dfs(root): 
    #     if root is None: 
    #         return 

    #     if count == k: 
    #         return root.val 

    #     dfs(root.left)
    #     count +=1 
    #     dfs(root.right)
    #     return 

    count = [0]  # Use list to make it mutable
    result = [None]
    
    def dfs(root): 
        if root is None or count[0] >= k: 
            return 
        
        dfs(root.left)
        
        count[0] += 1
        if count[0] == k:
            result[0] = root.val
            return
        
        dfs(root.right)
    
    dfs(root)
    return result[0]

    # of course another way is to return results from the recursion itself, rather than mutating the variables 

    def dfs(root, count): 
        if root is None: 
            return count, None
        
        count, result = dfs(root.left, count)
        if result is not None:
            return count, result
        

        # we would only come here once we finish traversing the most left, and thus the leaf_left is the smallest ==> count+1
        count += 1
        if count == k:
            return count, root.val
        
        count, result = dfs(root.right, count)
        return count, result
    
    _, result = dfs(root, 0)
    return result