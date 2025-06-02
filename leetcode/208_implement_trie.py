class TrieNode:
    def __init__(self): 
        self.children = [0] * 26 
        self.isEnd = False # Determines if the node is the end 

"""
Start with a root node -> That is essentially an empty array [0] * 26 

for word in words:  

    index = ord(word) - ord('a')
    
    # if there are no children here
    if TrieNode.children[index] is null: ? 
        TrieNode()

        # add the child

But the problem is that how do we link the nodes together ? 

In this case there are not pointers, so just instantiate a TrieNode inside a TrieNode 

"""

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        
        for char in word: 
            
            index = ord(char) - ord('a')
            
            # this check here would see if a new node is required to be instantiated 
            # else we just traverse until not empty 
            if node.children[index] == 0: 
                node.children[index] = TrieNode() # this would instantiate a char - since we are using indexes 

            # traverse the tree 
            node = node.children[index]
        
        # at the end mark the path as completed 
        node.isEnd = True 

    def search(self, word: str) -> bool:

        """
        Search the tree, word by word

        If the word is found, then we should have exhausted all the words. 

        Since we are finding a word match, we MUST end with a flag 
        """

        node = self.root

        for char in word: 

            index = ord(char) - ord('a')

            # if no char to continue 
            if node.children[index] == 0: 
                return False 

            node = node.children[index]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for char in prefix: 

            index = ord(char) - ord('a')

            if node.children[index] == 0: 
                return False 

            node = node.children[index]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)