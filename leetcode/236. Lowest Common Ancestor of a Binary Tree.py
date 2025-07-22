# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1. Since its a BT and not a BST, we need to find the position of the nodes

        explore left
        do something 
        explore right 

        2. the condition for LCA is that we would need to know the parents of p and q 
        3. and it needs to be the deepest as possible 
        4. hence p and q both gives a lowest bound to which the solution can exist at

        what i currently think: 
        1. use bfs and track the level which the p and q exist at 
        2. get the highest level of either, the solution would this lie [0, lower_bound]
        3. check the tree again 

        but how do i actually get the solution ? 

        given that i know the actual level,  i would still not know the actual position of the node 
        hence could be hard to trace back to the solution 

        Observation: 

        for the DFS solution , we ask the same question every node 
        In this case, at the current node, if we find the nodes p and q at the left and right tree (and the current node itself), then 
        then the current node is the LCA 

        but how do we know if p and q are in the left / right tree?
        if we use a function to check, then that means that for the current node, we perform a full recursion of left and right tree,
        then that means we get N(N) calls since for all the nodes we check all the other nodes

        hence we should do in one single pass 


        ## Note

        There are 3 cases: 

        1. if p and q are in the left adn right tree --> in the case of example 1 

        2. if q is a descendent of p --> in example 2 

        3. if p is a descendent of q --> mirror example 2

        For the current node, we explore the left tree 

        if node == p or node == q:
            return (since we already found a plausbile solution) 

        now we would search the right tree 

        NOTE: This would lead to the same 3 cases, except it would lead to 2 outcomes: 
        1. in case1, we would find our q in the right tree! 

        2. else, we would return an empty node, since both tree are "technically" in the left tree 

        hence if we recieve a null node, then that means its either case 2 /3 => return the left node p/q as the solution!


        Note that we sort of perform pruning here, since if we found p / q we can isntantly return / stop searching ! s
        essentially we are diving down until we see our solution, then once we get it , return upwards ! 
        """

        if not root: 
            return None

        if root == p or root == q:
            return root 
        
        # explore the left and right tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both left and right node are not null, then that means we have hit case 1! 
        if left and right: 
            return root

        return left if left else right 