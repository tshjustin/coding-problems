# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1. As we traverse, we need to form the string, but how do we traverse and build this string - depends on how we deserialize it 


2. For deserializing, we need to ensure that handle the nodes correctly -> do we have enough information to construct with the given ? 

try
----
perform an pre-order traversal, since we want to note the root 

[1, 2, null, null, 3, 4, 5] ==> but this is not accounting for all the nulls that we see

[1, 2, null, null, 3, 4, null, null, 5, null, null] ==> to get the solution , we can shift the firstr element after the double null up 

[1, 2, 3, null, null, 4, 5]


note
-----
since dont have to follow leetcode format, 

1. can just use anymeans to convert to string 

2. but from this string, ensure we get back the same binary tree 


"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "null"

        traversal = []

        def dfs(root): 

            if not root: 
                traversal.append("null")
                return 

            traversal.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(traversal) # 1,2,null,null,3,4,null,null,5,null,null
        

    def deserialize(self, data):
        """
        now need to retrieve the tree from the string 

        1,2,null,null,3,4,null,null,5,null,null

        ==> building back the tree from a pre-order traversal 


        Observations 

        1. When a node is accompanied by 2 nulls ==> it is a leaf node 

        2. If a node is accompanied by another another node, then 2 leafs, then that node is the parent of a leaf 

        3. the pattern A B N N C N N => A is the parent of B and C 

        4. consider the cases where 2 has a left child + None OR None + right child

        2 6 N N N   | 2 N  6 B N N => Notice the grouping of 3 NN nodes ==> its a subtree 


        5. so we can build from the root
            a. from the root, build a subtree, meaning left and right child 
            b. from this left and right child, build their own subtree ==> recurse 

        6. what does that mean with our data string? 


        OR we can take it element by element 

        if we see a node
            build 

        if we see a Null:
            return 

        """

        if not data: 
            return "null"

        vals = data.split(",")
        index = [0]  

        def build(): 
            if vals[index[0]] == "null":
                index[0] +=1
                return 

            node = TreeNode(int(vals[index[0]]))
            index[0] +=1 

            node.left = build()

            node.right = build()

            return node # need to return since we created the node, hence node.left = .. is making the connections
        
        return build()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))