class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        treat each word as a node 

        hot --> cog => Differ by 2 letters 

        hot --> dot => Differ by 1 letter 


        1. Form a graph of words in the world list --> if differ by 1 character , then there is an edge 

        2. Find the shortest path from the start node to the end node via these connections 

        3. Since we want a shortest path, use BFS 


        Do we need an adj list ? => very expensive since need to check and then iterate all 
        
        or just visit neighbours on the fly 

        try
        ---
        1. Starting from the start word 

        2. Enqueue it 

        3. Find all the neigbours of this start node 
            a. check difference to ensure validity of the neighbour 
            b. need to find all the neighbour inside the wordList efficiently 
            

            ==> this 2 steps can be lumped together 

            {
                "*ot": hot, dot 
                "h*t": hot, 
                "ho*": hot, 

                "d*t": dot, 
                'do*": dot, 
                ....
            }

            # 1. we have gotten rid of the difference checking 
            # 2. we can find neigbours effectively 

        4. enqueue them 

        5. traverse until find solution 

        6. return traversal count 



        time complexity matters here 
        -----------------------------

        number of words = N
        word length = M

        1. if we create an adjlist 
            for each word: 
                calculate difference and patterns 


                -> O(N^2M)


        2. in the below, preprocesisng ==> O(N × M²), pattern_matching ==> O(m), since just need to scan through the words



        bfs time compleixty
        ------------------
        in the worst case of a fully connected graph 

        1. enqueue all nodes 
        2. explore all relationships 
        O(v+e)
        """


        if endWord not in wordList: 
            return 0 

        from collections import deque, defaultdict 


        # preprocess the patterns  # pattern: [words]
        pattern_dict = defaultdict(list)

        for word in wordList: 
            for i in range(len(word)): 
                pattern = word[:i] + "*" + word[i+1:] 
                pattern_dict[pattern].append(word)

        def find_neighbours(word): 
            """
            Given the preprocess patterns of the above, need to find the neighbours 

            1. for the current word, find all the patterns that it has => remove char one by one 

            2. for each of the pattern, check with the pattern_dict ==> just a simple scan 
            """

            neigbours = [] 
            for i in range(len(word)): 
                pattern = word[:i] + "*" + word[i+1:]
                neigbours.extend(pattern_dict[pattern])
            return neigbours 

        visited = set()
        queue = deque([(beginWord, 1)]) # (word, current_length)

        while queue: 

            current_word, current_length = queue.popleft()

            if current_word == endWord: 
                return current_length 

            visited.add(current_word) # actually its better to add when enqueueing generally --> would always prevent duplicates 

            neigbours = find_neighbours(current_word)

            for neigbour in neigbours:
                if neigbour not in visited: 
                    queue.append((neigbour, current_length+1))

        return 0 

